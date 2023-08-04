from django.forms import ModelForm, CharField, TextInput
from .models import Quote,Tag, Author
from .models import MAX_LENGTH_DESCRIPTION,MAX_LENGTH

class QuoteForm(ModelForm):

    quote = CharField(min_length=5, max_length=MAX_LENGTH_DESCRIPTION, required=True, widget=TextInput())
    author = CharField(min_length=5, max_length=MAX_LENGTH_DESCRIPTION, required=True, widget=TextInput())

    class Meta:
        model = Quote
        fields = ['quote','author']
        exclude = ['tags']

class TagForm(ModelForm):

    name = CharField(min_length=3, max_length=MAX_LENGTH_DESCRIPTION, required=True, widget=TextInput())
    
    class Meta:
        model = Tag
        fields = ['name']

class AuthorForm(ModelForm):
    fullname = CharField(min_length=5, max_length=MAX_LENGTH_DESCRIPTION, required=True, widget=TextInput())
    born_date = CharField(min_length=5, max_length=MAX_LENGTH_DESCRIPTION, required=True, widget=TextInput())
    born_location = CharField(min_length=5, max_length=MAX_LENGTH_DESCRIPTION, required=True, widget=TextInput())
    description = CharField(min_length=5, max_length=MAX_LENGTH_DESCRIPTION, required=True, widget=TextInput())

    class Meta:
        model = Author
        fields = ["fullname","born_date","born_location","description"]
