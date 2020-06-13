from django.shortcuts import render


def foo(request):
    data = {'blah', 'blaz'}
    return render(request, 'predatoryjournals/home.html', {'data': data})
