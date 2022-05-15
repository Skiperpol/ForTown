from django.contrib import admin
from .models import Event, Image
import smtplib

def sendEmail(toEmail, subject, body):
    with smtplib.SMTP("smtp-mail.outlook.com", 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login("wydarzeniakalisz@outlook.com","HasloKalisz1")

        msg = f'Subject: {subject}\n\n{body}'.encode('utf-8')

        smtp.sendmail("wydarzeniakalisz@outlook.com", toEmail, msg)
        
class ImageAdmin(admin.TabularInline):
    model = Image
    extra = 0

class EventAdmin(admin.ModelAdmin):
    inlines = [ImageAdmin,]
    # wywołuje sie przy zapisie w panel adminie
    def save_model(self, request, obj, form, change):
        if obj.status == "Odrzucone":
            sendEmail("filip.antoniak99@gmail.com", "Odrzucono wydarzenie", f"Wydarzenie {obj} zostalo odrzucone")
            Event.objects.filter(id=obj.id).delete()
        elif obj.status == "Zaakceptowane":
            sendEmail("filip.antoniak99@gmail.com", "Zaakceptowano wydarzenie", f"Wydarzenie {obj} zostalo zaakceptowane")
            obj.status = "Zaakceptowane"
            obj.save()
        elif obj.status == "Oczekuje":
            obj.save()
admin.site.register(Event, EventAdmin)