from django.shortcuts import render,HttpResponseRedirect
from Teacher.models import *

import hashlib
def setPassword(password):
    '''密码加密函数'''
    md5 = hashlib.md5()
    md5.update(password.encode())
    result = md5.hexdigest()
    return result

def login(request):
    '''登录页'''
    result = {'status':''}
    if request.method == 'POST' and request.POST:
        userName = request.POST.get('username')
        password = request.POST.get('pass')
        teachAcc = TeacherAccount.objects.filter(userName=userName).first()
        if teachAcc:
            dbPassword = teachAcc.passWord
            if setPassword(password) == dbPassword:
                response = HttpResponseRedirect('/teacher/index/')
                response.set_cookie('userName',teachAcc.userName)
                return response
            else:
                result['status'] = 'passError'
        else:
            result['status'] = 'noUser'

    return render(request,'teacher/login.html',locals())

def register(request):
    '''注册页'''
    result = {'status':''}
    if request.method == 'POST' and request.POST:
        #获取前端数据
        userName = request.POST.get('username')
        passwd = request.POST.get('pass')
        password = request.POST.get('password')
        if passwd == password:
            #将数据写入数据库（教师账号/密码表）
            teachAcc = TeacherAccount()
            teachAcc.userName = userName
            teachAcc.passWord = setPassword(passwd)
            teachAcc.save()
            result['status'] = 'success'
        else:
            result['status'] = 'error'
    return render(request,'teacher/register.html',locals())

def index(request):
    '''主页'''
    teacherId = request.COOKIES.get('userName')
    teachAcc = TeacherAccount.objects.filter(userName=teacherId).first()
    teachInfo = Teacher.objects.filter(teacherId=teacherId).first()

    return render(request,'teacher/index.html',locals())

def info(request):
    '''教师信息录入/修改页'''
    teacherId = request.COOKIES.get('userName')
    teacher = Teacher.objects.filter(teacherId=teacherId).first()
    result = {'state':''}
    if teacher:
        if request.method == 'POST' and request.POST:
            teacher.teacherName = request.POST.get('username')
            teacher.teacherTel = request.POST.get('phone')
            teacher.teacherEmail = request.POST.get('email')
            teacher.teacherFaculty = request.POST.get('faculty')
            teacher.teacherSub = request.POST.get('subject')
            teacher.save()
            result['state'] = '1'
    else:
        if request.method == 'POST' and request.POST:
            teachInfo = Teacher()
            teachInfo.teacherId = teacherId
            teachInfo.teacherName = request.POST.get('username')
            teachInfo.teacherTel = request.POST.get('phone')
            teachInfo.teacherEmail = request.POST.get('email')
            teachInfo.teacherFaculty = request.POST.get('faculty')
            teachInfo.teacherSub = request.POST.get('subject')
            teachInfo.save()
            result['state'] = '1'
    return render(request,'teacher/info.html',locals())

def changePassword(request):
    '''修改密码页'''
    result = {'statu':''}

    if request.method == 'POST' and request.POST:
        teacher = TeacherAccount.objects.filter(userName=request.COOKIES.get('userName')).first()

        newPassword = request.POST.get('pass')
        reNewPassword = request.POST.get('repass')
        oldPassword = teacher.passWord
        if newPassword == reNewPassword:
            if setPassword(newPassword) == oldPassword:
                result['statu'] = 'same'
            else:
                teacher.passWord = setPassword(newPassword)
                teacher.save()
                result['statu'] = 'success'
        else:
            result['statu'] = 'error'
    return render(request,'teacher/changePassword.html',locals())

# Create your views here.
