from django.shortcuts import render,redirect
from .models import Image_gallery,Contact_detail,Pooja_booking,Fund_donation,Blood_donation
import random
from django.views.decorators.csrf import csrf_exempt
from .paytm import Checksum
from Project1 import settings
MERCHANT_KEY = 'gpup7U%PxQ1T6y8u';

def home(request):
    params={'name':'janki patel','c':205}
    return render(request,'Proapp/index1.html',params)

def index(request):
    return render(request,'Proapp/index.html')

'''def payment(request):
    return render(request,'Proapp/paymentpage.html')'''

def contact(request):
    if request.method== "POST":
        name=request.POST.get('cname','')
        email=request.POST.get('cemail','')
        phone=request.POST.get('cphone','')
        msg=request.POST.get('cmessage','')

        print(name,email,phone,msg)
        contact=Contact_detail(name=name,email=email,phone_no=phone,message=msg)
        contact.save()

    return render(request,'Proapp/contact.html')

def poojabooking(request):
    if request.method == "POST":
        fname = request.POST.get('fname','')
        mname = request.POST.get('mname','')
        lname = request.POST.get('lname','')
        address = request.POST.get('address','')
        emailid = request.POST.get('emailid','')
        nopeople = request.POST.get('nopeople','')
        pdate = request.POST.get('bdate','')
        ptime = request.POST.get('btime','')
        pcategory = request.POST.get('pcategory','')
        city = request.POST.get('city','')
        zipcode = request.POST.get('zip','')
        token_no=random.randint(100000,999999)



        pbooking=Pooja_booking(fname=fname,mname=mname,lname=lname,address=address,emailid=emailid,
                               nopeople=nopeople,pdate=pdate,ptime=ptime,pcategory=pcategory,
                               city=city,zipcode=zipcode)
        pbooking.save()
        data=[[fname,mname,lname,address,emailid,nopeople,pdate,ptime,pcategory,city,zipcode,token_no]]
        params={'data':data}
        return render(request,'Proapp/poojabookingform.html',params)
    return render(request,'Proapp/poojabooking.html')

def basic(request):
    return render(request,'Proapp/basic.html')

def imagegallery(request):
    allimgs = []
    catimg = Image_gallery.objects.values('category', 'image_id')
    catitems = {item['category'] for item in catimg}
    for c in catitems:
        images = Image_gallery.objects.filter(category=c)
        n = len(images)
        allimgs.append([images, n, c])
    print(allimgs)
    params = {'allimgs': allimgs, 'cat': catitems}
    return render(request, 'Proapp/imagegallery.html',params)
def about(request):
    return render(request,'Proapp/about.html')
def facilities(request):
    return render(request,'Proapp/facilities.html')
def funddonation(request):

    if request.method == "POST":
        fname = request.POST.get('fname','')
        mname = request.POST.get('mname','')
        lname = request.POST.get('lname','')
        address = request.POST.get('address','')
        emailid = request.POST.get('emailid','')
        mobileno = request.POST.get('mobno','')
        city = request.POST.get('city','')
        zipcode = request.POST.get('zip','')
        damount = int(request.POST.get('damount',''))

        fdonation=Fund_donation(fname=fname,mname=mname,lname=lname,address=address,
                                emailid=emailid,mobileno=mobileno,city=city,zipcode=zipcode,
                                damount=damount)
        fdonation.save()
        # return render(request, 'shop/checkout.html', {'thank':thank, 'id': id})
        # Request paytm to transfer the amount to your account after payment by user
        param_dict = {

            'MID': 'byLVwz55811088203547',
            'ORDER_ID': str(fdonation.fid),
            'TXN_AMOUNT': str(damount),
            'CUST_ID': emailid,
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL': 'http://127.0.0.1:8000/handlerequest/',

        }
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        return render(request, 'Proapp/paytm.html', {'param_dict': param_dict})

        return render(request, 'Proapp/facilities.html')
    return render(request,'Proapp/funddonation.html')
def blooddonation(request):

    if request.method == "POST":
        fname = request.POST.get('fname','')
        mname = request.POST.get('mname','')
        lname = request.POST.get('lname','')
        address = request.POST.get('address','')
        emailid = request.POST.get('emailid','')
        mobileno = request.POST.get('mobno','')
        bdate = request.POST.get('bdate','')
        btime = request.POST.get('btime','')
        bgroup = request.POST.get('bgroup','')
        city = request.POST.get('city','')
        zipcode = request.POST.get('zip','')
        feedback = request.POST.get('feedback','')

        bdonation=Blood_donation(fname=fname,mname=mname,lname=lname,address=address,
                                emailid=emailid,mobileno=mobileno,bdate=bdate,
                                 btime=btime,bgroup=bgroup,city=city,zipcode=zipcode,
                                feedback=feedback)
        bdonation.save()
        return render(request,'Proapp/facilities.html')
    return render(request,'Proapp/blooddonation.html')

@csrf_exempt
def handlerequest(request):
    # paytm will send you post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'Proapp/paymentstatus.html', {'response': response_dict})

    '''if request.method == "POST":
        MERCHANT_KEY = settings.PAYTM_MERCHANT_KEY
        data_dict = {}
        for key in request.POST:
            data_dict[key] = request.POST[key]
        verify = Checksum.verify_checksum(data_dict, MERCHANT_KEY, data_dict['CHECKSUMHASH'])
        if verify:
            Fund_donation.objects.create(user=request.user, **data_dict)
            return render(request, "response.html", {"paytm": data_dict})
        else:
            return HttpResponse("checksum verify failed")
    return HttpResponse(status=200)'''



