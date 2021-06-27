from django.shortcuts import render

# Create your views here.
def welcome_students(request):
	return render(request=request, template_name='greetingApp/disp.html')
	