from django import template
from mainApp.models import Comment, SubComment, Post


register = template.Library()


@register.filter(name='comments')
def comments(post_id):
    comm = []
    post = Post.objects.get(id=int(post_id))

    for c in Comment.objects.filter(post=post):
        comm.append([c, SubComment.objects.filter(comment=c)])

    return comm
