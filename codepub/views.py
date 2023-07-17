from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from home.models import Profile
from codepub.models import Post
# Create your views here.

# @login_required(login_url='login')
def codepubHome(request):
    # For processing post data
    if request.method == 'POST':
        user = request.user
        title = request.POST['title-input']
        caption = request.POST['caption-input']
        image = request.FILES.get('image-input',None)

        new_post = Post.objects.create(title=title, user = user, image = image, caption = caption,likes=0)
        new_post.save()

        messages.info(request,"Post created successfully")

    allPosts = Post.objects.all()
    context = {'allPosts':allPosts}
    
    return render(request,'codepub/codepubHome.html',context)

@login_required(login_url='login')
def profile(request):
    user_profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':

        image = request.FILES.get('image')

        if image is None:
            image = user_profile.profileimg
        


        bio = request.POST['input_bio'].strip()
        location = request.POST['location']

        user_profile.profileimg = image
        user_profile.bio = bio
        user_profile.location = location
        user_profile.save()
        messages.success(request,'Profile updated sucessfully!')
        

        return redirect(profile)

    context = {'user_profile':user_profile}
    return render (request,'codepub/profile.html',context)

