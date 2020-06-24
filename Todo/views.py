from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from Todo.models import What_Todo
from django.http import HttpResponseRedirect

# Create your views here.


def home(request):
    todo_items = What_Todo.objects.all().order_by("-added_date")
    return render(request, 'Todo/index.html', {
        "todo_items": todo_items
    })


@csrf_exempt
def add_todo(request):
    current_date = timezone.now()
    content = request.POST["content"]
    What_Todo.objects.create(
        added_date=current_date, text=content)
    return HttpResponseRedirect('/')


@csrf_exempt
def delete_todo(request, todo_id):
    # Deleting an item in Django
    What_Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/")
