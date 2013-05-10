from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.template import RequestContext
from treatment.models import TreatmentPage


def home(request):
    most_recent = TreatmentPage.objects.filter(status=2).order_by('-publish_date')[:10]
    return render_to_response('index.html',
                              {"most_recent": most_recent},
                              context_instance=RequestContext(request))


def treatment(request, pageslug):
    treatment_data = get_object_or_404(TreatmentPage, slug=pageslug)
    return render_to_response('treatment/treatment.html',
                              {'treatment_data': treatment_data},
                              context_instance=RequestContext(request))