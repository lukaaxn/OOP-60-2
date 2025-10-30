# Класс:
class TheOriginal:
    # Конструктор класса:
    def __init__(self, name, age, creature):
        # Атрибуты класса:
        self.name = name
        self.age = age
        self.creature = creature
# Методы класса:
    def description(self):
        if self.name == 'Elijah':
            return f'{self.name} - первородный вампир, {self.age} лет. С рода его семьи началось возраждение вампиров.'
        else:
            return f'{self.name} - первородный гибрид, {self.age} лет. Наполовину вампир, наполовину оборотень.'
    def superpower(self):
        if self.name == 'Elijah':
            return f'{self.name} - обладает способностью внушать и людям, и вампирам.'
        else:
            return f'{self.name} - обладает способностью превращаться в оборотня, когда ему захочется, а не только в полнолуние.'
# Объект\экземпляр класса:
elijah = TheOriginal('Elijah', 1036, 'vampire')
klaus = TheOriginal('Klaus', 1031, 'hybrid')

print(elijah.description())
print(klaus.description())
print(elijah.superpower())
print(klaus.superpower())

