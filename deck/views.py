from .models import Deck, DeckItem
from .serializers import DeckSerializer, DeckItemSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status


class DeckCreateListView(ListCreateAPIView):
    serializer_class = DeckSerializer
    queryset = Deck.objects.all()


class DeckItemCreateListView(ListCreateAPIView):
    """Left list for now because it could be used
     in the future to list all cards of a user"""
    serializer_class = DeckItemSerializer
    queryset = DeckItem.objects.all()


class ItemRUDView(RetrieveUpdateDestroyAPIView):
    """Update currently allows to update deck. Shouldn't happen."""
    serializer_class = DeckItemSerializer
    queryset = DeckItem.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "We are done here"}, status=status.HTTP_201_CREATED)


class DeckRetrieveUDView(RetrieveUpdateDestroyAPIView):
    """Retrieve needs to show Deck's data such as name.
    Currently only shows the children it has"""
    serializer_class = DeckSerializer
    queryset = Deck.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instances = DeckItem.objects.filter(deck_id=self.kwargs.get('pk'))
        serializer = DeckItemSerializer(instances, many=True)
        return Response(serializer.data)

