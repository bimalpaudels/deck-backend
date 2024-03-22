from django.db import models

# Create your models here.


class Deck(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class DeckItem(models.Model):
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, related_name="deck")
    front = models.CharField(max_length=255, null=True, blank=True)
    back = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.deck.name} - {self.front}"

