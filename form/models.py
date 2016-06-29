from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

class Accounts(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=300)
    password = models.CharField(max_length=300)

    def __str__(self):
        return self.name + ' - ' + self.email


class CustomForm(models.Model):
    accounts = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    form_title = models.CharField(max_length= 300)         # 1 = Chacterfield, 2 = Choices
    type_pattern = models.CharField(max_length= 2000, default='')


    def __str__(self):
        return self.form_title


class Createlink(models.Model):
    customform = models.ForeignKey(CustomForm, on_delete=models.CASCADE)
    form_link = models.CharField(max_length= 2000, blank=True)


class StandardField(models.Model):
    field_type_id = models.IntegerField()
    field_type = models.CharField(max_length=300)

    def __str__(self):
        return self.field_type + ' - ' + str(self.field_type_id)

class Question(models.Model):
    customform = models.ForeignKey(CustomForm, on_delete=models.CASCADE, related_name='questions')
    ftype = models.ForeignKey(StandardField, on_delete=models.CASCADE, default='')
    question_text = models.CharField(max_length= 1000)


    def __str__(self):
        return self.question_text + ' ?'


class Options(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    option_text = models.CharField(max_length= 1000)
    stype = models.ForeignKey(StandardField, default='')

    def __str__(self):
        return self.option_text


class QuestionAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    question_answer = models.CharField(max_length=2000, null=False,blank=False)
    timestamp = models.DateTimeField(null= False,blank=False, default= datetime.now())
    userid = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
        return self.question_answer

LANGUAGE_CHOICES = [['python','python']]
STYLE_CHOICES = [['python','python'],['friendly','friendly']]

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    owner = models.ForeignKey('auth.User', related_name='snippets', default='')
    highlighted = models.TextField(default='')

    def __str__(self):
        return str(self.pk)

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        lexer = get_lexer_by_name(self.language)
        linenos = self.linenos and 'table' or False
        options = self.title and {'title': self.title} or {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)

    class Meta:
        ordering = ('created',)


class Album(models.Model):
    album_name = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)

    def __str__(self):
        return self.album_name

class Track(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='tracks')
    order = models.IntegerField()
    title = models.CharField(max_length=100)
    duration = models.IntegerField()

    class Meta:
        unique_together = ('album', 'order')
        ordering = ['order']

    def __str__(self):
        return self.title

    def __unicode__(self):
        return '%d: %s' % (self.order, self.title)


#  More types can be added by binding foriegn key on custom form









