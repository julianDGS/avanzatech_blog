import factory

from user.models import User, Team

class TeamFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Team
    
    name = factory.sequence(lambda n: 'Team %s' % n)

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    
    email = factory.Faker('email')
    name = factory.sequence(lambda n: "Name %s" % n)
    last_name = factory.sequence(lambda n: "Last Name %s" % n)

    @factory.post_generation
    def set_user_password(obj, create, extracted, **kwargs):
        if not create:
            # When a related instance (sub factory) is being created and userFactory is already created
            return
        if extracted:
            # If I set a value for password creating an instance of this factory
            obj.set_password(extracted)
        else:
            obj.set_password('1234')