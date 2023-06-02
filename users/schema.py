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
        limit=graphene.Int(),
        )
    
    top_users = graphene.List(
        UserType,
        property=graphene.String(),
        limit=graphene.Int()
    )

    user_by_username = graphene.Field(UserType, username=graphene.String(required=True))

     
    def resolve_top_users(self, info, property=None, limit=None):
        
        if property == "headshotAccuracy":
            order_by = "-stats__headshotAccuracy"
        elif property == "wins":
            order_by = "-stats__wins"
        else:
            order_by = None
        
        if order_by:
            qs = User.objects.all().order_by(order_by)[:limit]
        else:
            qs = User.objects.all()[:limit]

        return qs


    def resolve_users(self, info, search=None,first= None,limit=None, skip= None, **kwargs):

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

        if limit:  # Ordenar por headshotAccuracy de mayor a menor
            qs = qs.order_by('-stats__headshotAccuracy')[:limit]

        return qs
    
    def resolve_user_by_username(self, info, username):
        try:
            user = User.objects.get(username=username)
            return user
        except User.DoesNotExist:
            raise GraphQLError("No existe un usuario con ese nombre de usuario.")
        

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
    



