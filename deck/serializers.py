from rest_framework import serializers
from .models import Deck, DeckItem


class DeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = ["id", "name", ]


class DeckItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeckItem
        fields = [
            "id", "deck", "front", "back"
        ]
