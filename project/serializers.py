from rest_framework import serializers

from project.models import Project, Category, Updateimage


#project
class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


#project Details
class ProjectDetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'




class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class UpdateimageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Updateimage
        fields = "__all__"