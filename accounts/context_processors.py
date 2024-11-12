# accounts/context_processors.py
from .models import UserProfile

def user_profile_image(request):
    if request.user.is_authenticated:
        userprofile = UserProfile.objects.filter(user=request.user).first()
        if userprofile:
            return {'userprofile_image': userprofile.profile_image}
    return {'userprofile_image': None}
