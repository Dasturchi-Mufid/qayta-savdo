from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger,EmptyPage
from .models import Guest, Comment
from databse import get_db_myconfig,get_db
from .decorators import login_required_session
from .queries import customers,variable
from dotenv import load_dotenv
import bcrypt
import datetime
import calendar
import openpyxl
import os
import json

load_dotenv()

branches = json.loads(os.getenv('BRANCHES'))


def binary_search(arr, target):
    low, high = 0, arr[-1][0] - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid][0] == target:
            return mid
        elif arr[mid][0] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1 

def verify_password(plain_password: str, hashed_password: str) -> bool:
    # Check if the plain password matches the hashed password
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

def paginator_page(List,num,request):
    paginator = Paginator(List,num)
    page = request.GET.get('page')
    try:
        List = paginator.page(page)
    except PageNotAnInteger:
        List = paginator.page(1)
    except EmptyPage:
        List = paginator.page(paginator.num_pages)
    return List

def get_date():
    current_date = datetime.date.today()
    first_day = current_date.replace(day=1)
    last_day = current_date.replace(day=calendar.monthrange(current_date.year, current_date.month)[1])

    return first_day,last_day


def get_data(query,db,params=[]):
    
    db.execute(query,params)
    users = db.fetchall()
    return users

def download_people_xlsx(request, data):
    # Create a workbook and a worksheet
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = 'People Data'

    # Set the headers for the columns
    headers = [
        'Xaridor ID', 'Xaridor FIO', 'Telefon raqam', 'Telefon raqam','Passport', 'JSHSHR', 
        'Tug`ilgan kun', 'Xarid limiti oy boshi', 'Joriy oy xaridi', 'Qoldiq','Xarid %','Xarid uchun kelish sanasi',
        'Sotuvchi','Mas`ul hodim'
    ]
    
    # Write the headers to the first row
    sheet.append(headers)

    # Ensure that data is not empty and properly structured
    if not data:
        print("No data to write to the file.")
    
    # Write data rows
    for row in data:
        # Ensure the row is a dictionary and append values to the Excel sheet
        sheet.append([
            row.get('id', ''),
            row.get('name', ''),
            row.get('phone', [])[0] if len(row.get('phone', [])) > 0 else '',  # Ensure phone has at least one element
            row.get('phone', [])[1] if len(row.get('phone', [])) > 1 else '',  # Ensure there's a second phone number
            row.get('passport', ''),
            row.get('pnfl', ''),
            row.get('birth_date', ''),
            row.get('purchase_limit', ''),
            row.get('current_purchase', ''),
            row.get('balance', ''),
            row.get('percent', ''),
            row.get('come_date', ''),
            row.get('seller', ''),
            row.get('manager', ''),
        ])

    # Set the column widths (optional)
    column_widths = [10, 45, 15, 15, 11, 15, 15, 30, 30, 30,8,24,45,45]
    for i, width in enumerate(column_widths, 1):
        sheet.column_dimensions[openpyxl.utils.get_column_letter(i)].width = width

    # Create a response object with 'Content-Type' for Excel
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        charset='utf-8'
    )
    response['Content-Disposition'] = 'attachment; filename="people_data.xlsx"'

    try:
        # Save the workbook to the response object
        workbook.save(response)
    except Exception as e:
        print(f"Error saving workbook: {e}")
        response = HttpResponse("Error generating file.", status=500)

    return response

@login_required_session
def home(request):
    print(request.session.items())
    uuid = request.session.get('user',None)
    try:
        guest = Guest.objects.get(uuid=uuid)
    except Guest.DoesNotExist:
        return redirect('login')
    context = {'name':guest.name,'branches':branches,'guest':guest}
    return render(request, 'index.html',context)


def login(request,db=get_db_myconfig()):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        db.execute(f"select * from users where logins='{username}'")
        user = db.fetchone()
        if not user:
            messages.error(request,'Bunday foydalanuvchi mavjud emas')
            return render(request,'auth/login.html')
        
        if user and verify_password(hashed_password=user[5],plain_password=password):
            guest = Guest.objects.get_or_create(
                user=user[0],
                name=user[1],
                position_id=user[3],
                branch=user[4],
                )
            
            request.session['user'] = str(guest[0].uuid)
            request.session['branch'] = str('q') if guest[0].branch == 'ofice' else guest[0].branch
            return redirect('home')
        messages.error(request,'Login yoki parol xato')
    return render(request, 'auth/login.html')

