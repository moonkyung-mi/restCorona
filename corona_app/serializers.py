from rest_framework import serializers
from .models import CoPopuDensity

class CoPopuDensitySerializer(serializers.ModelSerializer):
    class Meta:
        model = CoPopuDensity
        fields = [
            "loc",
            "popu_density",
            "qur_rate",
            "std_day",
            "cp_idx",
          ]

