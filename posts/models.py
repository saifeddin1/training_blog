from django.db import models
from django.conf import settings
from django.utils import timezone




class TimespamtedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True


class Post(TimespamtedModel):
    user         = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    title        = models.CharField(max_length=120)                  
    content      = models.TextField()
  
    draft = models.BooleanField(default=False)
    # slug = models.SlugField(unique=True)
    # image = models.ImageField(upload_to=upload_location,
    #                         null=True, 
    #                         blank=True,)


    def __str__(self):
        return self.title


class Comment(TimespamtedModel):
    commented_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    name = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    # email = models.EmailField(max_length=254)
    body  = models.TextField()


    def __str__(self):
        return f'comment {self.id} by {self.name}' 
        












    # def save(self, *args, **kwargs):
    # 	if not self.id:
    # 		created_at = timezone.now()
    # 	updated = timezone.now()
    # 	return super(Post, self).save(*args, **kwargs)

















# def create_slug(instance, new_slug=None):
#     slug = slugify(instance.title)
#     if new_slug is not None:
#         slug = new_slug
#     qs = Post.objects.filter(slug=slug).order_by("-id")
#     exists = qs.exists()
#     if exists:
#         new_slug = "%s-%s" %(slug, qs.first().id)
#         return create_slug(instance, new_slug=new_slug)
#     return slug