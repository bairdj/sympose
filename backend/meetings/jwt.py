from django.conf import settings
import jwt


def generate(room, user=None):
    payload = {
        "iss": settings.JWT_ISS,
        "sub": settings.JWT_SUB,
        "aud": settings.JWT_AUD,
        "room": room
    }
    if user is not None:
        payload["context"] = {
            "user": {
                "id": user.username,
                "name": "{} {}".format(user.first_name, user.last_name)
            }
        }
    return jwt.encode(payload, settings.JWT_SECRET).decode('utf-8')