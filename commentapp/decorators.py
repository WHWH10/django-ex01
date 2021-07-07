from django.http import HttpResponseForbidden
from commentapp.models import Comment

# accountapp : User 확인 (본인이 맞는지)
def comment_ownership_required(func):
    def decorated(request, *args, **kwargs):
        comment = Comment.objects.get(pk=kwargs["pk"])
        if not comment.writer == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)

    return decorated
