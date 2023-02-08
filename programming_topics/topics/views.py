from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Topic, Subtopic
from .forms import SubtopicForm
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
    context = {'post': post}
    return render(request, 'topics/post.html', context)


def post_form(request):
    form = SubtopicForm()
    if request.method == 'POST':
        form = SubtopicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'topics/post_form.html', context)


def update(request, pk):
    post = Subtopic.objects.get(id=pk)
    form = SubtopicForm(instance=post)
    
    if request.method == 'POST':
        form = SubtopicForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post', pk=pk)


    context = {'form': form}
    return render(request, 'topics/post_form.html', context)

def delete(request, pk):
    post = Subtopic.objects.get(id=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('home')

    return render(request, 'topics/delete_post.html')


def about(request):
    # return HttpResponse('<h1>About page</h1>')
    return render(request, 'topics/about.html')