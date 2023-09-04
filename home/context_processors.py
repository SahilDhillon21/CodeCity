from .models import Profile

def profile_details(request):
    if request.user.is_authenticated:
        try:
            user_profile = Profile.objects.get(user=request.user)
            return {'user_profile':user_profile}
        except:
            pass
    return {}