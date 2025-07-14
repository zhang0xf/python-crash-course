from django.db import models

# Create your models here.

# 模型告诉Django如何处理应用程序中存储的数据
# 要使用模型，必须让Django将应用程序包含到项目中,另见:settings.py

class Topic(models.Model): # 继承Model
    """用户学习的主题"""
    text = models.CharField(max_length=200) # 200告诉Django该在数据库中预留多少空间
    date_added = models.DateTimeField(auto_now_add=True) # auto_now_add=True:每当用户创建新主题时，这都让Django将这个属性自动设置成当前日期和时间
    
    # Django调用方法__str__()来显示模型的简单表示
    def __str__(self):
        """返回模型的字符串表示"""
        return self.text

class Entry(models.Model):
    """学到的有关某个主题的具体知识"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) # 外键
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    # Meta存储用于管理模型的额外信息
    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text[:50]+"..."