class User:
    def __init__(self, id: int, name : str):
        self.id = id
        self.name = name
    @classmethod
    def conversion_dico_User(cls, user : 'dict') -> 'User':
        return cls(user['id'],user['name'])
    def conversion_User_dico(self):
        return{'id':self.id, 'name': self.name}