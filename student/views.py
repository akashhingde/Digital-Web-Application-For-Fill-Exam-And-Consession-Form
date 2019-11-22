from django.shortcuts import render,redirect
from django .template import loader
from .forms import *
from django.contrib.auth.decorators import login_required
from .models import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView,View
from django.views.generic import CreateView
from django.urls import reverse,reverse_lazy
from django.contrib import messages
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.db.models import Q
from datetime import date
from datetime import datetime
import json



@login_required
def home(request):

	return render(request,'home.html')

def change_password(request, user):
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = request.user
			post.save()
			update_session_auth_hash(request, user)  # Important!
			messages.success(request, 'Your password was successfully updated!')
			return redirect('change_password')
		else:
			messages.error(request, 'Please correct the error below.')
	else:
		form = PasswordChangeForm(request.user)
	return render(request, 'change_password.html', {
		'form': form
	})



class ExamformCreateView(CreateView):
	model = examformmodel
	form_class = examform
	success_url = reverse_lazy('home')

def load_semesters(request):
	year_id = request.GET.get('year')
	semesters = Semester.objects.filter(year_id=year_id).order_by('name')
	
	# subjects = Subject.objects.filter(semesters_id=semesters_id).order_by('name')
	
	return render(request, 'student/semester_dropdown_list_options.html', {'semesters': semesters})

def load_subjects(request):
	semesters_id = request.GET.get('q')
	branch_id = request.GET.get('branch')
	subjects = Subject.objects.raw('SELECT * FROM student_Subject WHERE semester_id = %s AND branch_id = %s', [semesters_id, branch_id])
	print(subjects)
	subject_list = []
	for sub in subjects:
		subject_list.append(sub)
	print(subject_list)	 
	return render(request, 'student/subject_dropdown_list_options.html', {'subjects':subject_list})	

def load_subjects1(request):
	semesters_id = request.GET.get('q')
	branch_id = request.GET.get('branch')
	subjects = Subject.objects.raw('SELECT * FROM student_Subject WHERE semester_id = %s AND branch_id = %s', [semesters_id, branch_id])
	print(subjects)
	subject_list = []
	for sub in subjects:
		subject_list.append(sub)
	print(subject_list)	 
	# return render(request, 'student/subject_dropdown_list_options.html', {'subjects':subject_list})
	return subject_list

def load_subjects_for_print(request):
	semesters_id = request.GET.get('q')
	branch_id = request.GET.get('branch')
	subjects = Subject.objects.raw('SELECT * FROM student_Subject WHERE semester_id = %s AND branch_id = %s', [semesters_id, branch_id])
	print(subjects)
	subject_list = []
	for sub in subjects:
		subject_list.append(sub)
	return render(request, 'student/subject_dropdown_list_options_for_print.html', {'subjects':subject_list})	

def load_subjects_atkt(request):
	semesters_id = request.GET.get('q')
	branch_id = request.GET.get('branch')
	subjects = Subject.objects.raw('SELECT * FROM student_subject  WHERE semester_id = %s AND branch_id = %s', [semesters_id, branch_id])
	subject_list = []
	for sub in subjects:
		subject_list.append(sub)
	print(subject_list)	
	return render(request, 'student/subject_dropdown_list_options_for_print.html', {'subjects':subject_list})	




class UserProfileModelUpdate(UpdateView):
	model = UserProfileModel
	fields = ['full_name','gender','age','mobile_no','birth_date','current_year','category','address'
,'image']
	template_name = 'update_form.html'
	success_url = reverse_lazy('home')
	def user_passes_test(self, request):
		if request.user.is_authenticated():
			self.object = self.get_object()
			return self.object == request.user.profile
		return False

	def dispatch(self, request, *args, **kwargs):
		if not self.user_passes_test(request):
			return redirect('home')
		return super(UserProfileModelUpdate, self).dispatch(
			request, *args, **kwargs)

