
users = [
    {'name':'james', 'password':123, 'level':'admin'},
    {'name':'george', 'password':234, 'level':'guest'}
]



def make_secure(access_level):
    def decorator(func):
        def user_check(*args, **kwargs):
            for user in users:
                if access_level=='admin':
                    return func(*args, **kwargs)
                else:
                    print (f"{user['name']}  has {access_level}")

        return  user_check
    return decorator

@make_secure('admin')
def admin():
    return '1234'

print(admin())



    

