from django.shortcuts import render
from django.http import HttpResponse
from .forms import VisitForm, VisitorNameForm
from .forms import VisitForm
from .models import Visit


def get_all_visits(request):

    visits = Visit.objects.all()

    context = {
        'visits': visits,
    }

    return render(
        request,
        template_name='visits.html',
        context=context,
    )


def get_visit(request, visit_id):

    visit = Visit.objects.get(id=visit_id)

    context = {
        'visit': visit,
    }

    return render(
        request,
        template_name='visit.html',
        context=context,
    )


def add_visit(request):

    form = VisitForm(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():
            math=request.POST['math']
            english=request.POST['english']
            science=request.POST['science']
            average = (int(math)+int(english)+int(science))/3
            visit = Visit(
                student=form.cleaned_data['student'],
                math=form.cleaned_data['math'],
                english=form.cleaned_data['english'],
                science=form.cleaned_data['science'],
                
                #average=form.cleaned_data['average'],
                
            )

            visit.save()

            context = {
                'visit': visit,
            }

            return render(
                request,
                template_name='visit.html',
                context=context,
            )

    return render(
        request,
        template_name='visit_form.html',
        context={'form': form}
)

def filter_visits_by_visitor(request):

    form = VisitorNameForm(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():

            visitor_name = form.cleaned_data['visitor_name']
            visits = Visit.objects.filter(visitor=visitor_name)

            context = {
                'visits': visits,
            }

            return render(
                request,
                template_name='visits.html',
                context=context,
            )

    context = {
        'form': form,
    }

    return render(
        request,
        template_name='visit_form.html',
        context=context,
    )

    
           
       
       

    
