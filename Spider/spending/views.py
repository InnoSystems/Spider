from django.http.response import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from .models import Shopping
from django.shortcuts import render, get_object_or_404
from django.urls.base import reverse

# Create your views here.

def index(request):
    latest_shopping_list = Shopping.objects.order_by('-shop_date')[:50]
    template = loader.get_template('spending/index.html')
    context = {
        'latest_shopping_list': latest_shopping_list,
    }
    return HttpResponse(template.render(context, request))

def getShoppingById(request, shopping_id):
    try:
        shopping = Shopping.objects.get(pk=shopping_id)
        template = loader.get_template('spending/indexTwo.html')
        context = {
            'shopping': shopping,
        }
    except Shopping.DoesNotExist:
        raise Http404("Shopping does not exist")
    return HttpResponse(template.render(context, request))

def detail(request, shopping_id):
    try:
        shopping = Shopping.objects.get(pk=shopping_id)
    except Shopping.DoesNotExist:
        raise Http404("Shopping does not exist")
    return render(request, 'spending/detail.html', {'shopping': shopping})

def result(request, shopping_id):
    latest_shopping_list = Shopping.objects.order_by('-shop_date')[:5]
    template = loader.get_template('spending/index.html')
    context = {
        'latest_shopping_list': latest_shopping_list,
    }
    return HttpResponse(template.render(context, request))

def vote(request, shopping_id):
    shopping = get_object_or_404(Shopping, pk=shopping_id)
    try:
        selected_article = shopping.article_set.get(pk=request.POST['article'])
    except (KeyError, Shopping.DoesNotExist):
        # Redisplay the voting form.
        return render(request, 'spending/detail.html', {
            'shopping': shopping,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_article.price += 1
        selected_article.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('spend:results', args=(shopping.id,)))
    
    
def results(request, shopping_id):
    shopping = get_object_or_404(Shopping, pk=shopping_id)
    return render(request, 'spending/results.html', {'shopping': shopping})