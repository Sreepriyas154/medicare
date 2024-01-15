from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class login(models.Model):
    logid = models.AutoField(primary_key=True)
    username = models.CharField("username",max_length=100)
    password =  models.CharField("password",max_length=100)
    role=models.CharField('role',max_length=10)

class user(models.Model):
    user_id=models.AutoField(primary_key=True)
    u_name=models.CharField("u_name",max_length=100)
    u_dob=models.CharField("u_dob",max_length=100)
    u_email=models.CharField("u_email",max_length=100)
    u_contact=models.CharField("u_contact",max_length=100)
    u_address=models.CharField("u_address",max_length=300)
    bloodgroup=models.CharField("u_bloodgroup",max_length=300)
    # u_aadarno=models.CharField("u_aadarno",max_length=100)
    
    # p_detail=models.CharField("p_detail",max_length=100)
    # m_detail=models.CharField("m_deetaigl",max_length=100)
    # rqrd_service=models.CharField("rqrd_service",max_length=100)
    # ration_card=models.CharField("ration_card",max_length=100)
    # Class_id=models.ForeignKey(clas,on_delete=models.CASCADE,null=True)
    # u_status=models.CharField("u_status",max_length=100)
    u_log_id=models.ForeignKey(login,on_delete=models.CASCADE,null=True)

class Hospital(models.Model):
    hospitalname=models.CharField(max_length=250)
    

