from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import razorpay
# Create your views here.
def home(request):
    if request.method=="POST":
        order_amount = 10000 #counts in paisa 
        order_currency = 'INR'
        client=razorpay.Client(auth=("rzp_test_0yjbWo8nLJPZCK","zDFisijM4bggFTtNplFxmFsp")) 
        payment=client.order.create({"amount":order_amount, "currency":order_currency,"payment_capture":"1"})
        a=request.POST['name']
        return render(request,"success.html",{'b':a})    
    return render(request,"index.html")

    