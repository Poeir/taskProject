from django.db import models

# Create your models here.
class Task(models.Model):
    name  = models.CharField(max_length=200)
    status = models.BooleanField(default=False)
    def __str__(self):
        returnStatus = self.status
        if returnStatus == True:
            returnStatus = '(เสร็จสิ้น)'
        else:
            returnStatus = '(ยังไม่เสร็จ)'
        return self.name + returnStatus