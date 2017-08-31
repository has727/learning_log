from django.shortcuts import render, redirect
from .models import Topic, Entry
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.core.urlresolvers import reverse
from learning_logs.forms import TopicForm, EntryForm

# Create your views here.


# def index(request):
#     return render(request, 'learning_logs/index.html')
    
    
def topics(request):
    template = get_template('learning_logs/topics.html')
    topics = Topic.objects.all().order_by('date_added')
    # context = {'topics': topics}
    # return render(request, 'learning_logs/topics.html', context)
    html = template.render(locals())
    return HttpResponse(html)
    
def topic(request, topic_id):
    template = get_template('learning_logs/topic.html')
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    # context = {'topic': topic, 'entries': entries}
    # return render(request, 'learning_logs/topic.html', context)
    html = template.render(locals())
    return HttpResponse(html)


def index(request):
    template = get_template('learning_logs/index.html')
    now = datetime.now
    usrtotal = ['A','B','C','D']
    userlists = list()
    for usr in usrtotal:
        userlists.append({'name': usr})
  
    html = template.render(locals())
    return HttpResponse(html)


def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))
        
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


def new_entry(request, topic_id):
    template = get_template('learning_logs/new_entry.html')
    topic = Topic.objects.get(id=topic_id)
    
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))
    
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)