from dataclasses import field
from rest_framework import serializers
from drf.models import Bicyle

class BicyleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bicyle
        fields = ['id', 'created', 'name', 'reason', 'estimed_time']


    def create(self, validated_data):
        """
        Create new instance of bicycle with validated data
        """
        return Bicyle.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update an existing instance of Bicycle
        """
        instance.name = validated_data.get('name', instance.name)
        instance.reason = validated_data.get('reason', instance.reason)
        instance.estimed_time = validated_data.get('estimed_time', instance.estimed_time)

        instance.save()
        return instance