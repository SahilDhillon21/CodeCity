from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from home.models import Profile
from codepub.models import Post, LikePost, FollowAccount
# Create your views here.

# @login_required(login_url='login')
def codepubHome(request):
    # For processing post data
    if request.method == 'POST':
        user = request.user.username
        title = request.POST['title-input']
        caption = request.POST['caption-input']
        image = request.FILES.get('image-input')

        new_post = Post.objects.create(title=title,user=user, image = image, caption = caption)
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

@login_required(login_url='login')
def like_post(request):
    username = request.user.username
    post_id = request.GET.get('post_id')

    post = Post.objects.get(id=post_id)

    like_filter = LikePost.objects.filter(post_id=post_id, username=username).first()

    if like_filter == None:
        new_like = LikePost.objects.create(post_id=post_id,username=username)
        new_like.save()
        post.likes = post.likes+1
        post.save()
        return redirect(codepubHome)
    else:
        like_filter.delete()
        post.likes = post.likes-1
        post.save()
        return redirect(codepubHome)

@login_required(login_url='login')
def view_profile(request,pk):
    viewed_user_object = User.objects.get(username=pk)
    viewed_user_profile = Profile.objects.get(user=viewed_user_object)
    viewed_user_posts = Post.objects.filter(user=pk)
    viewed_user_posts_length = len(viewed_user_posts)

    context = {
        'viewed_user_object':viewed_user_object,
        'viewed_user_profile':viewed_user_profile,
        'viewed_user_posts':viewed_user_posts,
        'viewed_user_posts_length':viewed_user_posts_length
    }
    return render(request,'codepub/view-profile.html',context)

@login_required(login_url='login')
def follow(request,F):
    follower = request.user.username
    
    if FollowAccount.objects.filter(follower=follower,user = F).first():
        delete_follower = FollowAccount.objects.get(follower=follower,user = F)
        delete_follower.delete()
    else:
        new_follower = FollowAccount.objects.create(follower=follower,user=F)
        new_follower.save()

    return redirect('/view-profile/'+F)