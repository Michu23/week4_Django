from django.shortcuts import render,redirect
from django.views.decorators.cache import never_cache

# Create your views here.


def ultimate(request):
    return render(request, 'base.html',{'name':'Michu'})

def base(request):
    title='Title'
    para="Lorem ipsum is placeholder text commonly used in the graphic, print, and publishing industries for previewing layouts and visual mockups."
    link='Google'
    myDict=[{'title':title,'paragraph':para,'link':link},
            {'title':title,'paragraph':para,'link':link},
            {'title':title,'paragraph':para,'link':link}]
    
    return render(request, 'home.html',{'context':myDict,'name':'Michu'})

@never_cache
def home(request):
    if request.session.has_key('login'):
        return render(request, 'main.html',{'name':'Michu'})
    else:
        return redirect('login')

@never_cache
def login(request):
    if request.session.has_key('login'):
        return redirect('home')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'michu' and password == 'django':
            request.session['login']=username
            return redirect('home')
        else:
            error = "The username and password not correct!"
            return render(request, 'login.html', {'error':error})
    else:
        return render(request, 'login.html',{'name':'Michu'})
@never_cache 
def logout(request):
    if request.session.has_key('login'):
        del request.session['login']
        return redirect('login')
    else:
        return redirect('login')
        



