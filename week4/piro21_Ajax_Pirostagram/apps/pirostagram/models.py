# from django.db import models

# class Post(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='posts/')
#     caption = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     likes = models.ManyToManyField(User, related_name='post_likes', blank=True)

#     def __str__(self):
#         return self.caption

# class Comment(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     text = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.text