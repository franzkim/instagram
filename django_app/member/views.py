from django.contrib.auth import \
    login as django_login, \
    logout as django_logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from member.forms.user import UserEditForm
from .forms import LoginForm, SignupForm

User = get_user_model()













