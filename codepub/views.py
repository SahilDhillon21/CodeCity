from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib import messages
from home.models import Profile
from codepub.models import *
from itertools import chain 
import uuid
# Create your views here.

# @login_required(login_url='login')
def codepubHome(request):
    if request.method == 'POST':
        user = request.user.username
        title = request.POST['title-input']
        caption = request.POST['caption-input']
        image = request.FILES.get('image-input')

        new_post = Post.objects.create(title=title,user=user, image = image, caption = caption)
        new_post.save()

        messages.info(request,"Post created successfully")


    user_following_list = []
    feed = []

    user_following = FollowAccount.objects.filter(follower=request.user.username)

    for user in user_following:
        user_following_list.append(user.user)

    for username in user_following_list:
        feed_lists = Post.objects.filter(user=username)
        
        for p in feed_lists:
            feed.append(p)

    # follow suggestions ->
    all_users = User.objects.all()  

    # Extract users from user_following
    followedUsers = []
    for U in user_following:
        person = User.objects.get(username=U.user)
        followedUsers.append(person)


    # Now we have a list of users which the current user follows.
    # The suggestions list must NOT contain these users.
    # Creating list of users that aren't being followed.

    suggested_users = []

    for U in all_users:
        if U not in followedUsers:
            suggested_users.append(U)

    # Remove currently logged in user
    current_user = request.user
    if current_user in suggested_users:
        suggested_users.remove(current_user)

    suggested_profile_followers = []
    for Suser in suggested_users:
        SuserFollowing = FollowAccount.objects.filter(user=Suser.username)
        suggested_profile_followers.append(len(SuserFollowing))

    # gather profiles of these suggested users

    suggested_profiles = []

    for S in suggested_users:
        prof = Profile.objects.get(user=S)
        suggested_profiles.append(prof)

    sug_profiles = zip(suggested_profiles,suggested_profile_followers)
    print(sug_profiles)

    context = {'allPosts':feed,'suggested_profiles':suggested_profiles,'sug_profiles':sug_profiles}
    
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

    follower = request.user.username
    user = pk

    if FollowAccount.objects.filter(follower=follower, user = user).first():
        follow_text = "Unfollow"
    else:
        follow_text = "Follow"

    viewed_user_followers = FollowAccount.objects.filter(user=pk).all()
    no_of_followers = len(viewed_user_followers)

    viewed_users_following = FollowAccount.objects.filter(follower=pk).all()
    no_of_persons_followed = len(viewed_users_following)
    



    context = {
        'viewed_user_object':viewed_user_object,
        'viewed_user_profile':viewed_user_profile,
        'viewed_user_posts':viewed_user_posts,
        'viewed_user_posts_length':viewed_user_posts_length,
        'follow_text':follow_text,
        'viewed_user_followers':viewed_user_followers,
        'no_of_followers':no_of_followers,
        'viewed_users_following':viewed_users_following,
        'no_of_persons_followed':no_of_persons_followed
    }
    return render(request,'codepub/view-profile.html',context)




def search(request):
    if request.method == 'POST':
        query = request.POST['search-input']
        query_users = User.objects.filter(username__icontains=query)
        
        query_profiles = []

        for user in query_users:
            prof = Profile.objects.get(user=user)
            query_profiles.append(prof)
            
    
    context = {'query':query,'query_profiles':query_profiles}

    return render(request,'codepub/search.html',context)



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


@login_required(login_url='login')
@csrf_exempt
def postComment(request):   
    if request.method=='GET':
        post_id = request.GET.get('post_id')
        user = request.user
        post = Post.objects.get(id=post_id)
        

    if request.method=='POST':
        if(request.POST.get("form_type")=="post-comment"):
            post_id = request.POST['post_id']
            post = Post.objects.get(id=post_id)
            comment_input = request.POST['comment-input']
        
            if(len(comment_input)) > 0:
                new_comment = PostComment(comment=comment_input,user=request.user,post=post)
                new_comment.save()
        
        elif(request.POST.get("form_type")=="like-comment"):
            liked_comment_id = request.POST.get("comment_id")
            post_id = request.POST['post_id']
            post = Post.objects.get(id=post_id)

            liked_comment = PostComment.objects.filter(id=liked_comment_id).first()
            liked = liked_comment.isLiked()
            
            if liked:
                liked_comment.likes -= 1
                liked_comment.liked = False
                print('liked1')
            else:
                liked_comment.likes += 1
                liked_comment.liked = True
                print('liked2')
                

            liked_comment.save()
        else:
            post_id = request.POST.get('post_reply_id')
            post = Post.objects.get(id=post_id)
            parent_comment_id = request.POST.get('comment_id')
            reply = request.POST.get('reply')
            parent_comment = PostComment.objects.filter(id=parent_comment_id).first()

            if(len(reply)>0):
                new_reply = PostComment(comment=reply,parent=parent_comment,user=request.user,post=post)
                new_reply.save()


    
    all_comments = PostComment.objects.filter(post=post)
    context = {'post':post,'all_comments':all_comments}
    return render(request,'codepub/commentPostView.html',context)

def report(request,user_id,post_id):
    isPost = is_valid_uuid(post_id)
    print(isPost)
    post = None
    profile = None
    context = {'isPost':isPost, 'post':post, 'profile':profile}

    reported_user = User.objects.get(username=user_id)
    reported_profile = Profile.objects.get(user=reported_user)
    context['profile'] = reported_profile

    if isPost:
        reported_post = Post.objects.get(id=post_id)
        context['post'] = reported_post


    


    return render(request,'codepub/report.html',context)


def is_valid_uuid(value):
    try:
        uuid.UUID(str(value))
        return True
    except ValueError:
        return False
    
def report_submitted(request):
    if request.method=='POST':
        type = request.POST['type']
        post_id = request.POST['post']
        post = Post.objects.get(id=post_id)
        reported_user_name = request.POST.get('reported_user'," none ")
        reported_user = User.objects.get(username=reported_user_name)
        reason = request.POST['reason']

        new_report = Report.objects.create(user = reported_user, post = post, type=type, reason=reason)
        new_report.save()
        messages.error(request,"Report successfully submitted")
    return redirect(codepubHome)

