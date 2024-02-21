from django.db import models

# Create your models here.


class Blog(models.Model):
    """Model definition for Blog."""

    # TODO: Define fields here
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for Blog."""

        verbose_name = "Blog"
        verbose_name_plural = "Blogs"

    def __str__(self):
        """Unicode representation of Blog."""
        return self.title
