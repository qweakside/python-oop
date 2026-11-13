class MushroomsCollector:
    def __init__(self):
        self.mushrooms = []
    def is_poisonous(self,mushroom):
        if mushroom == "Мухомор" or mushroom == "Поганка":
            return True
        return False
    def add_mushroom(self,mushroom):
        if self.is_poisonous(mushroom):
            print('Нельзя добавить ядовитый гриб')
        else:
            self.mushrooms.append(mushroom)
    def __str__(self):
        return ", ".join(self.mushrooms)
zxc=MushroomsCollector()
zxc.add_mushroom("Мухомор")
zxc.add_mushroom("Лисичка")
zxc.add_mushroom("Опенок")
print(zxc)
