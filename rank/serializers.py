from models import Rank
from rest_framework import serializers

class RankSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializing all the Ranks
    """
    class Meta:
        model = Rank
        #fields = ('id', 'first_name', 'last_name')
        #data = serializers.serialize('json', model.objects.all(), fields=('username', 'email'))
        fields = ('username', 'facebook_id', 'email', 'first_name', 'last_name', 'points', 'highest_score')