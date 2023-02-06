from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
dummy_data = [
    {
        'id': 1,
        'name': 'Lets learn python'
    },
    {
        'id': 2,
        'name': 'Lets learn HTML'
    },
    {
        'id': 3,
        'name': 'What about JavaScript?'
    }
]


def home(request):
    # return HttpResponse("""<h1>Welcome to my home page</h1>
    #                         <p>daslk;fjaoksdfhaisdhfiajseghfjhasgf</p>""")
    context = {'data': dummy_data}
    return render(request, 'topics/home.html', context)


def subtopics(request, pk):
    data = None
    for item in dummy_data:
        if item['id'] == int(pk):
            data = item
    context = {'data': data}
    print(data)
    return render(request, 'topics/subtopics.html', context)


def about(request):
    # return HttpResponse('<h1>About page</h1>')
    return render(request, 'topics/about.html')