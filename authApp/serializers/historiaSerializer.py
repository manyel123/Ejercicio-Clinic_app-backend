from authApp.models.historia import Historia
from rest_framework import serializers

class HistoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historia
        fields = ['ultMedTrat','antQuirurgicos','antMedicos','antFarmacologicos','tratamientoFarmacol','diagPrevio','diagActual','observacion']