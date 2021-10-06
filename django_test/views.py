from django.shortcuts import render
from django.http import HttpResponse
import pyrebase

config = {
  "apiKey": "AIzaSyB1IPU68U13Qx2ucJFvj89DhvTE1ZynkF4",
  "authDomain": "django-test-284bd.firebaseapp.com",
  "databaseURL": "https://django-test-284bd-default-rtdb.firebaseio.com",
  "projectId": "django-test-284bd",
  "storageBucket": "django-test-284bd.appspot.com",
  "messagingSenderId": "888794563759",
  "appId": "1:888794563759:web:5a0ed4ecb5874f0d82405a",
  "measurementId": "G-FJJVC95SMG"
}

firebase = pyrebase.initialize_app(config)
atuh = firebase.auth()
database = firebase.database() 

#all_products = database.child('products').order_by_child('prod_type').equal_to('smartphone').get()
# all_products = database.child('products').child('prod_id').order_by_child('prod_price').get()
# products = {}
# for i in all_products.each():
#     products[i.key()] = i.val()
#     print(products)

def index(request):
    # n = '11'
    # prod_name = database.child(n).child('prod_name').get().val()
    # prod_price = database.child(n).child('prod_price').get().val()
    # prod_qn = database.child(n).child('prod_qn').get().val()
    # prod_type = database.child(n).child('prod_type').get().val()
    # prod_color = database.child(n).child('prod_color').get().val()
    # all_products = database.child('products').child('prod_id').get()
    # products = {}
    # for i in all_products.each():
    #     products[i.key()] = i.val()
    cart_price = 90
    customer_id = 1
    # print(cart_price)
    # print(customer_id)
    summary = {
      'amount': cart_price,
      'customer_id': customer_id
    }
    print(summary)
  
    # return render(request, 'confirm.html', summary )
    return render(request, 'index.html', summary)

def home(request):
  return render(request, 'home1.html')

def Smartphone(request):
  all_products = database.child('products').child('prod_id').order_by_child('prod_type').equal_to('smartphone').get()
  products = {}
  for i in all_products.each():
    products[i.key()] = i.val()
  return render(request, 'smartphone.html', {"products": products})

def laptop(request):
  all_products = database.child('products').child('prod_id').order_by_child('prod_type').equal_to('laptop').get()
  products = {}
  for i in all_products.each():
    products[i.key()] = i.val()
  return render(request, 'laptop.html', {"products": products})

def watch(request):
  all_products = database.child('products').child('prod_id').order_by_child('prod_type').equal_to('watch').get()
  products = {}
  for i in all_products.each():
    products[i.key()] = i.val()
  return render(request, 'watches.html', {"products": products})

def headphone(request):
  all_products = database.child('products').child('prod_id').order_by_child('prod_type').equal_to('headphones').get()
  products = {}
  for i in all_products.each():
    products[i.key()] = i.val()
  return render(request, 'headphones.html', {"products": products})


def create(request):
  return render(request,"form.html")