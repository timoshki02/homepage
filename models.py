from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

# Create your models here.
class publishedmanager(models.Manager):
	def get_queryset(self):
		return super(publishedmanager,
			         self).get_queryset()\
		                  .filter(status = 'published')

class NewsPost(models.Model):

	STATUS_CHOICES = (
		('draft','Draft'),
		('published','Published')
	)

	image = models.ImageField(upload_to = "%y/%m/%d/news")
	title = models.CharField(max_length = 250)
	body = models.TextField()
	publish = models.DateTimeField(default = timezone.now)
	created = models.DateTimeField(auto_now_add = True,auto_now = False)
	updated = models.DateTimeField(auto_now_add = False,auto_now = True)
	slug = models.SlugField(max_length = 250,unique_for_date = 'publish')
	status = models.CharField(max_length = 10,choices = STATUS_CHOICES,default = 'draft')
	objects = models.Manager()
	published = publishedmanager()

	class Meta:
		ordering = ('-publish',)


	def __str__(self):
		return self.title


	def get_absolute_url(self):
		return reverse('detail',
						args = [self.publish.year,
						        self.publish.strftime('%m'),
						        self.publish.strftime('%d'),
						        self.slug])


class Comment(models.Model):
	post = models.ForeignKey(NewsPost, related_name = 'comments')
	name = models.CharField(max_length = 85)
	email = models.EmailField()
	body = models.TextField()
	created = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
	active = models.BooleanField(default = True)

	class Meta:
		ordering = ('created',)


	def __str__(self):
		return 'comment by {} on {}'.format(self.name,self.post)
