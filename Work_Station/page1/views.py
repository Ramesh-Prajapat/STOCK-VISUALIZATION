from django.shortcuts import render
from django.http import HttpResponse
from .models import RussellData
import MySQLdb

# Create your views here.

def home(request):
    return render(request,'front_page.html')

def get_start(request):
    return render(request, 'get_started.html')

def about(request):
    return render(request, 'about.html')
def choose_cmp(request):
    return render(request, 'get_started.html')

def show_data(request):
    if request.method=='POST':
        TICKER1 = request.POST['ticker']
        DATE1 = request.POST['d_date']
        data = RussellData(TICKER=TICKER1, D_DATE=DATE1)
        if data is None:
            print("There entry for this date")
        else:
            context = {}
            db = MySQLdb.connect("localhost", "root", "Qp$_a400", "data_visualization")
            cur = db.cursor()
            # Fetch data from table
            sql = "SELECT * FROM page1_russelldata WHERE TICKER='{}' AND D_DATE='{}'".format(data.TICKER, data.D_DATE)
            print(sql)
            cur.execute(sql)
            re = cur.fetchall()
            context = {
                'ticker': re[0][1],
                'date': re[0][2],
                'open': re[0][3],
                'high': re[0][4],
                'low': re[0][5],
                'close': re[0][6],
                'adj_close': re[0][7],
                'volume': re[0][8],
            }
            print('context : - ',context)
            print(re)
            db.close()
            return render(request, 'show_data.html', context)
        #print(DATE1)
    else:
        return render(request, 'show_data.html')

def profile(request):
    return HttpResponse("Your profile")