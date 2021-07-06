from django.http import HttpResponseForbidden
from articleapp.models import Article

# accountapp : User 확인 (본인이 맞는지)
def article_ownership_required(func):
    def decorated(request, *args, **kwargs):
        article = Article.objects.get(pk=kwargs["pk"])
        if not article.writer == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)

    return decorated
