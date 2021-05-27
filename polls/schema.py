import graphene
from graphene_django import DjangoObjectType
from .models import Student


class StudentType(DjangoObjectType):
    class Meta:
        model = Student
        fields = ("id", "name", "gpa")


class Query(graphene.ObjectType):
    all_students = graphene.List(StudentType)
    students_by_id = graphene.Field(StudentType, id=graphene.Int(required=True))

    def resolve_all_students(root, info):
        # We can easily optimize query count in the resolve method
        return Student.objects.all() #Ingredient.objects.select_related("category").all()
    def resolve_students_by_id(root, info, id):
        try:
            return Student.objects.get(id=id)
        except Student.DoesNotExist:
            return None

schema = graphene.Schema(query=Query)
