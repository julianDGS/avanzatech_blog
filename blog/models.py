from django.db import models

from user.models import User


class BaseAbstractModel(models.Model):
    
    class Meta:
        abstract = True

    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class BlogPost(BaseAbstractModel):
    
    title = models.CharField("title", max_length=250)
    content = models.TextField("content")
    content_html = models.TextField("Html Content")
    author = models.ForeignKey(User, verbose_name="Author", on_delete=models.DO_NOTHING)
    likes = models.ManyToManyField(User, verbose_name=("Likes"), related_name='liked_posts', through='Like')
    comments = models.ManyToManyField(User, verbose_name=("Comments"), related_name='commented_posts', through='Comment')

    @property
    def excerpt(self):
        return self.content_html[:200]

    class Meta:
        db_table = "blog_posts"
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"

    def __str__(self):
        return f'title: {self.title}, user: {self.author.email}'

class Like(BaseAbstractModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)

    class Meta:
        db_table = 'blog_post_likes'
        constraints = [
            models.UniqueConstraint(fields=['post', 'user'], name='unique_post_user')
        ]

    def __str__(self) -> str:
        return self.post.__str__()
    
class Comment(BaseAbstractModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    comment = models.TextField(("comment"))

    class Meta:
        db_table = 'blog_post_comments'

    def __str__(self) -> str:
        return f'{self.post.__str__()}, comment: {self.comment}'