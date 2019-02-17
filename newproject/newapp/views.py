from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, "index.html")

def student(request):
	return render(request, "student.html")

def mine(request):
	return render(request, "mine.html")

def bot(request):
	return render(request, "bot.html")
