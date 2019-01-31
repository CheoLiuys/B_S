from django.db import models

class Teacher(models.Model):
    '''教师表'''
    teacherId = models.CharField(max_length=32)#教师工号
    teacherName = models.CharField(max_length=32)#教师姓名
    teacherTel = models.CharField(max_length=32)#教师手机号
    teacherEmail = models.EmailField()#教师邮箱
    teacherFaculty = models.CharField(max_length=32)#教师所属院系
    teacherSub = models.CharField(max_length=10)#关联科目表的科目代号

class TeacherAccount(models.Model):
    '''教师账号/密码表'''
    userName = models.CharField(max_length=32)#教师登录账号（teacherId）
    passWord = models.CharField(max_length=32)#教师登录密码
# Create your models here.
