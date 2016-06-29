from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginForm,SignupForm
from .models import Accounts,CustomForm,StandardField,QuestionAnswer,Question,Options, Album
from django.db.models import Q
from .forms import AssignMangerForm,InputForm1
from datetime import datetime
from django.core import serializers
from django.http import HttpResponse
from rest_framework import generics
from .permissions import IsOwnerOrReadOnly
from .serializers import QuestionSerializer,CustomFormSerializer,QuestionAnswerSerializer
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import renderers
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here



# POST request to send answer to the questions
class QusetionAnswerList(generics.ListCreateAPIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = QuestionAnswer.objects.all()
    serializer_class = QuestionAnswerSerializer


# GET api for fetching forms to be displayed on web and android
class CustomFormDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomForm.objects.all()
    serializer_class = CustomFormSerializer


# create form to create form - perfect status or remove type_pattern
def makeform(request):

    if 'auth' in request.session:
        if request.method == 'POST':
            account = get_object_or_404(Accounts, pk = request.session['id'])  # remove this

            form_name = request.POST['fname']  # form name must be unique

            # we get the data now we have to save
            #a = request.POST.getlist('mytext[]')
            b = request.POST.getlist('choice[]')
            c = request.POST.getlist('type[]')

            lst_types = ''
            for z in range(len(c)):
                if z == len(c)-1:
                    lst_types += c[z]
                else:
                    lst_types += c[z] + ','

            html = ''
            lst = lst_types.split(',')

            # form create validation
            if len(c) > 0:
                for i in range(len(c)):
                    #html += lst[i] + ' '
                    #return HttpResponse(lst)
                    if c[i] == '3' or c[i] == '4' or c[i] == '6' or c[i] == '12':
                        try:
                            if c[i+1] == '9':
                                pass

                            else:
                                return HttpResponse('Options must be placed after single, multiple and dropdown')
                        except:
                            return HttpResponse('Error you didt give any choices')

                    elif c[i] == '9':
                        try:
                            if c[i-1] == '3' or c[i-1] == '4' or c[i-1] == '6' or c[i-1] == '9' or c[i-1] == '12':
                                pass
                            else:
                                return HttpResponse('Either single, multiple or dropdown should be placed before options')

                        except:
                            return HttpResponse('options cant be first choice, please select either single,multiple or dropdown before options')


                        #if lst[i-1] == 3 or lst[i-1] == 4 or lst[i-1] == 6:
                        #    pass
                        #else:
                        #    return HttpResponse('Please select Options after radio, multiple or dropdown')

            # create new form
            # first save question in form_id

            customform = account.customform_set.create(form_title = form_name, type_pattern = lst_types)    # returns the customform object just created
            pk = customform.pk

            if len(b) > 0:
                lst = []
                choice = customform.question_set.all()
                for inn in range(len(b)):
                    # 1 = short answer type
                    if c[inn] == '1':
                        choice = customform.question_set.create(question_text = b[inn], ftype = StandardField.objects.get(pk=1))
                        lst.append(choice)

                    #textarea
                    elif c[inn] == '2':
                        choice = customform.question_set.create(question_text=b[inn], ftype = StandardField.objects.get(pk=2))
                        lst.append(choice)

                    # radio - options
                    elif c[inn] == '3':
                        choice = customform.question_set.create(question_text=b[inn], ftype = StandardField.objects.get(pk=3))
                        lst.append(choice)

                    # multiple - options
                    elif c[inn] == '4':
                        choice = customform.question_set.create(question_text=b[inn], ftype = StandardField.objects.get(pk=4))
                        lst.append(choice)

                    # checkbox
                    elif c[inn] == '5':
                        choice = customform.question_set.create(question_text=b[inn], ftype = StandardField.objects.get(pk=5))
                        lst.append(choice)

                    # dropdown or select in HTML - options
                    elif c[inn] == '6':
                        choice = customform.question_set.create(question_text=b[inn], ftype = StandardField.objects.get(pk=6))
                        lst.append(choice)

                    # date
                    elif c[inn] == '7':
                        choice = customform.question_set.create(question_text=b[inn], ftype = StandardField.objects.get(pk=7))
                        lst.append(choice)

                    #time
                    elif c[inn] == '8':
                        choice = customform.question_set.create(question_text=b[inn], ftype = StandardField.objects.get(pk=8))
                        lst.append(choice)

                    # Email
                    elif c[inn] == '10':
                        choice = customform.question_set.create(question_text=b[inn],ftype=StandardField.objects.get(pk=10))
                        lst.append(choice)

                    # Integer
                    elif c[inn] == '11':
                        choice = customform.question_set.create(question_text=b[inn],ftype=StandardField.objects.get(pk=11))
                        lst.append(choice)

                    # multiple Checkbox - options
                    elif c[inn] == '12':
                        choice = customform.question_set.create(question_text=b[inn], ftype=StandardField.objects.get(pk=12))
                        lst.append(choice)

                    #options
                    elif c[inn] == '9':
                        last_choice = lst[-1]
                        type_of_option = last_choice.ftype
                        last_choice.options_set.create(option_text = b[inn], stype = type_of_option)



            # Form and its questions saved
            return HttpResponse('Saved Success ' + ' link = ' +'../new_form/' +str(pk)+'/' )

        return render(request, 'form/new_form.html' )

    return HttpResponse('please Login')




# display dynamic form - perfect status
def display_form_view1(request, form_id):
    if 'auth' in request.session:
        if request.method == 'POST':

            id = request.session['id']

            customform = CustomForm.objects.get(pk=form_id)
            form_name = customform.form_title
            form = InputForm1(request.POST, formid = form_id)
            count = 0

            html = ''

            lst_mulptiple_choices_answer = []

            if form.is_valid():
                for k,v in form.cleaned_data.items():
                    html += ' key = ' + k + 'value = ' + str(v) +'<br>'
                    count = count + 1

                account = Accounts.objects.get(pk = id)
                adatetime = datetime.now()

                for x in range(count):
                    if type(form.cleaned_data['choice_value_{no}'.format(no = x)]) == list:
                        for i in range(len(form.cleaned_data['choice_value_{no}'.format(no = x)])):
                            customform.question_set.all()[x].questionanswer_set.create(question_answer=form.cleaned_data['choice_value_{no}'.format(no=x)][i], timestamp=adatetime, userid=account)
                    else:
                        customform.question_set.all()[x].questionanswer_set.create(question_answer=form.cleaned_data['choice_value_{no}'.format(no = x)], timestamp = adatetime, userid = account)

                return HttpResponse('Thanks for response')

            else:
                return render(request, 'form/form.html', {'form': form, 'form_name': form_name})
                #return HttpResponse('Invalid Error')

        form1 = get_object_or_404(CustomForm, pk=form_id)
        form_name = form1.form_title
        form = InputForm1(formid = form1.pk)
        return render(request, 'form/testform.html', {'form': form, 'form_name': form_name})
    return HttpResponse('please login')


def index(request):
    return render(request, 'form/index.html')

# Show all responses - perfect status
def show(request):
    if 'auth' in request.session:
        id = request.session['id']
        account = Accounts.objects.get(pk = id)
        html = ''
        customform = account.customform_set.all()
        n = len(customform)
        if n > 0:
            for i in range(n):
                if n > 0:                              # customform exists
                    for x in range(len(customform)):                       # customform loop all forms
                        html += '<h2>' + customform[x].form_title + '</h2>'

                        if len(customform[x].question_set.all()) > 0:  # question exists
                            html += '<h3>Questions</h3>'
                            #if len(customform[x].question_set.all()[x].questionanswer_set.all()) > 0:
                            for y in range(len(customform[x].question_set.all())):
                                html += '<br><strong>' + customform[x].question_set.all()[y].question_text + '</strong><br>'
                                for inner in range(len(customform[x].question_set.all()[y].questionanswer_set.all())):
                                    html += '<br>Answers are = ' + customform[x].question_set.all()[y].questionanswer_set.all()[inner].question_answer
                            #html += customform[x].question_set.all()[y].question_answer

        return HttpResponse(html)
    return HttpResponse('please login')


def mypage(request):

    if 'auth' in request.session:
        auth = True
        id = request.session['id']
        account = Accounts.objects.get(pk=id)
        return HttpResponse('You are login and session id = ' + str(id) +'<br>Accounts object= '+ str(account))
        # redirect new form

    else:
        return HttpResponse('Unathorized Access, please login to view this page')

def login_new(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            emailc = form.cleaned_data['email']
            passwordc = form.cleaned_data['password']

            try:
                account = Accounts.objects.get(Q(email=emailc), Q(password=passwordc))
                id = account.pk
                request.session['id'] = id
                request.session['auth'] = 'yes'
                check = True

            except:
                check = False

            if check:
                return HttpResponseRedirect('../mypage/')
                # login sucess
            else:

                return HttpResponse('Login Failed, either email or password is incorrect')


    form = LoginForm()
    return render(request, 'form/login.html', {'form': form} )

# Register Accounts

def signup_form(request):

    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES or None)

        if form.is_valid():
            form.save(commit=False)
            email = form.cleaned_data['email']
            account = Accounts.objects.filter(email=email)
            try:
                account = account[0]
                if account.email == email:
                    return HttpResponse('email Adready exits please Login')
            except:
                pass

            # Create New accounts
            # Saving form in Accounts models
            form.save()
            # Get session id
            account = Accounts.objects.get(email=email)
            id = account.pk
            request.session['id'] = id
            request.session['auth'] = 'yes'
            # Account Created

            # redirecting to mypage
            return HttpResponseRedirect('../mypage/')

            # Checking name value pairs in response

        else:
            return render(request, 'form/login_form.html', {'form': form, 'name':'Register Agents'})

    form = SignupForm()
    return render(request, 'form/login_form.html', {'form': form, 'name':'Register Patient'})




# logout

def logout_user(request):
    if('auth' in request.session):
        del request.session['auth']
        del request.session['id']
        return HttpResponse('Successfully logout')
    else:
        return HttpResponse('Invalid Request, please login first')






















# Example 3
'''
def create_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            do_something_with(form.cleaned_data)
            return redirect("create_user_success")
    else:
        form = UserCreationForm()

    return render_to_response("signup/form.html", {'form': form})

def display_form_view2(request):
    form_field = {}
    form_field['name'] = 'ishaan'
    form_field['label'] = 'what is your name'
    form_field['type'] = 'charcter'
    lst = ['name', 'what is your name', 'integer']
    form = InputForm2( fields = form_field )
    return render(request, 'form/form.html', {'form': form})


# Exmaple 2

def display_form_view1(request):
    label = 'what is your name'
    value_type = 'csvnnj'
    form = InputForm1(label=label, value_type=value_type)
    return render(request, 'form/form.html', {'form': form})
'''