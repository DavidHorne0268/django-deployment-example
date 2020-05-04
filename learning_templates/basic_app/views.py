from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'text': 'hello world', 'number': 100}

    return render(request, 'basic_app/index.html', context_dict)

def other(request):
    contextdata = {}
    contextdata['data'] = ['david','richard', 'rachel']
    contextdata['data2'] = [1,2,3,4,5]
    print(contextdata)
    return render(request, 'basic_app/other.html', context=contextdata)

def relative(request):
    return render(request, 'basic_app/relative_url_templates.html')

