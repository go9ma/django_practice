from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    body = models.TextField()
    image = models.ImageField(upload_to='posts', null=True)
    # 1. MEDIA_ROOT/posts/이미지파일명 위치에 저장하겠다.
    # 2. 게시물을 작성할 댸 이미지를 반드시 넣지 않아도 된다.
    # *image변수에는 이미지파일이 통으로 들어가는것이 아니라, 이미지가 위치되어 있는 위치 및 경로를 저장하는것이다.
    created_at = models.DateTimeField()
    liked_users = models.ManyToManyField(User, related_name='liked_posts')

    def __str__(self):

        # return f'{self.user.get_username()}: {self.body}'
        if self.user:
            return f'{self.user.get_username()}: {self.body}'

        return f'{self.body}'
        # user 는 무조건 user.get_username()을 써서 값을 가져와야한다.
        # get_username = 함수

