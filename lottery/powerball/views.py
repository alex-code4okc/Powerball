from django.shortcuts import render, HttpResponseRedirect
# importing generic class based views (List, Detail, etc.)
from django.views import generic


from random import randrange

# Create your views here.
def powerball(request):
    context = {}
    if(request.method == 'POST'):
        wb_array = []
        while(len(wb_array)<5):
            pick = randrange(1,70)
            if pick not in wb_array:
                wb_array.append(pick)

        pb = randrange(1,27)

        context['wb_array'] = sorted(wb_array)
        context['pb'] = pb
        
        if('next' in request.POST):
            context['next'] = 'next'

        return render(request,'powerball.html',context=context)
    else:
        return render(request,'powerball.html',context=context)