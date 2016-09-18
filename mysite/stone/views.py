# -*- coding: utf-8 -*-

#from django.http import HttpResponse
from django.shortcuts import render,render_to_response,HttpResponse
from django.http import HttpResponseRedirect
from stone.models import note
from django.template import Context

def homepage(request):
    context          = {}
    #context['homepage'] = {}
    context['news'] = '本公司网页刚做好，所以很开心发个公告'
    return render(request, 'homepage.html', context)

def About(request):
    context          = {}
    #context['homepage'] = {}
    context['news'] = '本公司网页刚做好，所以很开心发个公告'
    return render(request, 'About.html', context)

def hjm(request):
    context         ={}
    #context['hjm']  ={};
    context['news'] = '本公司网页刚做好，所以很开心发个公告'
    return render_to_response('hjm.html',context)

def hxs(request):
    context         ={}
    #context['hjm']  ={};
    context['news'] = '本公司网页刚做好，所以很开心发个公告'
    return render_to_response('hxs.html',context)

def yx(request):
    context         ={}
    #context['hjm']  ={};
    context['news'] = '本公司网页刚做好，所以很开心发个公告'
    return render_to_response('yx.html',context)

def hzxm(request):
    context         ={}
    #context['hjm']  ={};
    context['news'] = '本公司网页刚做好，所以很开心发个公告'
    return render_to_response('hzxm.html',context)

def bm(request):
    context         ={}
    #context['hjm']  ={};
    context['news'] = '本公司网页刚做好，所以很开心发个公告'
    return render_to_response('bm.html',context)

def lys(request):
    context         ={}
    #context['hjm']  ={};
    context['news'] = '本公司网页刚做好，所以很开心发个公告'
    return render_to_response('lys.html',context)

def hl(request):
    context         ={}
    #context['hjm']  ={};
    context['news'] = '本公司网页刚做好，所以很开心发个公告'
    return render_to_response('hjm.html',context)

def gc(request):
    context         ={}
    #context['hjm']  ={};
    context['news'] = '本公司网页刚做好，所以很开心发个公告'
    return render_to_response('hjm.html',context)


def gcal(request):
    context         ={}
    #context['hjm']  ={};
    c=Context({ 'news':'本公司网页刚做好，所以很开心发个公告',
                'first':'工程案例(1)',
                'second':'工程案例(2)',
                'third':'工程案例(3)',
                'forth':'工程案例(4)',
                'fifth':'工程案例(5)',
                'sixth':'工程案例(6)',
                'picture1':'picture1',
                'picture2':'picture2',
                'picture3':'picture3',
                'picture4':'picture4',
                'picture5':'picture5',
                'picture6':'picture6',
                'picture01':'/static/img/gcal/1.png',
                'picture02':'/static/img/gcal/2.png',
                'picture03':'/static/img/gcal/3.png',
                'picture04':'/static/img/gcal/4.png',
                'picture05':'/static/img/gcal/5.png',
                'picture06':'/static/img/gcal/6.png',

                })
    return render_to_response('gcal.html',c)

def feedback(request):
    context={}
    context['news'] = '本公司网页刚做好，所以很开心发个公告'
    if request.POST:
        post=request.POST
        new_note=note(
            theme=post["theme"],
            content=post["content"],
            name=post["name"],
            phone=post["phone"],
        )
        new_note.save()
        return HttpResponseRedirect('/')
    return render_to_response('feedback.html',context)

def service(request):
    context         ={}
    #context['hjm']  ={};
    notes=note.objects.all()
    c=Context({"notes":notes,'news':'本公司网页刚做好，所以很开心发个公告',})
    return render_to_response('service.html',c)

def picture1(request):
    context={}
    c=Context({ 'news':'本公司网页刚做好，所以很开心发个公告',
                'last':'回到首页',
                'next':'工程案例(2)',
                'picture0':'/static/img/gcal/1.png',
                'lastweb':'/gcal',
                'nextweb':'/gcal/picture2',
                })
    return render_to_response('picture1.html',c)   

def picture2(request):
    context={}
    c=Context({ 'news':'本公司网页刚做好，所以很开心发个公告',
                'last':'工程案例(1)',
                'next':'工程案例(3)',
                'picture0':'/static/img/gcal/2.png',
                'lastweb':'/gcal/picture1',
                'nextweb':'/gcal/picture3',
                })
    return render_to_response('picture2.html',c)   

def picture3(request):
    context={}
    c=Context({ 'news':'本公司网页刚做好，所以很开心发个公告',
                'last':'工程案例(2)',
                'next':'工程案例(4)',
                'picture0':'/static/img/gcal/3.png',
                'lastweb':'/gcal/picture2',
                'nextweb':'/gcal/picture4',
                })
    return render_to_response('picture3.html',c)   

