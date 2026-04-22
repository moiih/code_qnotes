from django.db import models
# from django.conf import settings

# User = settings.AUTH_USER_MODEL

# # Create your models here.

# class CodeNotes(models.Model):

#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     note_title = models.CharField(max_length=200)
#     note = models.CharField(max_length=500)
#     note_priority = models.PositiveIntegerField()
#     note_image = models.ImageField(upload_to='Image-Notes', null=True)
#     note_audio = models.FileField(upload_to='Audio-Notes', null=True)
#     date = models.DateField(auto_now=True)
#     time = models.TimeField(auto_now=True)

#     class Meta:
#         db_table = 'notes_keeping_table'
