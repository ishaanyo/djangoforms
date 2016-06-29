from django.contrib import admin
from .models import Accounts,CustomForm,Question,QuestionAnswer,Createlink,Options,StandardField,Snippet,Album,Track
from rest_framework.authtoken.admin import TokenAdmin



# Register your models here.


admin.site.register(Accounts)
admin.site.register(CustomForm)
admin.site.register(Question)
admin.site.register(QuestionAnswer)
admin.site.register(Createlink)
admin.site.register(StandardField)
admin.site.register(Options)
admin.site.register(Snippet)
admin.site.register(Album)
admin.site.register(Track)
TokenAdmin.raw_id_fields = ('user',)



