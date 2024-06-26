import os

import celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")


app = celery.Celery("mysite")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
