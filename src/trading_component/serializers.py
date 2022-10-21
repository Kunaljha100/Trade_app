from datetime import datetime, date

from rest_framework import serializers
from trading_component.models import  order


class orderSerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source = 'user.username')

    class Meta:
        model = order
        fields = ('id','trade_type','entry_price', "quantity", "user","user_name")

