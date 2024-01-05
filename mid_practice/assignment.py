class Weapon:
    def __init__(self,name, type, level):
        self.name = name
        self.type = type
        self.level = level

    def upgrade(self):
        self.level = str(int(self.level) + 1)
        print('weapon upgraded level to ' + self.level)

    def display(self):
        print(self.name + ' ' + self.type + ' ' + self.level)

def run():
    weapon1 = Weapon('revolver','pistol','2')
    weapon2 = Weapon('AK47','rifle','1')
    weapon1.upgrade()
    weapon1.display()
    weapon2.upgrade()
    weapon2.display()

