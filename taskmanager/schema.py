import graphene
from graphene_django.types import DjangoObjectType
from tasks.models import Task
from django.contrib.auth.models import User
from tasks.serializers import TaskSerializer
from graphql import GraphQLError

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("id", "username")

class TaskType(DjangoObjectType):
    assignedTo = graphene.Field(UserType)

    class Meta:
        model = Task
        fields = ("id", "title", "status", "created_at")

    def resolve_assignedTo(self, info):
        return self.assigned_to

class Query(graphene.ObjectType):
    all_tasks = graphene.List(TaskType)

    def resolve_all_tasks(self, info):
        user = info.context.user
        if not user.is_authenticated:
            raise Exception("Authentication required")
        return Task.objects.filter(assigned_to=user)

# Mutations
class CreateTask(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        status = graphene.String(required=True)

    task = graphene.Field(TaskType)

    def mutate(self, info, title, status):
        user = info.context.user
        if not user.is_authenticated:
            raise GraphQLError("Authentication required")
        serializer = TaskSerializer(data={'title': title, 'status': status})
        serializer.is_valid(raise_exception=True)
        task = serializer.save(assigned_to=user)
        return CreateTask(task=task)

class UpdateTask(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        title = graphene.String()
        status = graphene.String()

    task = graphene.Field(TaskType)

    def mutate(self, info, id, title=None, status=None):
        user = info.context.user
        if not user.is_authenticated:
            raise GraphQLError("Authentication required")
        try:
            task = Task.objects.get(pk=id, assigned_to=user)
        except Task.DoesNotExist:
            raise GraphQLError("Task not found")
        data = {}
        if title is not None:
            data['title'] = title
        if status is not None:
            data['status'] = status
        serializer = TaskSerializer(task, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        task = serializer.save()
        return UpdateTask(task=task)

class Mutation(graphene.ObjectType):
    create_task = CreateTask.Field()
    update_task = UpdateTask.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)