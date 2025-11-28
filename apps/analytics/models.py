from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Event(models.Model):
    EVENT_VIEW = "view"
    EVENT_LIKE = "like"
    EVENT_SHARE = "share"
    EVENT_COMMENT = "comment"

    EVENT_CHOICES = (
        (EVENT_VIEW, "View"),
        (EVENT_LIKE, "Like"),
        (EVENT_SHARE, "Share"),
        (EVENT_COMMENT, "Comment"),
    )

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    post = models.ForeignKey("blog.Post", on_delete=models.CASCADE, related_name="events")
    event_type = models.CharField(max_length=20, choices=EVENT_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    metadata = models.JSONField(default=dict, blank=True)

    class Meta:
        ordering = ("-created_at",)
