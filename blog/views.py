from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Post
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from blog.forms import SendEmailForm
from django.utils import timezone


# Create your views here.


def show_all(request):

    all_posts = Post.objects.filter(status='PB')
    paginator = Paginator(all_posts, 3)
    curr_page = request.GET.get('page', 1)

    try:
        page = paginator.page(curr_page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        page = paginator.page(1)

    context = {
        'page': page
    }

    return render(request, 'blog/all.html', context)


def show_details(request, year, month, day, slug):

    post = get_object_or_404(Post, status='PB', slug=slug, created__year=year, created__month=month, created__day=day)

    context = {
        'post': post
    }

    return render(request, 'blog/details.html', context)


def share_post(request, id):

    sent = False
    post = get_object_or_404(Post, id=id, status="PB")

    if request.method == "POST":
        mail_form = SendEmailForm(request.POST)
        if mail_form.is_valid():
            cd = mail_form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            title = f"{cd['name']} recomends your read"
            message = f"{cd.get('comment', "--placeholder--")} at {post_url}"
            mail = cd['email']
            to = [cd['to']]
            send_mail(title, message, mail, to)
            sent = True
    else:
        mail_form = SendEmailForm()

    context = {
        "form": mail_form,
        "post": post,
        "sent": sent
    }

    return render(request, 'blog/share.html', context)


def delete_post(request, id):

    post = get_object_or_404(Post, status="PB", id=id)
    flag = request.GET.get('flag', False)

    if flag:
        post.delete()
        return redirect("blog:all")
    else:
        context = {
            'post': post
        }

    return render(request, 'blog/delete.html', context)


def edit_post(request,  id):

    post = get_object_or_404(Post, status="PB", id=id)

    if request.GET.get('title', False) or request.GET.get('body', False):
        post.title = request.GET['title'] if request.GET['title'] else post.title
        post.body = request.GET['body'] if request.GET['body'] else post.body
        post.created = timezone.now()
        post.save()
        return redirect("blog:all")
    else:
        context = {
            'post': post
        }
        return render(request, 'blog/edit.html', context)