def logout(request):
    
    if request.session.get('user',None):
        del request.session['user']
    return redirect('login')

@login_required_session
def customers_list(request,branch):

    uuid = request.session.get('user',None)
    branch = request.session.get('branch',None)
    if not branch:
        return redirect('login')
    
    try:
        guest = Guest.objects.get(uuid=uuid)
    except Guest.DoesNotExist:
        return redirect('login')
    
    if guest.branch != 'ofice':
        branch = guest.branch

    if request.method == 'POST' and guest.branch=='ofice':
        branch = request.POST.get('branch')
        request.session['branch'] = branch

    ball,ball_limit = [int(i) for i in get_data(query=variable,db=get_db(dbname=branch))[0]]
    params = (get_date()[0],get_date()[1],ball,ball,ball_limit)
    
    customer = [{
        "id":i[0],
        "name":i[1],
        "phone":[i[5],i[6]],
        "passport":i[3],
        "pnfl":i[2],
        "birth_date":i[4],
        "purchase_limit":i[9],
        "current_purchase":i[8],
        "balance":i[9]-i[8],
        "percent":round((i[9]-i[8])/i[9]*100,2) if i[9] != 0 else 0,
        "come_date":i[11],
        "seller":i[7],
        "manager":i[10]
        } for i in get_data(customers,params=params,db=get_db(dbname=branch))]
    
    if request.method == 'POST' and request.POST.get('excel') and customer:
        # customer = []
        return download_people_xlsx(request,customer)
    queryset = paginator_page(customer,10,request)
    
    context = {"customers":queryset,'name':guest.name,'branches':branches,'guest':guest}
    return render(request, 'customers/list.html', context)

@login_required_session
def customer_detail(request,id):
    branch = request.session.get('branch')

    if not branch:
        return redirect('login')

    ball,ball_limit = [int(i) for i in get_data(query=variable,db=get_db(dbname=branch))[0]]
    params = (get_date()[0],get_date()[1],ball,ball,ball_limit)
    all_customer = get_data(query=customers,params=params,db=get_db(dbname=branch))
    num = binary_search(all_customer,id)
    customer = all_customer[num]
    print(customer)
    uuid = request.session.get('user',None)
    try:
        guest = Guest.objects.get(uuid=uuid)
    except Guest.DoesNotExist:
        return redirect('login')
    comments = Comment.objects.filter(customer_id=customer[0],branch=branch).order_by('-created_at')
    customer = {
    "id": customer[0],
    "name": customer[1],
    "phone": [customer[5], customer[6]],
    "passport": customer[3],
    "pnfl": customer[2],
    "birth_date": customer[4],
    "purchase_limit": customer[9],
    "current_purchase": customer[8],
    "balance": customer[9] - customer[8],
    "percent": round((customer[9] - customer[8]) / customer[9] * 100, 2) if customer[9] != 0 else 0,
    "come_date": customer[11],
    "seller": customer[7],
    "manager": customer[10]
}
    if customer.get('id') != id:
        customer = None

    context = {"customer":customer,'name':guest.name,'comments':comments,'branches':branches,'guest':guest}
    return render(request,'customers/detail.html',context=context)


def create_comment(request):
    if request.method == 'GET':
        return HttpResponse({"<center><h1>Method not allowed</h1></center>"})

    uuid = request.session.get('user',None)
    customer_id = request.POST.get('customer_id')
    try:
        guest = Guest.objects.get(uuid=uuid)
    except Guest.DoesNotExist:
        return redirect('login')
    if request.method == 'POST':
        comment = request.POST.get('comment')
        Comment.objects.create(
            guest=guest,
            customer_id=customer_id,
            branch=request.session.get('branch'),
            comment=comment
        )
    return redirect('customer_detail',customer_id)


def seller_detail(request,id=None):
    uuid = request.session.get('user',None)
    try:
        guest = Guest.objects.get(uuid=uuid)
    except Guest.DoesNotExist:
        return redirect('login')
    sellers = range(5)
    context = {'branches':branches,'guest':guest,'sellers':sellers}
    return render(request,'sellers/detail.html',context)


