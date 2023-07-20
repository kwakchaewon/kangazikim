from django.db import models
from django.utils import timezone
# Create your models here.

class Picture(models.Model):
    id = models.AutoField(primary_key=True)
    userid = models.ForeignKey('accounts.User', on_delete=models.CASCADE, db_column='UserID', blank=False)  # Field name made lowercase.
    photo = models.ImageField(upload_to="picture/post/", null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    model_result= models.CharField(max_length=255, blank=True, null=True) # 모델 결과
    model_conf = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True) # 모델 결과 confidence
    pet_id= models.ForeignKey('accounts.Pet', on_delete=models.CASCADE, db_column='PetID', blank=True, null=True)
    gpt_explain = models.TextField(blank=True, null=True) # GPT 질병 설명
    
    
    class Meta:
        db_table = 'picture'
    def __str__(self) -> str:
        return f"{self.userid}'s {self.pet_id} : {self.model_result} [{self.created_at}]"
        
class Question(models.Model):
    id = models.AutoField(primary_key=True)
    userid = models.ForeignKey('accounts.User', on_delete=models.CASCADE, db_column='UserID', blank=False)  # Field name made lowercase.
    pictureid = models.ForeignKey('Picture', on_delete=models.CASCADE, db_column='PictureID', blank=False, null=False)

    title = models.CharField(db_column='Title', max_length=32, blank=True, null=True)  # Field name made lowercase.
    contents = models.TextField(db_column='Contents', blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'question'
        ordering = ['-created_at']
    def __str__(self) -> str:
        return self.title

class Answer(models.Model):
    id = models.AutoField(primary_key=True)
    userid = models.ForeignKey('accounts.User', on_delete=models.CASCADE, db_column='UserID')  # Field name made lowercase.
    questionid = models.ForeignKey('Question', on_delete=models.CASCADE, db_column='Questionid')  # Field name made lowercase.
    # title = models.CharField(db_column='TItle', max_length=32)  # Field name made lowercase.
    contents = models.TextField(db_column='Contents')  # Field name made lowercase.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'answer'


