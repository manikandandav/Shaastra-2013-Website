#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
from dajax.core import Dajax
from django.utils import simplejson
from django.template import loader, Context, RequestContext, Template
from controlroom.models import *
from controlroom.forms import *
from dajaxice.decorators import dajaxice_register
from django.core.cache import cache
from django.contrib.sitemaps import ping_google
from operator import attrgetter

@dajaxice_register
def save_individual_checkin(request,form):
    dajax =Dajax()
    individual_form=IndividualForm(form)
    if individual_form.is_valid():
        form = individual_form.save()
        room = AvailableRooms.objects.get(id = form.room_id)
        room.already_checkedin = room.already_checkedin + 1
        room.save()
        msg = "Checked In Successfully!"
        dajax.alert(msg)
    else:
        msg = "Invalid Form" 
        dajax.alert(msg)
    return dajax.json()

@dajaxice_register
def save_individual_checkout(request,form,shaastraid):
    dajax =Dajax()
    checkedin = IndividualCheckIn.objects.get(shaastra_ID=shaastraid)
    individual_form=IndividualForm(form, instance = checkedin)
    if individual_form.is_valid():
        form = individual_form.save()
        room = AvailableRooms.objects.get(id = form.room_id)
        room.already_checkedin = room.already_checkedin - 1
        room.save()
        msg = "Checked Out Successfully!"
        dajax.alert(msg)
    else:
        msg = "Invalid Form" 
        dajax.alert(msg)
    return dajax.json()
