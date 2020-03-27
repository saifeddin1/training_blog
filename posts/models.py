from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    user       = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    title      = models.CharField(max_length=120)                  
    content      = models.TextField()
    created_at   = models.DateField(auto_now=False, auto_now_add=False, null=True)
    updated      = models.DateTimeField(auto_now=True, auto_now_add=False)
    # slug = models.SlugField(unique=True)
    # image = models.ImageField(upload_to=upload_location,
    #                         null=True, 
    #                         blank=True,)
    # draft = models.BooleanField(default=False)


    def save(self, *args, **kwargs):
    	if not self.id:
    		created_at = timezone.now()
    	updated = timezone.now()
    	return super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


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