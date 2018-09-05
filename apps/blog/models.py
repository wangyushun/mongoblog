from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.


class Category(models.Model):
    '''
    分类模型
    '''
    name = models.CharField(max_length=20, verbose_name='类型名')

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'<Category: {self.name}>'


    class Meta:
        verbose_name = '类型'
        verbose_name_plural = verbose_name



class Blog(models.Model):
    '''
    博客模型
    '''
    title = models.CharField(max_length=200, verbose_name='标题')
    author = models.CharField(max_length=200, verbose_name='作者')
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE, verbose_name='类型')
    content = models.TextField(verbose_name='内容')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')

    def __str__(self):
        return f'<Blog: {self.title}>'


    class Meta:
        ordering = ['-add_time']
        verbose_name = '博客'
        verbose_name_plural = verbose_name


       

