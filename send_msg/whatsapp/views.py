from django.shortcuts import render
from whatsapp.models import Team
import pywhatkit

def send_msg():
    obj = Team.objects.get(id=1)
    msg = (
        f"Уважаемый {obj.trener.first_name} {obj.trener.otchevstvo} добрый день! В следующие выходные будет турнир. Примите участие?"
    )
    pywhatkit.sendwhatmsg(obj.trener.phone, msg, 15, 2)
