from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import kanjic2j as kj
from kanjic2j_web.forms import KanjiForm
from kanjic2j_web.models import Log
from django.utils import timezone

def index(request):
	form2 = u''
	if request.method == 'POST':
		form = KanjiForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			mylyric = kj.Lyrics(cd['content'])
			form2 = mylyric.work().data
			mxp =Log(use_time=timezone.now(),filename=form2[:15],
				address=request.META['HTTP_X_FORWARDED_FOR'] if
				request.META.has_key('HTTP_X_FORWARDED_FOR') else
				request.META['REMOTE_ADDR'])
			mxp.save()
	else:
		form = KanjiForm()
	context={'form':form,'form2':form2}
	return render(request,"kanji/index.html",context)

