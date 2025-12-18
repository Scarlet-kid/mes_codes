class Weapon:
    def __init__(self,name,sup):
        self.name = name
        self.sup = sup

    def get_name(self):
        return self.name

    def get_damage_amount(self):
        return self.sup

