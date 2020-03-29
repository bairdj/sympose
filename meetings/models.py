from django.db import models
from django.contrib.auth.models import  User
from django.conf import settings
from .jwt import generate
import uuid


class Meeting(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned')
    room_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    subject = models.CharField(max_length=50)
    start_time = models.DateTimeField()
    is_anonymous = models.BooleanField("allow anonymous access", default=False)
    attendees = models.ManyToManyField(to=User, through='Attendee', related_name='meetings')

    class Meta:
        ordering = ['start_time']

    def __str__(self):
        return self.subject

    def jwt(self):
        if self.is_anonymous is False:
            return None
        return generate(self.room_id)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('meeting', args=[self.room_id])


class Attendee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    is_moderator = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'meeting'], name='unique_meeting')
        ]

    def __str__(self):
        return str(self.user)

    def jwt(self):
        return generate(str(self.meeting.room_id), self.user)

    def url(self):
        string = "{}/{}?jwt={!s}".format(settings.JITSI_URL, self.meeting.room_id, self.jwt())
        print(string)
        return string




