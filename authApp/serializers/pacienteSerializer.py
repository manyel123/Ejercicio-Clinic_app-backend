from rest_framework import serializers
from authApp.models.paciente import Paciente
from authApp.models.historia import Historia
from authApp.serializers.historiaSerializer import HistoriaSerializer


class PacienteSerializer(serializers.ModelSerializer):
    historia = HistoriaSerializer()
    class Meta:
        model = Paciente
        fields = ['id', 'document', 'name', 'email', 'fechaNacim', 'telefono', 'direccion', 'ciudad']

    def create(self, validated_data):
        historiaData = validated_data.pop('historia')
        pacienteInstance = Paciente.objects.create(**validated_data)
        Historia.objects.create(paciente=pacienteInstance, **historiaData)
        return pacienteInstance


    def to_representation(self, obj):
        paciente = Paciente.objects.get(id=obj.id)
        historia = Historia.objects.get(paciente=obj.id)
        return {
                    'id': paciente.id,
                    'document': paciente.document,
                    'name': paciente.name,
                    'email': paciente.email,
                    'fechaNacim': paciente.fechaNacim,
                    'telefono': paciente.telefono,
                    'direccion': paciente.direccion,
                    'ciudad': paciente.ciudad,
                    'historia': {
                        'id': historia.id,
                        'ultMedTrat': historia.ultMedTrat,
                        'antQuirurgicos': historia.antQuirurgicos,
                        'antMedicos': historia.antMedicos,
                        'antFarmacologicos': historia.antFarmacologicos,
                        'tratamientoFarmacol': historia.tratamientoFarmacol,
                        'diagPrevio': historia.diagPrevio,
                        'diagActual': historia.diagActual,
                        'observacion': historia.observacion
                    }
                }