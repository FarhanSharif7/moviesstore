from django.db import models
from django.contrib.auth.models import User
from movies.models import Movie

class HiddenMovie(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
	hidden_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		unique_together = ('user', 'movie')

	def __str__(self):
		return f"{self.user.username} hid {self.movie.name}"
