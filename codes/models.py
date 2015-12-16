from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

def get_sentinel_user():
	return get_user_model().objects.get_or_create(username='deleted')[0]

class Snippet(models.Model):
	ACC_HIDDEN = 1
	ACC_READABLE = 2
	ACC_WRITABLE = 3
	ACCESS_CHOICES = (
		(ACC_HIDDEN, "Hidden"),
		(ACC_READABLE, "Readable"),
		(ACC_WRITABLE, "Writable"),
	)

	code_text = models.TextField()
	access_flag = models.IntegerField(choices=ACCESS_CHOICES)

	def __str__(self):
		return '[{}] '.format(self.ACCESS_CHOICES[self.access_flag - 1][1][0]) + self.code_text.strip()[:100]

class Source(models.Model):
	filename = models.CharField(max_length=128)
	date = models.DateTimeField('creation date')
	# When the author of a source is removed, the source remains
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET(get_sentinel_user))
	# Each source contains many snippets, and each snippet can be in many sources
	snippets = models.ManyToManyField(Snippet, through='SnippetSource')

	def __str__(self):
		return self.filename

class SnippetSource(models.Model):
	snippet = models.ForeignKey(Snippet)
	source = models.ForeignKey(Source)
	number = models.PositiveIntegerField()

	def __str__(self):
		return self.source.filename + " - " + str(self.snippet)

	class Meta:
		ordering = ('number',)

class Exercise(models.Model):
	title = models.CharField(max_length=100, unique=True)
	description = models.TextField(unique=True)
	# When author is removed, the exercise remains
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET(get_sentinel_user))
	score = models.IntegerField()
	# Each exercise may have multiple sources, each of which can be in each exercise
	sources = models.ManyToManyField(Source)

	def __str__(self):
		return self.title

# When an answer is removed, all the related sources should be removed, too
# and all the snippets in those sources which are writable shall be also removed
class Answer(models.Model):
	# When an exercise is removed, also answers are removed
	exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
	# When author is removed, answers are removed, too
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	passes = models.BooleanField(default=False)
	# Each answer may have multiple sources
	sources = models.ManyToManyField(Source)

	def __str__(self):
		return "[Ans] " + str(self.exercise)

class IOTest(models.Model):
	# A name or description for this text
	description = models.CharField(max_length=200)
	# When an exercise is removed, there's no need for its tests
	exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
	# What goes in input to the program
	input_data = models.TextField()
	# What goes in output to the program
	output_data = models.TextField()

	def __str__(self):
		return self.description

