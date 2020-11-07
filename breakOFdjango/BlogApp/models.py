from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploaderField
from django.contrib.auth.models import User #Gere quem pode entrar


#Classe de objetos, que são as partes do banco de dados 
class Post(models.Model):
    title = models.CharField(max_length= 150)
    sumary = RichTextField() #resumo
    content = RichTextUploaderField() #conteudo com imagem
    '''
    on_delete = quando apagar tal post, apaga quem fez
    models.PROTECT = permite apagar so quem fez o post
    '''
    author = models.ForeignKey(User, on_delete = models.PROTECT) 
    created_at = models.DateField(auto_now_add=True)

    def _str_(self):
        return self.title
