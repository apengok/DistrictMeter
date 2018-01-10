# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request,"home.html",{"item_d":"dasfasdf"})


def main(request):
	print request.GET
	return render(request,"main.html",{})

def test(request,var):
	print var
	# var = request.get("var")
	return render(request,"home.html",{"item_d":var})