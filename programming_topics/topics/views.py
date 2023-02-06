from django.shortcuts import render
from django.http import HttpResponse
from .models import Topic, Subtopic

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
    context = {'topics': topics}
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


def about(request):
    # return HttpResponse('<h1>About page</h1>')
    return render(request, 'topics/about.html')