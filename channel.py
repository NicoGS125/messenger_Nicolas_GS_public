class Channels :
    def __init__(self, id: int, name: str, member_id : list):
        self.id = id
        self.name = name
        self.member_id = member_id
    @classmethod
    def conversion_dico_Channels(cls, channels : 'dict') -> 'Channels':
        return cls(channels['id'], channels['name'], channels['member_id'])
    def conversion_Channels_dico(self):
        return{'id': self.id, 'name': self.name, 'member_id': self.member_id}
