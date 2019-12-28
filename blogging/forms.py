from django.forms import ModelForm
from blogging.models import Post, Category

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'title', 
            'text', 
            'author', 
            # 'create_date', 
            # 'modified_date', 
            'published_date'
        ]

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = [
            'name', 
            'description', 
            'posts'
        ]
