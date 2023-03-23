from urllib.parse import urljoin

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.utils import timezone

from apps.accounts.utils import encode_uid
from apps.celery_app import app


@app.task()
def send_email_for_password_reset(user_id: int):
    user = get_user_model().objects.only('email').get(pk=user_id)
    user.last_login = timezone.now()
    user.save(update_fields=('last_login',))

    uid = encode_uid(user.pk)
    token = default_token_generator.make_token(user)

    link = urljoin(
        settings.FRONTEND_HOST,
        settings.FRONTEND_PASSWORD_RESET_PATH.format(uid=uid, token=token),
    )

    print(link, flush=True)
