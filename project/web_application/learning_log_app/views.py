from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Topic
from .models import Entry
from .forms import TopicForm
from .forms import EntryForm

# Create your views here.
def index(request):
    """学习笔记的主页"""
    return render(request,'learning_log_app/index.html')

def topics(request):
    """显示所有的主题"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}
    return render(request,'learning_log_app/topics.html',context)

def topic(request,topic_id):
    """显示单个主题及其所有的条目"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic,'entries':entries}
    return render(request,'learning_log_app/topic.html',context)

# 函数new_topic()将请求对象作为参数
def new_topic(request):
    """添加新主题"""
    # 用户初次请求该网页时，其浏览器将发送GET请求；用户填写并提交表单时，其浏览器将发送POST请求。
    if request.method != 'POST':
        # 未提交数据：创建一个新表单
        form = TopicForm()
    else:
        # POST提交的数据,对数据进行处理
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save() # 将表单中的数据写入数据库
            # 用户提交主题后我们将用户重定向到网页topics
            # 函数reverse()根据指定的URL模型确定URL，这意味着Django将在页面被请求时生成URL
            return HttpResponseRedirect(reverse('learning_log_app:topics')) 
    context = {'form':form}
    return render(request,'learning_log_app/new_topic.html',context) # 通过"上下文字典"将表单发送给模板

def new_entry(request,topic_id):
    """在特定的主题中添加新条目"""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        # 未提交数据,创建一个空表单
        form = EntryForm()
    else:
        # POST提交的数据,对数据进行处理
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_log_app:topic',args=[topic_id]))
    context = {'topic':topic,'form':form}
    return render(request,'learning_log_app/new_entry.html',context)

def edit_entry(request,entry_id):
    """编辑既有条目"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if request.method != 'POST':
        # 初次请求，使用当前条目填充表单￼
       form = EntryForm(instance=entry)
    else:
        # POST提交的数据，对数据进行处理
        form = EntryForm(instance=entry,data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_log_app:topic',args=[topic.id]))
    context = {'entry':entry,'topic':topic,'form':form}
    return render(request,'learning_log_app/edit_entry.html',context)