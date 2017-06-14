from rest_framework import serializers
from .models import *

from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)

class SpotSz(TaggitSerializer, serializers.ModelSerializer):
	tags = TagListSerializerField()

	class Meta:
		model = Spot
		fields = ('id', 'name', 'suburb', 'lat', 'lng', 'tags', )
