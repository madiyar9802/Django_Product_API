from rest_framework import serializers
from .models import Product, PhotoLink, City


class PhotoLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoLink
        fields = ['id', 'product_id', 'photo_link', 'city_id']


class ProductSerializer(serializers.ModelSerializer):
    photo_links = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'photo_links']

    def get_photo_links(self, obj):
        request = self.context.get('request')
        city_id = request.headers.get('City') if request else None

        if city_id:
            photos = obj.photo_links.filter(city_id=city_id)
        else:
            photos = obj.photo_links.filter(city__isnull=True)

        return PhotoLinkSerializer(photos, many=True).data


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name']
