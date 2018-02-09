# -*- coding: utf-8 -*-
from rest_framework import serializers
from redamigos.apps.chip.models import Chip, State, ChipDelivery

class ChipSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chip
        fields = (
            'lccid',
            'text',
            'user',
            'state',
        )


class StateSerializer(serializers.ModelSerializer):

    class Meta:
        model = State
        fields = (
            'id',
            'description',
        )


class ChipDeliverySerializer(serializers.ModelSerializer):

    class Meta:
        model = ChipDelivery
        fields = (
            'id',
            'chip',
            'delivery'
        )
