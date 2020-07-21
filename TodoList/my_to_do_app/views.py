from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *

# Create your views here.

def index(request):
    todos = Todo.objects.all() #모든 데이터를 선택
    content = {'todos': todos}
    return render(request, 'my_to_do_app/index.html', content)

def createTodo(request):
    user_input_str = request.POST['todoContent']
    new_todo = Todo(content=user_input_str)
    new_todo.save()
    print('새로만든 todo의 id', new_todo.id)
    return HttpResponseRedirect(reverse('index'))
    #return HttpResponse("create Todo를 할 거야! =>"+user_input_str)

def doneTodo(request):
    done_todo_id = request.GET['todoNum']
    print('완료한 todo의 id', done_todo_id)
    # Todo모델의 object에 접근, id가 done_todo_id 인 데이터를 todo에 저장
    todo = Todo.objects.get(id=done_todo_id)
    #todo의 isDone 데이터를 True로 변경 -> index에서 출력안함
    todo.isDone=True
    todo.save()
    return HttpResponseRedirect(reverse("index"))