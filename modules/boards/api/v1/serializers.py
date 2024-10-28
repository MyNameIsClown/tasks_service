from rest_framework import serializers
from ...models import Board, BoardStatus

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'

class BoardStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardStatus
        fields = '__all__'

