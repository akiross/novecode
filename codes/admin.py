from django.contrib import admin

from .models import Snippet, Source, SnippetSource, Exercise, Answer, IOTest

admin.site.register(Snippet)
admin.site.register(Source)
admin.site.register(SnippetSource)
admin.site.register(Exercise)
admin.site.register(Answer)
admin.site.register(IOTest)
