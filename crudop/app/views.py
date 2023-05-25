from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q


def topic(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}
    return render(request,'sample1.html',d)

def web(request):
    LOW=Webpage.objects.all()
    LOW=Webpage.objects.filter(topic_name='FootBall')
    LOW=Webpage.objects.exclude(topic_name='FootBall')
    LOW=Webpage.objects.all()[1:2:]
    LOW=Webpage.objects.all().order_by('name')
    LOW=Webpage.objects.all().order_by('-name')
    LOW=Webpage.objects.all().order_by(Length('name'))
    LOW=Webpage.objects.all().order_by(Length('name').desc())
    LOW=Webpage.objects.all()
    LOW=Webpage.objects.filter(name__startswith='m')
    LOW=Webpage.objects.filter(email__endswith='.com')
    LOW=Webpage.objects.filter(name__contains='C')
    #LOW=Webpage.objects.filter(name__in=('Ram'))
    LOW=Webpage.objects.filter(name__regex='[a-zA-Z]{6}')
    LOW=Webpage.objects.filter(Q(topic_name='RRR')&(Q(name='Ram Charan & NTR')))
    LOW=Webpage.objects.filter(Q(topic_name='Varasudu'))
    d={'web':LOW}
    return render(request,'sample2.html',d)

def access(request):
    LOA=AccessRecord.objects.all()
    d={'access':LOA}
    return render(request,'sample3.html',d)