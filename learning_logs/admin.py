from django.contrib import admin

# Register your models here.

from learning_logs.models import Topic, Entry

class adminTopic(admin.ModelAdmin):
	list_display = ('text', 'date_added')

admin.site.register(Topic, adminTopic)
admin.site.register(Entry)
