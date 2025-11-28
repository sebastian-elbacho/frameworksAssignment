from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=250, blank=True)
    city = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"(self.user.username)' s profile"
    

class Project(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  # Kto dodał projekt
    name = models.CharField(max_length=200)  # Nazwa projektu
    description = models.TextField(blank=True)  # Opis projektu (opcjonalny)
    start_date = models.DateField()  # Data rozpoczęcia
    end_date = models.DateField(null=True, blank=True)  # Data zakończenia (opcjonalna)
    stakeholders = models.CharField(max_length=255, blank=True)  # Lista osób zaangażowanych (tekst)
    status = models.CharField(max_length=50, choices=[
        ('planned', 'Zaplanowany'),
        ('in_progress', 'W trakcie'),
        ('finished', 'Zakończony'),
    ], default='planned')  # Status projektu

    def __str__(self):
        return self.name  # Jak ma się wyświetlać w adminie
    




class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    subject = models.CharField(max_length=200)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Wiadomość od {self.sender} do {self.recipient} – {self.subject}"
