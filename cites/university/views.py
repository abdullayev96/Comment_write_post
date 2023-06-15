from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from .models import *
from django.views.generic import ListView, DetailView
import csv
from django.urls import reverse
from .forms import CommentForm
from hitcount.views import HitCountDetailView

# def export_csv(request):
#     students=Followrs.objects.all()
#     response=HttpResponse('text/cvs')
#     response['Content-Disposition'] = 'attachment; filename=export_csv' + str(datetime.now()) + '.csv'
#
#     write=csv.writer(response)
#     write.writerow([ 'id',  'name', "email", "phone_number", "message"])   ##### madel ni ichidagini yozamz
#     students_fields=students.values_list('id', 'name', 'email', "phone_number", "message")
#     for student in students_fields:
#         write.writerow(student)
#     return response

class  PostListView(ListView):
    model  = Customer
    template_name = 'list.html'
    context_object_name = 'posts'



class  PostDetailView(HitCountDetailView):
    model = Customer
    template_name = 'detail.html'
    context_object_name = 'post'
    count_hit = True



    form = CommentForm
    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            post = self.get_object()
            form.instance.user = request.user
            form.instance.post = post
            form.save()

            return redirect('/', str(post.id))

    def get_context_data(self, **kwargs):
        post_comments_count = Comment.objects.all().filter(post=self.object.id).count()
        post_comments = Comment.objects.all().filter(post=self.object.id)
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        context.update({
             'form': self.form,
             'post_comments': post_comments,
             'post_comments_count': post_comments_count,
        })
        return context


def  Contact(request):
    if request.method == 'POST':
        model = Followrs()

        model.name = request.POST.get('name')
        model.email = request.POST.get('email')
        model.number = request.POST.get('number')
        model.message = request.POST.get('message')

        model.save()

        return render(request,'contact.html')
    else:
        return render(request,'contact.html')




