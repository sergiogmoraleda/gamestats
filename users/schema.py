import graphene
from graphene_django import DjangoObjectType

from .models import User
from .models import StatsUser

# TYPES
class UserType(DjangoObjectType):
    class Meta:
        model = User

class StatsUserType(DjangoObjectType):
    class Meta:
        model = StatsUser


# QUERYS

class Query(graphene.ObjectType):

    users = graphene.List(UserType)

    def resolve_users(self, info, **kwargs):
        return User.objects.all()

# MUTATIONS



class StatsUserInput(graphene.InputObjectType):
    
    wins = graphene.Int()
    defeat = graphene.Int()
    kda = graphene.String()
    headshotAccuracy = graphene.Float()


class CreateUser(graphene.Mutation):

    id = graphene.ID()
    username = graphene.String()
    stats = graphene.Field(StatsUserType)
    
    class Arguments:

        username = graphene.String()
        stats = StatsUserInput()
        

    def mutate(self, info, username, stats):

        stats_user = StatsUser(wins=stats.wins, defeat=stats.defeat, kda= stats.kda, headshotAccuracy= stats.headshotAccuracy)
        stats_user.save()

        user = User(username= username, stats=stats_user)
        user.save()



        return CreateUser(
            id = user.id,
            username = user.username,
            stats = user.stats
        )

class Mutation(graphene.ObjectType):

    create_user = CreateUser.Field()
    



