class Member:
    
    def __init__(self, first_name, last_name, premium = False, active = True, id = None):
        self.first_name = first_name
        self.last_name = last_name
        self.premium = premium
        self.active = active
        self.id = id