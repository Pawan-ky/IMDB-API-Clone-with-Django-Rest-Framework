from rest_framework import serializers
from watchlist_app.models import WatchList,StreamPlatform,Reviews

class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Reviews
        # fields = '__all__'
        exclude = ('watchlist',)


class WatchListSerializer(serializers.ModelSerializer):
    #  to show extra fields in response w/o adding it to model
    # name_length = serializers.SerializerMethodField()
    
    # review = ReviewSerializer(many=True,read_only=True)
    # showing name istead of id
    platform = serializers.CharField(source='platform.name')
    class Meta:
        model = WatchList
        fields = '__all__'             # to access all fields in the model
        # fields = ['id', 'name', 'description']           # to access secetive fields in the model
        # exclude = ['name']        # to exclude selected fields in the model

    # def get_name_length(self, obj):
    #     return len(obj.name)

    # def validate_name (self, value):
    #     if len(value)<=3:
    #         raise serializers.ValidationError("Name must be at least 4 characters long")
    #     return value
    # def validate(self, data):
    #     if data["name"] == data["description"]:
    #         raise serializers.ValidationError("Name and description cannot be the same")
    #     return data

class StreamPlatformSerializer(serializers.ModelSerializer):
    # watchlist = WatchListSerializer(many=True,read_only=True)   #for complete movie object

    # watchlist = serializers.StringRelatedField(many=True,read_only=True)
    watchlist = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='movie_detail'
    )
    class Meta:
        model = StreamPlatform
        fields = '__all__'


        










# -------------- by using serializers.serializer -------------

# # by using the built-in `validate` method, we can validate the input data
# def name_length(value):
#     if len(value)<=3:
#         raise serializers.ValidationError("Name must be at least 4 characters long")
#     return value

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=100, validators=[name_length])
#     description = serializers.CharField(max_length=1000)
#     active = serializers.BooleanField(default=True)

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance

#     # def validate_name (self, value):
#     #     if len(value)<=3:
#     #         raise serializers.ValidationError("Name must be at least 4 characters long")
#     #     return value
#     def validate(self, data):
#         if data["name"] == data["description"]:
#             raise serializers.ValidationError("Name and description cannot be the same")
#         return data
        