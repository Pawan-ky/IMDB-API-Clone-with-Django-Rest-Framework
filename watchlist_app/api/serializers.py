from rest_framework import serializers
from watchlist_app.models import Movie

# by using the built-in `validate` method, we can validate the input data
def name_length(value):
    if len(value)<=3:
        raise serializers.ValidationError("Name must be at least 4 characters long")
    return value

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100, validators=[name_length])
    description = serializers.CharField(max_length=1000)
    active = serializers.BooleanField(default=True)

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance

    # def validate_name (self, value):
    #     if len(value)<=3:
    #         raise serializers.ValidationError("Name must be at least 4 characters long")
    #     return value
    def validate(self, data):
        if data["name"] == data["description"]:
            raise serializers.ValidationError("Name and description cannot be the same")
        return data
        