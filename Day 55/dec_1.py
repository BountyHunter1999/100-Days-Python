class User:

    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated_decorator(func):
    def wrapper(*args, **kwargs):
        print(args, kwargs)
        user = kwargs['user']
        if user.is_logged_in:
            return func(user)

    return wrapper


@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s blog post.")


new_user = User("Mikeyy")
# new_user.is_logged_in = True
create_blog_post(user=new_user)  # returns () {'user': our user object}
# create_blog_post(new_user)  # return (our user object) {}
