from django.db import models
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.name


class Post(models.Model):

    STATUS = (
        ("draft", "Draft"),
        ("published", "Published"),
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    tags = models.ManyToManyField(Tag,max_length=200, blank=True)

    title = models.CharField(max_length=200)

    slug = models.SlugField(unique=True)

    content = models.TextField()

    image = models.ImageField(
        upload_to="posts/",
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default="draft"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"


    def __str__(self):
        return self.title



class Comment(models.Model):

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    comment = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"


    def __str__(self):
        return self.user.email



class Like(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE
    )


    class Meta:
        unique_together = ("user", "post")
        verbose_name = "Like"
        verbose_name_plural = "Likes"


    def __str__(self):
        return f"{self.user.email} liked {self.post.title}"