import bcrypt, datetime, calendar, openpyxl, os, fdb
from django.core.paginator import Paginator, PageNotAnInteger,EmptyPage
from django.http import HttpResponse
from dotenv import load_dotenv

load_dotenv()

DSN_CONFIG = os.getenv('DSN_CONFIG')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
CHARSET = os.getenv('CHARSET')

DSN_BRANCH = os.getenv('DSN_BRANCH')

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
    response['Content-Disposition'] = 'attachment; filename="customers.xlsx"'

    try:
        # Save the workbook to the response object
        workbook.save(response)
    except Exception as e:
        print(f"Error saving workbook: {e}")
        response = HttpResponse("Error generating file.", status=500)

    return response


def update_xaridor(branch,seller_id,customer_id):
    try:
        con = fdb.connect(
            dsn=DSN_BRANCH.format(branch),
            user=USER,
            password=PASSWORD,
            charset=CHARSET
        )
        cur = con.cursor()

        cur.execute(f'UPDATE XARIDOR SET FOYDALANUVCHI_ID ={seller_id} WHERE id={customer_id}')
        con.commit()
    finally:
        if cur:
            cur.close()
        if con:
            con.close()

def add_date():
    pass