def picture4(request):
    context={}
    c=Context({ 'news':'本公司网页刚做好，所以很开心发个公告',
                'last':'工程案例(3)',
                'next':'工程案例(5)',
                'picture0':'/static/img/gcal/4.png',
                'lastweb':'/gcal/picture3',
                'nextweb':'/gcal/picture5',
                })
    return render_to_response('picture4.html',c)   

def picture5(request):
    context={}
    c=Context({ 'news':'本公司网页刚做好，所以很开心发个公告',
                'last':'工程案例(4)',
                'next':'工程案例(6)',
                'picture0':'/static/img/gcal/5.png',
                'lastweb':'/gcal/picture4',
                'nextweb':'/gcal/picture6',
                })
    return render_to_response('picture5.html',c)  

def picture6(request):
    context={}
    c=Context({ 'news':'本公司网页刚做好，所以很开心发个公告',
                'last':'工程案例(5)',
                'next':'工程案例(7)',
                'picture0':'/static/img/gcal/6.png',
                'lastweb':'/gcal/picture5',
                'nextweb':'/gcal/picture7',
                })
    return render_to_response('picture6.html',c)   


def delete(request,offset):
    offset=int(offset)
    p=note.objects.get(id=offset)
    p.delete()
    return HttpResponseRedirect('/')
def top(request):
    return render('top.html')
def bottom(request):
    return render('bottom.html')
def left_contect(request):
    return render('left_contect.html')   
def left_contect1(request):
    return render('left_contect1.html')   
def left_contect0(request):
    return render('left_contect0.html')   

def picture(request):
    return render(request,'picture.html')   

def list(request):
    return render(request,'list.html')
def list_5(request):
    return render(request,'list_5.html')
def list_4(request):
    return render(request,'list_4.html')
def list_3(request):
    return render(request,'list_3.html')
def list_2(request):
    return render(request,'list_2.html')
def list_1(request):
    return render(request,'list_1.html')
def culture(request):
    context={}
    c=Context({ 'news':'本公司网页刚做好，所以很开心发个公告',

                })
    return render_to_response('culture.html',c)   
def news(request):
    context={}
    c=Context({ 'news':'本公司网页刚做好，所以很开心发个公告',

                })
    return render_to_response('news.html',c)   
def product(request):
    context={}
    c=Context({ 'news':'本公司网页刚做好，所以很开心发个公告',

                })
    return render_to_response('product.html',c)   
def hiring(request):
    context={}
    c=Context({ 'news':'本公司网页刚做好，所以很开心发个公告',

                })
    return render_to_response('hiring.html',c)  
def contect(request):
    context={}
    c=Context({ 'news':'本公司网页刚做好，所以很开心发个公告',

                })
    return render_to_response('contect.html',c)  

def gcal_Index_1(request):
    context         ={}
    #context['hjm']  ={};
    c=Context({ 'news':'本公司网页刚做好，所以很开心发个公告',
                'first':'工程案例(1)',
                'second':'工程案例(2)',
                'third':'工程案例(3)',
                'forth':'工程案例(4)',
                'fifth':'工程案例(5)',
                'sixth':'工程案例(6)',
                'picture1':'picture1',
                'picture2':'picture2',
                'picture3':'picture3',
                'picture4':'picture4',
                'picture5':'picture5',
                'picture6':'picture6',
                'picture01':'/static/img/gcal/1.png',
                'picture02':'/static/img/gcal/2.png',
                'picture03':'/static/img/gcal/3.png',
                'picture04':'/static/img/gcal/4.png',
                'picture05':'/static/img/gcal/5.png',
                'picture06':'/static/img/gcal/6.png',

                })
    return render_to_response('gcal_Index_1.html',c)

def gcal_Index_2(request):
    context         ={}
    #context['hjm']  ={};
    c=Context({ 'news':'本公司网页刚做好，所以很开心发个公告',
                'first':'工程案例(7)',
                'second':'工程案例(8)',
                'third':'工程案例(9)',
                'forth':'工程案例(10)',
                'fifth':'工程案例(11)',
                'sixth':'工程案例(12)',
                'picture1':'picture7',
                'picture2':'picture8',
                'picture3':'picture9',
                'picture4':'picture10',
                'picture5':'picture11',
                'picture6':'picture12',
                'picture01':'/static/img/gcal/7.png',
                'picture02':'/static/img/gcal/8.png',
                'picture03':'/static/img/gcal/9.png',
                'picture04':'/static/img/gcal/10.png',
                'picture05':'/static/img/gcal/11.png',
                'picture06':'/static/img/gcal/12.png',

                })
    return render_to_response('gcal_Index_2.html',c)

def gcal_Index_3(request):
    context         ={}
    #context['hjm']  ={};
    c=Context({ 'news':'本公司网页刚做好，所以很开心发个公告',
                'first':'工程案例(13)',
                'picture1':'picture1',
                'picture01':'/static/img/gcal/13.png',

                })
    return render_to_response('gcal_Index_3.html',c)

def list_cpzs(request):
    return ('list_cpzs.html')