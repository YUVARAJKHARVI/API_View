from django.http.response import HttpResponse
from django.shortcuts import render

#Api Starts from here

def factorial(request):
    #if only execute the function when requested method is GET
    if request.method == 'GET':
        #a random value assign to n 
        n = 5   
        fact = 1
        
        #for loop for increment the number and calculation
        for i in range(1,n+1):
            #multiplies previous value and the current index
            fact = fact * i
        
        #this line for html responce
        html='<html><body>Factorial of 5 is %s.</body></html>' % fact

        #return the http responce to webpage
        return HttpResponse(html)

#I have deployed a above API in 
# https://roadwayexpress.pythonanywhere.com/api/auth/5
# you can check in and pass value in url 
#Thank you


#***This is an API which accepts value in Url ***

def factorial(request,n):
    #if only execute the function when requested method is GET
    if request.method == 'GET':
        #convert the type str to int
        m=int(n)

        fact = 1
        #for loop for increment the number and calculation
        for i in range(1,m+1):
            #multiplies previous value and the current index
            fact = fact * i
        
        #context to pass the value to web page
        ans={
            'n':m,
            'fact':fact
        }
        #return the render the ans to web page
        return render(request,'factorial.html',{"ans":ans})


 