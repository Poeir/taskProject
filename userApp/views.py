from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.
def register(request):
    if request.method == 'POST':
        #ส่งข้อมูลจากฟอร์มมา
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if username == '' or password == '' or confirm_password == '':
            messages.warning(request, 'กรุณากรอกข้อมูลให้ครบถ้วน')
            return redirect('/register')
        else:
            if password != confirm_password:
                messages.warning(request, 'รหัสผ่านไม่ตรงกัน')
                return redirect('/register')
            else:
                
                #ตรวจสอบว่ามี username นี้ในระบบแล้วหรือไม่
                if User.objects.filter(username=username).exists():
                    messages.warning(request, 'มีชื่อผู้ใช้งานนี้ในระบบแล้ว')
                    return redirect('/register')
                else:
                    #สร้าง user
                    user = User.objects.create_user(
                        username=username, 
                        password=password)
                    user.save
                    messages.success(request, 'สมัครสมาชิกสำเร็จ')
                    redirect('/register')
                return redirect('/login')
    else:
        #แสดงฟอร์ม
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        #รับค่าจากแบบฟอร์ม
        username = request.POST['username']
        password = request.POST['password']
        if username == '' or password == '':
            messages.warning(request, 'กรุณากรอกข้อมูลให้ครบถ้วน')
            return redirect('/login')
        else:
            #ตรวจสอบเข้าสู่ระบบ
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                #มีข้อมูล
                auth.login(request,user)
                return redirect('/')
            else:
                #ไม่มีข้อมูล
                messages.warning(request, 'ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง')
                return redirect('/login')
    else:
        return render(request, 'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/login')