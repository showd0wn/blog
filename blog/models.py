from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    # 类别名称
    name = models.CharField(max_length=10, unique=True)


class Tag(models.Model):
    # 标签名称
    name = models.CharField(max_length=10, unique=True)


class Article(models.Model):
    # 文章标题
    title = models.CharField(max_length=60)
    # 文章摘要
    abstract = models.CharField(max_length=200, blank=True)
    # 文章正文
    body = models.TextField()
    # 文章的创建时间
    created_time = models.DateTimeField()
    # 文章的最后一次修改时间
    modified_time = models.DateTimeField()
    # 文章作者
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # 文章类别
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # 文章标签
    tags = models.ManyToManyField(Tag, blank=True)
    # 文章浏览量
    views = models.PositiveIntegerField(default=0)
