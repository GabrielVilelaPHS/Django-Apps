from django.db import models
from ckeditor.fields import RichTextField #campo de texto mais rico
from ckeditor_uploader.fields import RichTextUploadingField #campos de texto que permite upar imagem
from django.contrib.auth.models import User #Gere quem pode entrar


#Classe de objetos, que são as partes do banco de dados 
class Post(models.Model):
    title = models.CharField(max_length= 150)
    summary = RichTextField() #resumo
    content = RichTextUploadingField() #conteudo com imagem
    '''
    on_delete = quando apagar tal post, apaga quem fez
    models.PROTECT = permite apagar so quem fez o post
    '''
    author = models.ForeignKey(User, on_delete = models.PROTECT) 
    created_at = models.DateField(auto_now_add=True)

    def _str_(self):  #exibi o titulo, colocar a função para cada post criado, 
        return self.title #assim aparecera o titulo ao invés de object
