from django import forms
from .models import Accounts, CustomForm
from django.shortcuts import render,get_object_or_404


class InputForm1(forms.Form):
    def __init__(self, *args, **kwargs):
        form_id = kwargs.pop('formid')
        lst_options =[]        #lst_choice = kwargs.get('label2')
        super(InputForm1, self).__init__(*args, **kwargs)

        customform = get_object_or_404(CustomForm, pk=form_id)
        #customform = CustomForm.objects.get(pk=form_id)

        type_pattern = customform.type_pattern.split(',')   # obtain list of strings like ['1','3','9','9']

        if len(customform.question_set.all()) > 0:
            for i in range(len(customform.question_set.all())):
                if customform.question_set.all()[i].ftype.pk == 1:
                    self.fields['choice_value_{s}'.format(s=str(i))] = forms.CharField(max_length=1000, required=True,label=customform.question_set.all()[i].question_text)

                elif customform.question_set.all()[i].ftype.pk == 2:
                    self.fields['choice_value_{s}'.format(s=str(i))] = forms.CharField(max_length=1000,required=True, label=customform.question_set.all()[i].question_text, widget= forms.Textarea)


                elif customform.question_set.all()[i].ftype.pk == 3:
                    lst_options = []
                    label = customform.question_set.all()[i].question_text
                    options = customform.question_set.all()[i].options_set.all()
                    for x in range(len(options)):
                        lst_options += [[options[x].option_text, options[x].option_text]]

                    self.fields['choice_value_{s}'.format(s=str(i))] = forms.ChoiceField(choices=lst_options, widget=forms.RadioSelect, required=True, label = label)

                # multiple field create
                elif customform.question_set.all()[i].ftype.pk == 4:
                    lst_options = []
                    label = customform.question_set.all()[i].question_text
                    options = customform.question_set.all()[i].options_set.all()
                    for x in range(len(options)):
                        lst_options += [[options[x].option_text, options[x].option_text]]

                    self.fields['choice_value_{s}'.format(s=str(i))] = forms.MultipleChoiceField(choices=lst_options,required=True, label=label)

                # chechbox field create
                elif customform.question_set.all()[i].ftype.pk == 5:
                    label = customform.question_set.all()[i].question_text

                    self.fields['choice_value_{s}'.format(s=str(i))] = forms.BooleanField(required=False, label=label)

                # dropdown or select field create
                elif customform.question_set.all()[i].ftype.pk == 6:
                    lst_options = []
                    label = customform.question_set.all()[i].question_text
                    options = customform.question_set.all()[i].options_set.all()
                    for x in range(len(options)):
                        lst_options += [[options[x].option_text, options[x].option_text]]

                    self.fields['choice_value_{s}'.format(s=str(i))] = forms.ChoiceField(choices=lst_options, label=label)

                # date field create
                elif customform.question_set.all()[i].ftype.pk == 7:
                    label = customform.question_set.all()[i].question_text

                    self.fields['choice_value_{s}'.format(s=str(i))] = forms.DateField(required=True, widget=forms.TextInput(attrs={'class':'datepicker'}, label=label))

                # time field create
                elif customform.question_set.all()[i].ftype.pk == 8:
                    label = customform.question_set.all()[i].question_text

                    self.fields['choice_value_{s}'.format(s=str(i))] = forms.TimeField(required=True, label=label)

                # Email field create
                elif customform.question_set.all()[i].ftype.pk == 10:
                    label = customform.question_set.all()[i].question_text

                    self.fields['choice_value_{s}'.format(s=str(i))] = forms.EmailField(required=True, label=label)

                # Integer field create
                elif customform.question_set.all()[i].ftype.pk == 11:
                    label = customform.question_set.all()[i].question_text

                    self.fields['choice_value_{s}'.format(s=str(i))] = forms.IntegerField(required=True, label=label)

                # multiple CheckBox field create
                elif customform.question_set.all()[i].ftype.pk == 12:
                    lst_options = []
                    label = customform.question_set.all()[i].question_text
                    options = customform.question_set.all()[i].options_set.all()
                    for x in range(len(options)):
                        lst_options += [[options[x].option_text, options[x].option_text]]

                    self.fields['choice_value_{s}'.format(s=str(i))] = forms.MultipleChoiceField(choices=lst_options, widget=forms.CheckboxSelectMultiple(), required=True, label=label)


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Accounts
        fields = ['email', 'password']

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Accounts
        fields = ['name', 'email', 'password']


class AssignMangerForm(forms.Form):
    employee_id = forms.IntegerField(required=True)
    managers = forms.ChoiceField(choices= (('mr', 'Mister'), ('mrs', 'Miss') ), widget=forms.Select, required=True)


'''
class UserCreationForm(forms.Form):
    username = forms.CharField(max_length=30)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1", "")
        password2 = self.cleaned_data["password2"]
        if password1 != password2:
            raise forms.ValidationError("The two password fields didn't match.")
        return password2


class InputForm2(forms.Form):
    def __init__(self, *args, **kwargs):
        form_fields = kwargs.pop("fields", {})
        #n = kwargs.pop('n')
        #form_fields = kwargs.pop("fields")
        #form_fields = kwargs.pop("fields", {})
        #i =1
        super(InputForm2, self).__init__(*args, **kwargs)
        for field in form_fields:
        #while(i<=n):
            # Get the field attributes

            #field_name = field[0]
            #field_label = field[1]
            #field_type = field[2]

            field_name = field['name']
            field_label = field['label']
            field_type = field['type']

            # Create the form field
            if field_type == 'integer':
                self.fields[field_name] = forms.IntegerField(required=True, label=field_label)
            elif field_type == 'decimal':
                self.fields[field_name] = forms.DecimalField(decimal_places=4, max_digits=8, required=True,
                                                             label=field_label)
            else:
                self.fields[field_name] = forms.CharField(max_length=100, required=True, label=field_label)



class InputForm1(forms.Form):
    def __init__(self, *args, **kwargs):
        label = kwargs.pop("label")
        value_type = kwargs.pop("value_type")
        super(InputForm1, self).__init__(*args, **kwargs)
        if value_type == 'integer':
            self.fields['value'] = forms.IntegerField(required=True, label=label)
        elif value_type == 'decimal':
            self.fields['value'] = forms.DecimalField(decimal_places=4, max_digits=8, required=True, label=label)
        else:
            self.fields['value'] = forms.CharField(max_length=100, required=True, label=label)


'''