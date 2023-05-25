import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError
from django.db.models import Q

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

    users = graphene.List(
        UserType,
        search=graphene.String(),
        first = graphene.Int(),
        skip= graphene.Int(),
        )


    def resolve_users(self, info, search=None,first= None, skip= None, **kwargs):

        qs = User.objects.all()

        if search:

            filter = (
                Q(username__icontains=search)            
            )
            
            qs = qs.filter(filter)
            
        if skip:
            qs = qs[skip:]
            
        if first:
            qs = qs[:first]

        return qs

        

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
    



