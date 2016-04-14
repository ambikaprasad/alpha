from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from datetime import datetime
Questype=((1,'MCQ Single Correct'),(2,'MCQ multiple correct'),(3,'Group MCQ single correct'),(4,'True and false'),
(5,'Integer Type'),(6,'Matrix match'),(7,'Linked questions'),(8,'Assertion and Reasons type'),(9,'Subjective or descriptive type'),
(10,'Group (Common data) Subjective or descriptive type'))

class Category(models.Model):
    name= models.CharField(max_length=255)
    description= models.TextField(null=True,blank=True)
    slug=models.SlugField(max_length=150,unique=True)
    active=models.BooleanField(default=False)
    created_date=models.DateTimeField(auto_now_add=True)
    modified_date=models.DateTimeField(auto_now=True)
    added_by=models.ForeignKey(User)
    def __unicode__(self):
        return self.tag_name
    def save(self, *args, **kwargs):
        if self.slug is None or self.slug == '':
            self.slug=slugify(self.name)
        super(Category, self).save(*args, **kwargs)

class Tag(models.Model):
    name= models.CharField(max_length=255)
    description= models.TextField(null=True,blank=True)
    slug=models.SlugField(max_length=150,unique=True)
    active=models.BooleanField(default=False)
    created_date=models.DateTimeField(auto_now_add=True)
    modified_date=models.DateTimeField(auto_now=True)
    added_by=models.ForeignKey(User)
    def __unicode__(self):
        return self.tag_name
    def save(self, *args, **kwargs):
        if self.slug is None or self.slug == '':
            self.slug=slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

class QuestionManager(models.Model):
  Questype = models.IntegerField(max_length=2,choices=Questype, default=1)
  Question =  models.TextField()
  ParentQuestion = models.ForeignKey("self",null=True,blank=True)
  category = models.ManyToManyField(Category)
  Tag = models.ManyToManyField(Tag)
  added_date = models.DateTimeField(auto_now_add=True)
  added_by = models.ForeignKey(User)
  status = models.BooleanField(default=False)
  correct_answer = models.TextField()
  explanation=models.TextField(null=True,blank=True)
  taguser= models.ManyToManyField(User)

class Option(models.Model):
  question= models.ForeignKey(QuestionManager)
  option= models.TextField()





