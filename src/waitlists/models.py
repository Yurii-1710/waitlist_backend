from django.db import models


class WaitlistEntry(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'WaitlistEntries'
        
    def __str__(self):
        return self.email
    