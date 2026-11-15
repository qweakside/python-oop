class Phone:
    line_type='проводной'
    def __init__(self, dial_type_value):
        self.dial_type = dial_type_value
    def Ring(self):
        print("дзз")
    def call(self,number):
        print(f'звоню на {number} по {self.dial_type}, тип связи - {self.line_type}')
        self.Ring()
class MobilePhone(Phone):
    line_type = 'сотовый'
    def __init__(self, dial_type_value):
        super().__init__(dial_type_value)
    def game(self):
        print(f'играть в игру на {self.dial_type}')
phone1 = Phone(dial_type_value='дисковый телефон')
phone2 = MobilePhone(dial_type_value='смартфон')
phone2.game()
phone2.call('123-456')
