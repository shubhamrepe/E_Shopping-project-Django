from django.shortcuts import render, redirect,HttpResponse
from .models import Product,CartItem,Order
from django.db.models import Q
from. forms import CreateUserForm,AddProduct
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
import random
import razorpay
# Create your views here.
def index(req):
    product=Product.objects.all()
    context={}
    context['products']=product
    return render(req,"index.html",context)

def details(req,pid):
    products=Product.objects.get(product_id=pid)
    context={'products':products}
    return render(req,"detail.html",context)

def cart(req):
    if req.user.is_authenticated:
        allproducts = CartItem.objects.filter(user= req.user)
    else:
        return redirect('/login')
    context ={}
    context['cart_item'] = allproducts
    total_price =0
    for x in allproducts:
        total_price += (x.product.price * x.quantity)
        print(total_price)
    context['total'] = total_price
    length = len(allproducts)
    context['items']=length
    return render(req,"cart.html",context)

def add_cart(req,pid):
    products=Product.objects.get(product_id=pid)
    user = req.user if req.user.is_authenticated else None
    print(products)
    if user:
        cart_item,created= CartItem.objects.get_or_create(product=products,user=user)
        print(cart_item,created)
    else:
         return redirect('/login')
        # cart_item,created= CartItem.objects.get_or_create(product=products)

    if not created:
        cart_item.quantity += 1
    else:
        cart_item.quantity = 1
    cart_item.save()
    
    return redirect("cart")

def remove(request,pid):
    info = CartItem.objects.filter(product_id = pid,user = request.user)
    #print(info)
    info.delete()
    return redirect("cart")


def search(req):
    query=req.POST['q'] 
   # print(f"Recieved Query is {query}")
    if not query:
        result=Product.objects.all()
    else:
        result=Product.objects.filter(
            Q(product_name__icontains=query)|
             Q(price__icontains=query)
        )
    return render(req,"search.html",{'result':result,'query':query})

def range(req):
    if req.method == "GET":
        return redirect("/")
    else:
        r1 = req.POST["min"]
        r2 = req.POST["max"]
        print(r1,r2)
        if r1 is not None and r2 is not None and r1 != "" and r2 !="": 
            queryset = Product.objects.filter(price__range = (r1,r2))
            context= {'products':queryset}
            return render(req,"index.html",context)
        
def watchList(req):
    queryset = Product.prod.watch_list()
    #print(queryset)
    context= {'products':queryset}
    return render(req,"index.html",context)

def sort(req):
    queryset= Product.objects.all().order_by('price')
    context= {'products':queryset}
    return render(req,"index.html",context)

def hightolow(req):
    queryset= Product.objects.all().order_by('-price')
    context= {'products':queryset}
    return render(req,"index.html",context)

def updateQty(req,uval,pid):
    products= Product.objects.get(product_id =pid)
    user = req.user
    c = CartItem.objects.filter(product = products, user=user)
    print(c)
    print(c[0])
    print(c[0].quantity)
    if uval == 1:
        a = c[0].quantity + 1
        c.update(quantity = a)
        print(c[0].quantity)
    else:
        a = c[0].quantity - 1
        c.update(quantity = a)
        print(c[0].quantity)

    return redirect("cart")

def register_user(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,("User Cerate Sucessfully"))
            return redirect("/login")
        else:
            messages.error(request,("incoirect Password Format"))
            return redirect("/register")
    context ={'form': form}
    return render(request,"register.html",context)


def login_user(req):
    if req.method =='POST':
        username = req.POST['username']
        password = req.POST['password']
        user = authenticate(req, username=username,password=password)
        if user is not None:
            login(req,user)
            messages.success(req,('You Have Been Logged In'))
            return redirect('/')
        else:
            messages.error(req,('incorrect Username Or Password'))
            return redirect('/login')
    else:
        return render(req,"login.html")

# def user_logout(req):
#     logout(req)
#     messages.success(req('Log Out Sucessfully'))
#     return redirect('/')

def user_logout(req):
    logout(req)
    messages.success(req, 'Log Out Successfully')  # Fix the typo here
    return redirect('/')

def viewOrder(req):
    c= CartItem.objects.filter(user=req.user)
    # oid = random.randrange(1000,9999)
    # for x in c:
    #     Order.objects.create(order_id = oid, product_id= x.product.product_id, user = req.user,quantity=x.quantity)
    # orders = Order.objects.filter(user = req.user,is_completed=False)
    context ={}
    context['cart_item'] = c
    total_price =0
    for x in c:
        total_price += (x.product.price * x.quantity)
        print(total_price)
    context['total'] = total_price
    length = len(c)
    context['items']=length
    return render(req,"viewOrder.html",context)

def makePayment(req):
    c = CartItem.objects.filter(user = req.user)
    oid = random.randrange(1000,9999)
    for x in c:
        Order.objects.create(order_id = oid, product_id= x.product.product_id, user = req.user,quantity=x.quantity)
        orders = Order.objects.filter(user = req.user,is_completed=False)
    total_price =0
    for x in orders:
        total_price += (x.product.price * x.quantity)
        oid = x.order_id
    client = razorpay.Client(auth=("rzp_test_aC8eVIkARyNcLQ", "1ofQ2R52Po58tdDj5gDvOhcv"))
    data = {
    "amount": total_price * 100,
    "currency": "INR",
    "receipt": "oid",
    }
    payment =client.order.create( data = data)
    context= {}
    context['data'] = payment
    context['amount']= payment ['amount']
    #empting cart
   
    c.delete()
    orders.update(is_completed = True)
    return render (req,"payment.html",context)

def insertProduct(req):
    if req.user.is_authenticated:
        user=req.user
        if req.method =="GET":
            form = AddProduct()
            return render(req,"insertProd.html",{'form':form})
        else:
            form = AddProduct(req.POST,req.FILES or None)
            if form.is_valid():
                form.save()
                messages.success(req,("Product Enterde Sucessfully"))
                return redirect("/")
            else:
                messages.error(req,("incorrect Data"))
                return render(req,"insertProd.html",{'form':form})
            
    else:
        return render('/login')

