from rest_framework import serializers
from apps.ratings.models import Rating


class RatingSerializer(serializers.ModelSerializer):
    rater = serializers.SerializerMethodField(read_only=True)
    agent = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Rating
        exclude = ["created_at", "pkid"]

    def get_rater(self, obj):
        return self.rater.username

    def get_agent(self, obj):
        return self.agent.user.username

