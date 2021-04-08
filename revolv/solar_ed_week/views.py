import datetime
import threading

from django.http import JsonResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from revolv.lib.mailer import send_revolv_email
from revolv.solar_ed_week.models import HostEvent, BecomePartner, BecomeSponsor
from datetime import timedelta
from django.db.models import Count

def solar_education(request):
    today = datetime.datetime.today()
    host_events = HostEvent.objects.filter(date__gte=today).values()
    solar_counter = HostEvent.objects.filter(date__range=["2021-03-24", "2021-04-30"]).count()
    state_counter = HostEvent.objects.filter(date__range=["2021-03-24", "2021-04-30"]).values('state').annotate(the_count=Count('state')).count()
    return render_to_response('solar_ed_week/solar_ed_week.html',
                              context_instance=RequestContext(request, {'host_events': host_events,'solar_counter': solar_counter,'state_counter': state_counter}))    

def host_event(request):
    data = {}
    try:
        name = request.POST.get('name')
        email = request.POST.get('email')
        title = request.POST.get('event_title')
        evntime = request.POST.get('evntime')
        date = request.POST.get('date')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zipcode = request.POST.get('zipcode')
        event_detail = request.POST.get('event_detail')
        facebook_link = request.POST.get('eventbrite')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        HostEvent.objects.create(
            name=name,
            email=email,
            title=title,
            evntime=evntime,
            date=date,
            address=address,
            city=city,
            state=state,
            zip_code=zipcode,
            detail=event_detail,
            facebook_link=facebook_link,
            latitude=latitude,
            longitude=longitude
        )
        data["success"] = True
        data["message"] = "Saved successfully"
        context = {'name': name,
                   'email': email,
                   'title': title,
                   'date': date,
                   'address': address,
                   'city': city,
                   'state': state,
                   'zip_code': zipcode,
                   'detail': event_detail}
        thr = threading.Thread(target=send_email, args=('host_event_template', context), kwargs={})
        thr.start()
    except Exception:
        data["success"] = False
        data["message"] = "Error while saving data"

    return JsonResponse(data)


def become_partner(request):
    data = {}
    try:
        name = request.POST.get('partner_name')
        email = request.POST.get('partner_email')
        organization = request.POST.get('partner_organization')
        promote_solar = request.POST.get('promote_solar', False)
        promoting_way = request.POST.get('promoting_way')
        logo = request.FILES.get('partner_logo')
        BecomePartner.objects.create(
            name=name,
            email=email,
            organization=organization,
            promote_solar=promote_solar,
            promoting_way=promoting_way,
            logo=logo
        )
        data["success"] = True
        data["message"] = "Saved successfully"
        context = {'name': name, 'email': email, 'organization': organization, 'promote_solar': promote_solar,
                   'promoting_way': promoting_way}
        thr = threading.Thread(target=send_email, args=('become_partner_template', context), kwargs={})
        thr.start()
    except Exception:
        data["success"] = False
        data["message"] = "Error while saving data"

    return JsonResponse(data)


def become_sponsor(request):
    data = {}
    try:
        name = request.POST.get('sponsor_name')
        email = request.POST.get('sponsor_email')
        organization = request.POST.get('sponsor_organization')
        financially_support = request.POST.get('financially_support', False)
        logo = request.FILES.get('sponsor_logo')
        BecomeSponsor.objects.create(
            name=name,
            email=email,
            organization=organization,
            financially_support=financially_support,
            logo=logo
        )
        data["success"] = True
        data["message"] = "Saved successfully"
        context = {'name': name, 'email': email, 'organization': organization,
                   'financially_support': financially_support}
        thr = threading.Thread(target=send_email, args=('become_sponsor_template', context), kwargs={})
        thr.start()
    except Exception:
        data["success"] = False
        data["message"] = "Error while saving data"

    return JsonResponse(data)


def send_email(template, context):
    send_revolv_email(template, context, ['info@re-volv.org'])
