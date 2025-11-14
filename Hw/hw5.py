def admin_only(func):
    def wrapper(user):
        if user.is_admin == True:
            func(user)
        else:
            print('PermissionError: Доступ запрещён! Только админ может выполнить эту операцию.')
    return wrapper
class User:
    def __init__(self, name, is_admin=False):
        self.name = name
        self.is_admin = is_admin
@admin_only
def delete_database(user):
    print("База данных удалена!")
admin = User('Luka', is_admin=True)
user = User('Manuel', is_admin=False)
delete_database(admin)
delete_database(user)
