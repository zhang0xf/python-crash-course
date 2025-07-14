from django import forms
from .models import Topic,Entry

# 表单的操作流程与模块(models.py)相似
# 让用户输入并提交信息的页面都是表单，哪怕它看起来不像表单
# Django中，创建表单的最简单方式是使用ModelForm
class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text':''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text':''}
        widgets = {'text':forms.Textarea(attrs={'cols':80})}