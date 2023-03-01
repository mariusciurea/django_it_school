from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Topic, Subtopic, Comments
from .forms import SubtopicForm
from django.contrib.auth.decorators import login_required
import datetime

# Create your views here.
# dummy_data = [
#     {
#         'id': 1,
#         'name': 'Lets learn python'
#     },
#     {
#         'id': 2,
#         'name': 'Lets learn HTML'
#     },
#     {
#         'id': 3,
#         'name': 'What about JavaScript?'
#     }
# ]


def home(request):
    # return HttpResponse("""<h1>Welcome to my home page</h1>
    #                         <p>daslk;fjaoksdfhaisdhfiajseghfjhasgf</p>""")
    topics = Topic.objects.all()
    print(topics)
    context = {'topics': topics, 'date': [datetime.date.today(), datetime.time]}
    return render(request, 'topics/home.html', context)


def subtopics(request, pk):
    topic = Topic.objects.get(id=pk)
    subtopics = Subtopic.objects.filter(topic=pk)
    context = {'subtopics': subtopics, 'topic': topic}
    return render(request, 'topics/subtopics.html', context)


def post(request, pk):
    post = Subtopic.objects.get(id=pk)
    comments = post.comments_set.all().order_by('-date_created')
    members = post.members.all()

    if request.method == 'POST':
        comment = request.POST.get('text')
        Comments.objects.create(
            user=request.user,
            comment=comment,
            post=post,
        )
        post.members.add(request.user)
        return redirect('post', pk=post.id)

    context = {'post': post, 'comments': comments, 'members': members}
    return render(request, 'topics/post.html', context)

@login_required(login_url='user-login')
def post_form(request, pk):
    form = SubtopicForm()
    topic = Topic.objects.get(id=pk)

    if request.method == 'POST':
        Subtopic.objects.create(
            user=request.user,
            topic=topic,
            name=request.POST['name'],
            content=request.POST.get('content')
        )
        return redirect('subtopic', pk=pk)
        # form = SubtopicForm(request.POST)
        # if form.is_valid():
        #     form.save()
        #     return redirect('home')

    context = {'form': form}
    return render(request, 'topics/post_form.html', context)


@login_required(login_url='user-login')
def update(request, pk):
    post = Subtopic.objects.get(id=pk)
    form = SubtopicForm(instance=post)
    
    if request.user != post.user:
        return HttpResponse('<h1>Not allowed here!</h1>')

    if request.method == 'POST':
        post.name = request.POST['name']
        post.content = request.POST['content']
        post.save()
        return redirect('post', pk=pk)
        # form = SubtopicForm(request.POST, instance=post)
        # if form.is_valid():
        #     form.save()
        #     return redirect('post', pk=pk)


    context = {'form': form}
    return render(request, 'topics/post_form.html', context)


@login_required(login_url='user-login')
def delete(request, pk):
    post = Subtopic.objects.get(id=pk)

    if request.user != post.user:
        return HttpResponse('<h1>Not allowed here!</h1>')

    if request.method == 'POST':
        post.delete()
        return redirect(f'/subtopic/{post.topic.id}')

    return render(request, 'topics/delete_post.html')


def profile(request):
    user_posts = Subtopic.objects.filter(user=request.user)
    context = {'posts': user_posts}
    return render(request, 'topics/profile.html', context)


def about(request):
    # return HttpResponse('<h1>About page</h1>')
    return render(request, 'topics/about.html')