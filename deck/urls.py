from django.urls import path
from .views import DeckCreateListView, DeckItemCreateListView, DeckRetrieveUDView, ItemRUDView

urlpatterns = [
    path('', DeckCreateListView.as_view(), name='add_list_deck'),
    path('<int:pk>', DeckRetrieveUDView.as_view(), name='individual_deck'),

    path('item', DeckItemCreateListView.as_view(), name='add_list_deck_item'),
    path('item/<int:pk>', ItemRUDView.as_view(), name='update_delete_retrieve_item'),
]