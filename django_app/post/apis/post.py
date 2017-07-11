from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from post.models import Comment
from post.models import Post
from post.serializers import PostSerializer

__all__ = (
    'PostListCreateView',
)


class PostListCreateView(APIView):
    # get 요청이 왔을 때, Post.objects.all()을
    # PostSerializer를 통해 Response로 반환
    # DRF API Guide
    #   - API View
    #   - Serializers
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            # serializer.save()로 생성된 Post Instance를 instance 변수에 할당
            instance = serializer.save(author=request.user)
            # comment_content에 request.data의 'comment'에 해당하는 값을 할당
            comment_content = request.data.get('comment')
            if comment_content:
                instance.my_comment = Comment.objects.create(
                    post=instance,
                    author=instance.author,
                    content=comment_content
                )
                instance.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
