from django.contrib import admin

from .models import Snippet, Source, SnippetSource, Exercise, Answer, IOTest

class SnippetInLine(admin.TabularInline):
	model = SnippetSource
	extra = 2

class SourceAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ('filename', 'author', 'date')}),
	]
	inlines = [SnippetInLine]

admin.site.register(Snippet)
admin.site.register(Source, SourceAdmin)
admin.site.register(SnippetSource)
admin.site.register(Exercise)
admin.site.register(Answer)
admin.site.register(IOTest)
