from django.shortcuts import render, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.views import generic, View
from django.views.generic.edit import UpdateView
from django.http import HttpResponseRedirect
from django.views.generic.edit import ModelFormMixin
from .models import *
from .forms import CommentForm, PostForm

# Create your views here.


class PostList(generic.ListView, ModelFormMixin):
    model = Post
    form_class = PostForm
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "post_list.html"
    paginate_by = 24

    def get(self, request, *args, **kwargs):
        self.object = None
        self.form = self.get_form(self.form_class)
        return generic.ListView.get(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = None
        self.form = self.get_form(self.form_class)

        if self.form.is_valid():
            self.object = self.form.save(commit=False)
            self.form_class.Author = request.user.username
            self.form.save()
            self.form = self.get_form(self.form_class)

        return self.get(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(PostList, self).get_context_data(*args, **kwargs)
        context['post_form'] = self.form
        return context


class PostEdit(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post_edit.html'
    success_url = reverse_lazy('post_list')

    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        return Post.objects.get(slug=slug)

    def form_valid(self, form):
        form.instance.Author = self.request.user.username
        return super().form_valid(form)


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.id
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()

        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


class CommentEdit(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment_edit.html'
    success_url = reverse_lazy('post_list')

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return Comment.objects.get(pk=pk)

    def form_valid(self, form):
        form.instance.Author = self.request.user.username
        return super().form_valid(form)


class PostLike(View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))
