from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'city']





# # all crud operations can be performed without writing and func
# class StudentSerializer(serializers.ModelSerializer):

#     # Validators
#     def start_with_r(value):
#         if value[0].lower() != 'r':
#             raise serializers.ValidationError('Name should start with r')

#     name = serializers.CharField(validators=[start_with_r])
#     # name = serializers.CharField(read_only=True)
#     class Meta:
#         model = Student
#         fields = ['name', 'roll', 'city']
#         read_only_fields = ['name', 'roll']
#         # extra_kwargs = {'name': {'requires': True}}

# # # Validators
# # def start_with_r(value):
# #     if value[0].lower() != 'r':
# #         raise serializers.ValidationError('Name should start with r')

# # class StudentSerializer(serializers.Serializer):
# #     # id = serializers.IntegerField()
# #     name = serializers.CharField(max_length=100, validators=[start_with_r])
# #     roll = serializers.IntegerField()
# #     city = serializers.CharField(max_length=100)

# #     def create(self, validate_data):
# #         return Student.objects.create(**validate_data)

# #     def update(self, instance, validated_data):
# #         instance.name = validated_data.get('name', instance.name)
# #         instance.roll = validated_data.get('roll', instance.roll)
# #         instance.city = validated_data.get('city', instance.city)
# #         instance.save()
# #         return instance

# #     # validate method is invoked when is_valid() iscalled in views
# #     # Validators have high priority than validate methods
# #     # field level validation
# #     def validate_roll(self, value):
# #         if value >= 200:
# #             raise serializers.ValidationError('Seats full')
# #         return value

# #     # object level validation
# #     def validate(self, data):
# #         nm = data.get('name')
# #         ct = data.get('city')
# #         if nm.lower() == 'ravi' and ct.lower() == 'fbd':
# #             raise serializers.ValidationError('Data not valid')
# #         return data
