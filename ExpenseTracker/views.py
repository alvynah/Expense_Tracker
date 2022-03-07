from multiprocessing.sharedctypes import Value
from tarfile import NUL
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.http import HttpResponseRedirect
from .email import send_welcome_email
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage , PageNotAnInteger
from django.db.models import Sum
from django.http import JsonResponse
import datetime
from django.views.generic import TemplateView
from django.utils import timezone

# Create your views here.


def signup_view(request):
   if request.method == 'POST':
       form = SignUpForm(request.POST)
       if form.is_valid():

           form.save()
           username = form.cleaned_data.get('username')
           password = form.cleaned_data.get('password1')

           name = form.cleaned_data['username']
           email = form.cleaned_data['email']

           send_welcome_email(name, email)
           user = authenticate(username=username, password=password)

           login(request, user)

           return redirect('welcome')
   else:
       form = SignUpForm()
   return render(request, 'registration/signup.html', {'form': form})





def profile(request, username):
   current_user = request.user.profile
   user_profile = get_object_or_404(User, username=username)
   profile = Profile.objects.get(user=current_user.user)
   
   if request.method == 'POST':
      user_form = UserUpdateForm(request.POST, instance=request.user)
      profile_form = UserProfileForm(
          request.POST, request.FILES, instance=request.user.profile)
      if user_form.is_valid() and profile_form.is_valid():
          user = user_form.save(commit=False)
          user.profile = profile
          user.profile = request.user.profile
          user.save()

          prof = profile_form.save(commit=False)
          prof.profile = profile
          prof.profile = request.user.profile
          prof.save()

          return HttpResponseRedirect(request.path_info)
   else:
      user_form = UserUpdateForm(instance=request.user)
      profile_form = UserProfileForm(instance=request.user.profile)
   params = {
       'user_form': user_form,
       'profile_form': profile_form,
 
   }
   return render(request , 'expense/profile.html', params)


@login_required
def welcome(request):
   users = User.objects.exclude(id=request.user.id)
   profiles = Profile.objects.all()
   current_user = request.user
   expenses = Expense.objects.filter(user=current_user)
   user_expense = Expense.objects.filter(add_money='Expense',user=current_user)
   user_income = Expense.objects.filter(add_money='Income',user=current_user)
   if(user_expense.count()>0):
	
        expense_sum = user_expense.aggregate(Sum('quantity')).get('quantity__sum')
        currencyExpense = "KSH {:,.2f}".format(expense_sum)

   else:
       expense_sum=0
       currencyExpense = "KSH {}".format(expense_sum)

   if(user_income.count() > 0):

        income_sum = user_income.aggregate(Sum('quantity')).get('quantity__sum')
        currencyIncome = "KSH {:,.2f}".format(income_sum)

   else:
       income_sum = 0
       currencyIncome = "KSH {}".format(income_sum)


   form = UpdateExpenseForm(request.POST)

  

 

   params = {
       'users': users,
       'profiles': profiles,
       'expenses':expenses,
       'form':form,
       'currencyIncome': currencyIncome,
       'currencyExpense': currencyExpense,
      
   }
   return render(request, 'expense/index.html', params)

@login_required
def addmoney_submission(request):
    current_user = request.user
    expenses = Expense.objects.filter(user=current_user)
    user_expense = Expense.objects.filter(add_money='Expense', user=current_user)
    user_income = Expense.objects.filter(add_money='Income',user=current_user)
    if(user_expense.count()>0):
        
        expense_sum = user_expense.aggregate(Sum('quantity')).get('quantity__sum')
        currencyExpense = "KSH {:,.2f}".format(expense_sum)

    else:
        expense_sum=0
        currencyExpense = "KSH {}".format(expense_sum)

    if(user_income.count() > 0):

        income_sum = user_income.aggregate(Sum('quantity')).get('quantity__sum')
        currencyIncome = "KSH {:,.2f}".format(income_sum)

    else:
        income_sum = 0
        currencyIncome = "KSH {}".format(income_sum)

    totalusage = income_sum - expense_sum
    currencyUsage = "KSH {}".format(totalusage)




    if request.method == 'POST':
        form = UpdateExpenseForm(request.POST)
        if form.is_valid():
           expense = form.save(commit=False)
           expense.user = request.user
           expense.save()
           return redirect('addmoney_submission')
    else:
        form = UpdateExpenseForm()
    params ={
        'expenses':expenses,
        'form':form,
        'currencyIncome': currencyIncome,
        'currencyExpense': currencyExpense,
        'currencyUsage': currencyUsage,
    }
    return render(request, 'expense/expense.html', params)


def edit_submission(request, id):
    if request.method == "POST":
        add = Expense.objects.get(id=id)

        form = UpdateExpenseForm(request.POST, instance=add)
        if form.is_valid():
            add = Expense.objects.get(id=id)

            expense = form.save(commit=False)
            expense.user = request.user

            expense.save()
        
        return redirect("welcome")
    else:
        form = UpdateExpenseForm()
    return render (request,'expense/expense.html', {'form':form})


def submission_detail(request, id):
    expenses = Expense.objects.get(id=id)

   

    params = {
        'expenses':expenses,
       
    }
    return render(request, 'expense/details.html', params)


def submission_delete(request, id):
    expenses = Expense.objects.get(id=id)
    if request.method == "POST":
        expenses.delete()
        return redirect('addmoney_submission')
        
    return redirect('addmoney_submission')


@login_required
def search_project(request):
       if 'search_project' in request.GET and request.GET["search_project"]:
         Category = request.GET.get("search_project")

 
         searched_projects = Expense.search_expense(Category).filter(user=request.user)
         message = f"{Category}"
         return render(request, 'expense/search_results.html', {'message':message,'results': searched_projects})
       else:
        message = "You haven't searched for any Expense"
       return render(request, 'expense/search_results.html', {'message': message})


class EditorChartView(TemplateView):
    template_name = 'expense/pie_chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Expense.objects.filter(user=self.user, add_money='Expense')
        return context

def pie_chartExpense(request):
    labels = []
    data = []

    queryset = Expense.objects.filter(user = request.user, add_money='Expense')
    expense_sum = queryset.aggregate(Sum('quantity')).get('quantity__sum')

    for expense in queryset:
        labels.append(expense.add_money)
        data.append(expense_sum)

    return render(request, 'expense/pie_chart.html', {
        'labels': labels,
        'data': data,
    })
    
def pie_chartIncome(request):
    labels1 = []
    data1 = []

    queryset = Expense.objects.filter(add_money='Income')
    for expense in queryset:
        labels1.append(expense.Category.name)
        data1.append(expense.quantity)

    return render(request, 'expense/index.html', {
        'labels1': labels1,
        'data1': data1,
    })
