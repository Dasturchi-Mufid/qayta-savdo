from django.http import HttpResponse,JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from databse import get_db_myconfig,get_db
from dotenv import load_dotenv
from .models import Guest, Comment
from .decorators import login_required_session
from . import queries
from . import func
import os, json
import pandas as pd


load_dotenv()

branches = json.loads(os.getenv('BRANCHES'))



@login_required_session
def home(request):
    
    uuid = request.session.get('user',None)
    try:
        guest = Guest.objects.get(uuid=uuid)
    except Guest.DoesNotExist:
        return redirect('login')
    context = {
        'name':guest.name,
        'branches':branches,
        'guest':guest}
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
        
        if user and func.verify_password(hashed_password=user[5],plain_password=password):
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
    sellers = [{
        "id":i[0],
        "name":i[1],
        } for i in func.get_data(query=queries.sellers,db=get_db(dbname=branch))]
    
    if not branch:
        return redirect('login')
    
    try:
        guest = Guest.objects.get(uuid=uuid)
    except Guest.DoesNotExist:
        return redirect('login')
    
    if guest.branch != 'ofice':
        branch = guest.branch

    if request.method == 'POST' and guest.branch=='ofice' and request.POST.get('branch'):
        branch = request.POST.get('branch')
        request.session['branch'] = branch
    
    if request.method == 'POST' and request.POST.get('seller'):
        print(f"seller id: {request.POST.get('seller')}")

    ball,ball_limit = [int(i) for i in func.get_data(query=queries.variable,db=get_db(dbname=branch))[0]]
    params = (func.get_date()[0],func.get_date()[1],ball,ball,ball_limit)
    
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
        } for i in func.get_data(queries.customers,params=params,db=get_db(dbname=branch))]
    
    if request.method == 'POST' and request.POST.get('excel') and customer:
        # customer = []
        return func.download_people_xlsx(request,customer)
    queryset = func.paginator_page(customer,10,request)
    
    context = {
        "customers":queryset,
        "sellers":sellers,
        'name':guest.name,
        'branches':branches,
        'guest':guest,
        'is_customer_page': True,
        }
    return render(request, 'customers/list.html', context)

@login_required_session
def customer_detail(request,id):
    branch = request.session.get('branch')

    if not branch:
        return redirect('login')

    ball,ball_limit = [int(i) for i in func.get_data(query=queries.variable,db=get_db(dbname=branch))[0]]
    params = (func.get_date()[0],func.get_date()[1],ball,ball,ball_limit)
    all_customer = func.get_data(query=queries.customers,params=params,db=get_db(dbname=branch))
    num = func.binary_search(all_customer,id)
    customer = all_customer[num]
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

    context = {
        "customer":customer,
        'name':guest.name,
        'comments':comments,
        'branches':branches,
        'guest':guest,
        'is_customer_page': True,
        }
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


def seller_list(request,branch):
    uuid = request.session.get('user',None)
    branch = request.session.get('branch',None)
    try:
        guest = Guest.objects.get(uuid=uuid)
    except Guest.DoesNotExist:
        return redirect('login')
    if guest.branch != 'ofice':
        branch = guest.branch

    if request.method == 'POST' and guest.branch=='ofice':
        branch = request.POST.get('branch')
        request.session['branch'] = branch
    seller_s = [{"id":i[0],"name":i[1]} for i in func.get_data(query=queries.sellers,db=get_db(dbname=branch))]

    context = {
        "sellers":seller_s,
        'branches':branches,
        'guest':guest,
        'is_customer_page': False,
        }
    return render(request,'sellers/list.html',context)



def seller_detail(request,id=None,s_id=None):
    
    uuid = request.session.get('user',None)
    branch = request.session.get('branch')

    try:
        guest = Guest.objects.get(uuid=uuid)
    except Guest.DoesNotExist:
        return redirect('login')
    params = [id,func.get_date()[0],func.get_date()[1]]
    
    sellers_deal = [{
        "deal_number":i[0],
        "date":i[1],
        "name":i[2],
        "lname":i[3],
        "pnfl":i[4],
        "sum_one":i[5],
        "sum_two":i[6],
        "term":i[7],
        "s_id":i[8],
        "id":i[9]
        } for i in func.get_data(query=queries.seller_deal,db=get_db(dbname=branch),params=params)]
    print(sellers_deal)
    void_contracts = [
        {
            "deal_number":i[0],
            "date":i[1],
            "name":i[2],
            "lname":i[3],
            "pnfl":i[4],
            "sum_one":i[5],
            "sum_two":i[6],
            "term":i[7]
            } for i in func.get_data(query=queries.void_contracts,db=get_db(dbname=branch),params=params)
        ]
    s_id = s_id if s_id else sellers_deal[0]['s_id'] 
    
    params_info = [s_id,func.get_date()[1]]
    seller_info = [
        {
            "deal_number":i[0],
            "date":i[1],
            "sum_one":i[2],
            "term":i[3],
            "monthly_payment":round(i[2] / i[3],2) if i[3] != 0 else 0,
            "debt":i[4],
            } for i in func.get_data(query=queries.seller_info,db=get_db(dbname=branch),params=params_info)
    ]

    context = {
        'branches':branches,
        'guest':guest,
        'sellers_deal':sellers_deal,
        'void_contracts':void_contracts,
        'seller_info':seller_info,
        'is_customer_page': False,
        }
    return render(request,'sellers/detail.html',context)


def upload(request):
    print(request.FILES.get('file'))

def process_excel_file(file,branch):
    # Read the Excel file into a pandas DataFrame
    df = pd.read_excel(file)

    # Process each row in the DataFrame
    for index, item in df.iterrows():
        customer_id = item.get('xaridor id')
        seller_id = item.get('xodim id')
        dbname = item.get('filial')

        print(dbname)
        print(branches.values())
        print(dbname in branches.keys())
        print(seller_id > 0)
        print(customer_id > 0)
        
        if customer_id > 0 and seller_id > 0 and dbname==branch:
            # func.update_xaridor(branch=dbname,seller_id=seller_id,customer_id=customer_id)
            print(1)
        else:
            return False
    else:
        return 
    True
        

# Django view to handle the file upload
def upload_excel(request):
    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']
        res = process_excel_file(file=uploaded_file,branch=request.session.get('branch'))

    if res:
        messages.success(request, 'Sotuvchilar muvaffaqiyatli biriktirildi.')
        return redirect('customers',request.session.get('branch'))
    messages.error(request,'Fayl ichidagi ma`lumotlar to`g`riligiga e`tibor bering!')
        


