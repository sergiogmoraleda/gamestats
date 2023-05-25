from django.contrib.auth import get_user_model

import graphene
from graphene_django import DjangoObjectType


class UserAuthType(DjangoObjectType):
    class Meta:
        model = get_user_model()

class Query(graphene.ObjectType):
    users_auth = graphene.List(UserAuthType)

    def resolve_users_auth(self, info):
        return get_user_model().objects.all()

class CreateUserAuth(graphene.Mutation):
    user_auth = graphene.Field(UserAuthType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, username, password, email):
        user_auth = get_user_model()(
            username=username,
            email=email,
        )
        user_auth.set_password(password)
        user_auth.save()

        return CreateUserAuth(user_auth=user_auth)


class Mutation(graphene.ObjectType):
    create_userAuth = CreateUserAuth.Field()