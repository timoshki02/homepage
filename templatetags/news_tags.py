from django import template
from django.db.models import Count

register = template.Library()

from ..models import NewsPost


@register.inclusion_tag('home/tags/latest_news.html')
def show_latest_news(count=3):
	latest_news = NewsPost.published.order_by('-publish')[:count]
	return {'latest_news':latest_news}


