from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from datetime import datetime
Questype=((1,'MCQ Single Correct'),(2,'MCQ multiple correct'),(3,'Group MCQ single correct'),(4,'True and false'),
(5,'Integer Type'),(6,'Matrix match'),(7,'Linked questions'),(8,'Assertion and Reasons type'),(9,'Subjective or descriptive type'),
(10,'Group (Common data) Subjective or descriptive type'))

class Tag(models.Model):
    name= models.CharField(max_length=255)
    description= models.TextField(null=True,blank=True)
    slug=models.SlugField(max_length=150,unique=True)
    active=models.BooleanField(default=False)
    is_category=models.BooleanField(default=False)
    created_date=models.DateTimeField(auto_now_add=True)
    modified_date=models.DateTimeField(auto_now=True)
    added_by=models.ForeignKey(User)
    def __unicode__(self):
        return self.name
    def save(self, *args, **kwargs):
        if self.slug is None or self.slug == '':
            self.slug=slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

class QuestionManager(models.Model):
  questype = models.IntegerField(max_length=2,choices=Questype, default=1)
  question =  models.TextField(unique=True)
  parentquestion = models.ForeignKey("self",null=True,blank=True)
  category = models.ManyToManyField(Tag,limit_choices_to={'is_category': True})
  tag = models.ManyToManyField(Tag,limit_choices_to={'is_category': False})
  status = models.BooleanField(default=False)
  correct_answer = models.TextField()
  explanation=models.TextField(null=True,blank=True)
  user= models.ManyToManyField(User)
  added_date = models.DateTimeField(auto_now_add=True)
  added_by = models.ForeignKey(User)
  default_marks=models.IntegerField(default=1)
  random_option=models.BooleanField(default=False)
  slug=models.TextField(unique=True)
  def __unicode__(self):
        return self.question
  def save(self, *args, **kwargs):
        if self.slug is None or self.slug == '':
            self.slug=slugify(self.name)
        super(QuestionManager, self).save(*args, **kwargs)

class Option(models.Model):
  question= models.ForeignKey(QuestionManager)
  option= models.TextField()
  active=models.BooleanField(default=True)





