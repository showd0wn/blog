from django.views import generic
from .models import Article, Menu, Link


class IndexView(generic.ListView):
    model = Article
    template_name = 'blog/index.html'
    context_object_name = "article_list"

    def get_context_data(self, **kwargs):
        # 获取菜单列表
        kwargs['menu_list'] = Menu.objects.all().order_by('order')
        # 获取链接列表
        kwargs['link_list'] = Link.objects.all().order_by('order')

        return super(IndexView, self).get_context_data(**kwargs)
