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
    # 文章阅读量
    views = models.PositiveIntegerField(default=0)


class Menu(models.Model):
    title = models.CharField('标题', max_length=10, unique=True)
    href = models.CharField('地址', max_length=60)
    order = models.IntegerField('顺序')

    class Meta:
        ordering = ['order']
        verbose_name = '菜单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Link(models.Model):
    title = models.CharField('标题', max_length=10, unique=True)
    href = models.CharField('地址', max_length=60)
    icon = models.CharField('图标', max_length=60)
    order = models.IntegerField('顺序')

    class Meta:
        ordering = ['order']
        verbose_name = '链接'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
