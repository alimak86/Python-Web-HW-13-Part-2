from django.db import models

# Create your models here.
# class Quote(Document):
#     tags = ListField()
#     author = ReferenceField(Author)
#     quote = StringField()

# class Author(Document):
#     fullname = StringField()
#     born_date = StringField()
#     born_location = StringField()
#     description = StringField()

MAX_LENGTH = 50 # max length of the string fields
MAX_LENGTH_DESCRIPTION = 2000

class Tag(models.Model):
    name = models.CharField(max_length=MAX_LENGTH_DESCRIPTION, null=False, unique=True)
    def __str__(self):
        return f"{self.name}"    

class Author(models.Model):
    fullname = models.CharField(max_length=MAX_LENGTH_DESCRIPTION,null=False)
    born_date = models.CharField(max_length=MAX_LENGTH_DESCRIPTION,null=False)
    born_location = models.CharField(max_length=MAX_LENGTH_DESCRIPTION,null=False)
    description = models.CharField(max_length=MAX_LENGTH_DESCRIPTION, null= False)
    def __str__(self):
        return f"{self.fullname}"

class Quote(models.Model):
    quote = models.CharField(max_length=MAX_LENGTH_DESCRIPTION, null=False)
    author = models.CharField(max_length=MAX_LENGTH_DESCRIPTION, null=False) #models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    tags = models.ManyToManyField(Tag)
    def __str__(self):
        return f"{self.name}"