class examcelladminUpdate(UpdateView):
	model = examcelladmin
	fields = ['full_name','mobile_no','address'
,'image']
	template_name = 'update_form1.html'
	success_url = reverse_lazy('home')
	def user_passes_test(self, request):
		if request.user.is_authenticated():
			self.object = self.get_object()
			return self.object == request.user.examcelladmin
		return False

	def dispatch(self, request, *args, **kwargs):
		if not self.user_passes_test(request):
			return redirect('home')
		return super(examcelladminUpdate, self).dispatch(
			request, *args, **kwargs)

class concessionadminUpdate(UpdateView):
	model = consessionadmin
	fields = ['full_name','mobile_no','address','image']
	template_name = 'update_form2.html'
	success_url = reverse_lazy('home')
	def user_passes_test(self, request):
		if request.user.is_authenticated():
			self.object = self.get_object()
			return self.object == request.user.consessionadmin
		return False

	def dispatch(self, request, *args, **kwargs):
		if not self.user_passes_test(request):
			return redirect('home')
		return super(concessionadminUpdate, self).dispatch(
			request, *args, **kwargs)


def railwaypass(request):
	crequest = consessionformmodel.objects.all()
	if request.method == 'POST':
		form = concessionform(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = request.user
			post.save()
			return redirect('home')
	else:
		form = concessionform
	return render(request,'railwaypass.html',{'form':form,'crequest':crequest,'request':request.user})

def newrailwaypass(request):
	crequest = newconsessionformmodel.objects.all()
	if request.method == 'POST':
		form = newconcessionform(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = request.user
			post.save()
			return redirect('home')
	else:
		form = newconcessionform
	return render(request,'newrailwaypass.html',{'form':form,'crequest':crequest,'request':request.user})	

def Regular_Examination(request):
	subject = Subject.objects.all()
	subject_list = []
	for p in Subject.objects.raw('SELECT * FROM student_Subject'):
		a = p.name
		subject_list.append(a)
		# semester_list.append(semester)
	
	branch_list = []
	for a in Branch.objects.raw('SELECT * FROM student_Branch'):
		
		bra = a.name
		branch_list.append(bra)

		
	semester_list = []
	for b in Semester.objects.raw('SELECT * FROM student_Semester'):
	
		s = b.name
		
		semester_list.append(b.name)
	
	# options_for_js = json.dumps(subject_list)	
	# print(options_for_js)
	if request.method == 'POST':
		form = examform(request.POST)
		
		if form.is_valid():
			post = form.save(commit=False)
			post.user = request.user
			post.save()
			return redirect('Regular_Examination')
			
			# print(form)
	else:
		form = examform
	
	return render(request,'Regular_Examination.html',{'form':form, 'subject':subject,'sub':subject_list,'branch':branch_list, 'semester':semester_list})


def select_Subject(request):
	Subject = Subject.objects.all()
	return render(request,'Regular_Examination.html',{'Subject':Subject})

def ATKT_Examination(request):

	if request.method == 'POST':
		form = atktform(request.POST)
		if form.is_valid():
			print("form")
			post = form.save(commit=False)
			post.user = request.user
			post.save()
			return redirect('ATKT_Examination')

	else:
		form = atktform
	return render(request,'ATKT_Examination.html',{'form':form})

def Regular_Revaluation(request):
	if request.method == 'POST':
		form = regularrevalutionform(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = request.user
			post.save()
			return redirect('Regular_Revaluation')
	else:
		form = regularrevalutionform
	print(render(request,'Regular_Revaluation.html',{'form':form}))
	return render(request,'Regular_Revaluation.html',{'form':form})

def ATKT_Revaluation(request):
	if request.method == 'POST':
		form = atktrevalutionform(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = request.user
			post.save()
			return redirect('ATKT_Revaluation')
	else:
		form = atktrevalutionform
	return render(request,'ATKT_Revaluation.html',{'form':form})

def Regular_PhotoCopy(request):
	if request.method == 'POST':
		form = regularphotocopyform(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = request.user
			post.save()
			return redirect('Regular_PhotoCopy')
	else:
		form = regularphotocopyform

	return render(request,'Regular_PhotoCopy.html',{'form':form})

def ATKT_PhotoCopy(request):
	if request.method == 'POST':
		form = atktphotocopyform(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = request.user
			post.save()
			return redirect('ATKT_PhotoCopy')
	else:
		form = atktphotocopyform

	return render(request,'ATKT_PhotoCopy.html',{'form':form})

def detail(request, student_id):
	student_id=student.objects.get(id=student_id)

	context={
			'name':name
		}
	return render(request,'detail.html',context)


def consessionrequest(request):
	crequest = consessionformmodel.objects.all()

	query = request.GET.get('q')
	if query:
		crequest = consessionformmodel.objects.filter(from_date__icontains=query)
	return render(request,'concessionrequestlist.html',{'crequest':crequest})

def newconsessionrequest(request):
	crequest = newconsessionformmodel.objects.all()
	query = request.GET.get('q')
	if query:
		crequest = newconsessionformmodel.objects.filter(from_date__icontains=query)
	return render(request,'newconcessionrequestlist.html',{'crequest':crequest})	

def response(request):
	if request.POST.get('accept'):
		result = 1
	else:
		result = 2
	r = consessionformmodel.objects.get(id=request.POST.get('request_id'))
	r.status = result

	r.save()
	return redirect('consessionrequest')

def newresponse(request):
	if request.POST.get('accept'):
		result = 1
	else:
		result = 2
	r = newconsessionformmodel.objects.get(id=request.POST.get('request_id'))
	r.status = result

	r.save()
	return redirect('newconsessionrequest')	

def responseExamrequest(request):
	if request.POST.get('accept'):
		result = 1
	else:
		result = 2
	r = examformmodel.objects.get(id=request.POST.get('request_id'))
	r.status = result

	r.save()
	return redirect('studentrequest')

def responseatktExamrequest(request):
	if request.POST.get('accept'):
		result = 1
	else:
		result = 2
	r = atktmodel.objects.get(id=request.POST.get('request_id'))
	r.status = result

	r.save()
	return redirect('studentatktrequest')	
		

def responseregularrevalution(request):
	if request.POST.get('accept'):
		result = 1
	else:
		result = 2
	r = regularrevalutionmodel.objects.get(id=request.POST.get('request_id'))
	r.status = result

	r.save()
	return redirect('regularrevalutionrequest')	

def responseatktrevalution(request):
	if request.POST.get('accept'):
		result = 1
	else:
		result = 2
	r = atktrevalutionmodel.objects.get(id=request.POST.get('request_id'))
	r.status = result

	r.save()
	return redirect('atktrevalutionrequest')	

def responseregularphotocopy(request):
	if request.POST.get('accept'):
		result = 1
	else:
		result = 2
	r = regularphotocopymodel.objects.get(id=request.POST.get('request_id'))
	r.status = result

	r.save()
	return redirect('regularphotocopyrequest')	

def responseatktphoto(request):
	if request.POST.get('accept'):
		result = 1
	else:
		result = 2
	r = atktphotocopymodel.objects.get(id=request.POST.get('request_id'))
	r.status = result

	r.save()
	return redirect('atktphotocopyrequest')	



def hallticket(request):
	examrequest = examformmodel.objects.all()
	return render(request,'hallticket.html',{'examrequest':examrequest})

def printhallticket(request):
	examrequest = examformmodel.objects.all()
	return render(request,'printhallticket.html',{'examrequest':examrequest})	

def printatkthallticket(request):
	return render(request,'printatkthallticket.html')	

def printatkt(request):
	examrequest = atktmodel.objects.all()
	return render(request,'printatkt.html',{'examrequest':examrequest})

def acknowledgementregularrevalution(request):
	return render(request,'acknowledgementregularrevalution.html')

def acknowledgementatktrevalution(request):
	return render(request,'acknowledgementatktrevalution.html')

def acknowledgementregularphotocopy(request):
	return render(request,'acknowledgementregularphotocopy.html')

def acknowledgementatktphotocopy(request):
	return render(request,'acknowledgementatktphotocopy.html')
		

	

def studentrequest(request):
	
	examrequest=examformmodel.objects.all()
	branch=Branch.objects.all()
	query=request.GET.get('q')
	if query:
		examrequest=examformmodel.objects.filter(branch__name__icontains=query)
	semesters_id = request.GET.get('sem')
	branch_id = request.GET.get('branch')
	subjects = Subject.objects.raw('SELECT * FROM student_Subject WHERE semester_id = %s AND branch_id = %s', [semesters_id, branch_id])
	print("subjects:",subjects)
	subject_list = []
	for sub in subjects:
		subject_list.append(sub)
	return render(request,'studentrequest.html',{'examrequest':examrequest,'branch':branch,'subjects':subject_list})

def load_subjects_for_examcell(request):
	semesters_id = request.GET.get('sem')
	branch_id = request.GET.get('branch')
	subjects = Subject.objects.raw('SELECT * FROM student_Subject WHERE semester_id = %s AND branch_id = %s', [semesters_id, branch_id])
	print("subject",subjects)
	subject_list = []
	for sub in subjects:
		subject_list.append(sub)
	return render(request, 'student/subject_dropdown_list_options_for_examcell.html', {'subjects':subject_list})	



def studentatktrequest(request):
	examrequest = atktmodel.objects.all()
	query = request.GET.get('q')
	if query:
		examrequest = examformmodel.objects.filter(branch__name__icontains=query)
	return render(request,'studentatktrequest.html',{'examrequest':examrequest})

def regularrevalutionrequest(request):
	examrequest = regularrevalutionmodel.objects.all()
	query = request.GET.get('q')
	if query:
		examrequest = examformmodel.objects.filter(branch__name__icontains=query)
	return render(request,'regularrevalutionrequest.html',{'examrequest':examrequest})

def atktrevalutionrequest(request):
	examrequest = atktrevalutionmodel.objects.all()
	query = request.GET.get('q')
	if query:
		examrequest = examformmodel.objects.filter(branch__name__icontains=query)
	return render(request,'atktrevalutionrequest.html',{'examrequest':examrequest})

def regularphotocopyrequest(request):
	examrequest = regularphotocopymodel.objects.all()
	query = request.GET.get('q')
	if query:
		examrequest = examformmodel.objects.filter(branch__name__icontains=query)
	return render(request,'regularphotocopyrequest.html',{'examrequest':examrequest})

def atktphotocopyrequest(request):
	examrequest = atktphotocopymodel.objects.all()
	query = request.GET.get('q')
	if query:
		examrequest = examformmodel.objects.filter(branch__name__icontains=query)
	return render(request,'atktphotocopyrequest.html',{'examrequest':examrequest})

@login_required
def newSelectedSubject(request,id):
	sub=Subject.objects.get(id=id)
  
	SelectedSubject.objects.get_or_create(student=request.user.profile,subject=sub)
   

	return render("Regular_Examination")

@login_required
def newSubject(request):
		newsub=request.POST.get('name')
		if newsub:
			newsub=newsub.replace(' ','_')
			newsub=newsub.replace(r"'",'')

			Subject.objects.get_or_create(faculty=request.user.faculty,subject_name=newsub.lower())


		return render("Regular_Examination")

def regulerprint(request):
	examrequest = examformmodel.objects.all()
	subject_list = []
	for p in Subject.objects.raw('SELECT * FROM student_Subject'):
		a = p.name
		subject_list.append(a)
		# semester_list.append(semester)
	print(subject_list)

	return render(request,'print.html',{'examrequest':examrequest, 'subject_list':subject_list})

def uploadresult(request):
	if request.method == 'POST':
		form = uploadresultform(request.POST, request.FILES)
		if form.is_valid():
			form.save()

			return redirect('home')
			
			
	else:
		form = uploadresultform()	
	return render(request,'uploadresult.html',{'form':form})

def result(request):
	all_result = uploadresultmodel.objects.all()
	return render(request,'result.html',{'all_result':all_result})

def uploadnotice(request):
	if request.method == 'POST':
		form = uploadnoticeform(request.POST, request.FILES)
		if form.is_valid():
			form.save()

			return redirect('home')
			
			
	else:
		form = uploadnoticeform()	
	return render(request,'uploadnotice.html',{'form':form})	

def notice(request):
	all_notice = uploadnoticemodel.objects.all().order_by('-date')
	return render(request,'notice.html',{'all_notice':all_notice})	
# Create your views here.
