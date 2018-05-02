from django.shortcuts import render,redirect
from django.http import HttpResponse
import gvcode
# Create your views here.
def get_code(request):
	base64_str, code = gvcode.base64()

	# 把code存到session中
	request.session['verify_code'] = code
	# 把base64_str 返回给用户
	return HttpResponse(base64_str)





def user_login(request):
	if request.method == 'POST':
		#获得用户输入的验证码
		user_code = request.POST.get('code').lower()
		print('user_code',user_code)
		#获取实际的验证码
		act_code = request.session.get('verify_code').lower()
		print('act_code',act_code)
		# #进行验证
		if user_code == act_code:
			return HttpResponse('验证成功')
	return render(request,'vertify_code.html')