from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from kanji.forms import KanjiForm

def index(request):
	if request.method == 'POST':
		form = KanjiForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			import kanjic2j
			cd['content']
	else:
		form = KanjiForm()
		form2 = KanjiForm()
	context={'form':form,'form2':form2}
	return render(request,"kanji/index.html",context)

