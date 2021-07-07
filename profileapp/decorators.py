from django.http import HttpResponseForbidden
from profileapp.models import Profile

# accountapp : User 확인 (본인이 맞는지)
def profile_ownership_required(func):
    def decorated(request, *args, **kwargs):
        profile = Profile.objects.get(pk=kwargs["pk"])
        if not profile.user == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)

    return decorated
