from abc import ABC, abstractmethod
# 1. Базовый класс Hero (наследование)
class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        return f"{self.name} готов к бою!"

# 2. Дочерние классы (наследование + переопределение)
class MageHero(Hero):
    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
        self.mp = mp

    def action(self):
        return f"Маг {self.name} кастует заклинание! MP: {self.mp}"

class WarriorHero(MageHero):
    def action(self):
        return f"Воин {self.name} рубит мечом! Уровень: {self.lvl}"

# 3. Класс BankAccount (инкапсуляция, свойства, методы класса)
class BankAccount:
    bank_name = "Simba"

    def __init__(self, hero, balance, password):
        self.hero = hero
        self._balance = balance
        self.__password = password

    def login(self, password):
        return password == self.__password

    @property
    def full_info(self):
        return f"{self.hero.name} | Уровень: {self.hero.lvl} | Баланс: {self._balance} SOM"

    @classmethod
    def get_bank_name(cls):
        return f"Банк: {cls.bank_name}"

    @staticmethod
    def bonus_for_level(lvl):
        return lvl * 10

# 4. Магические методы
    def __str__(self):
        return f"{self.hero.name} | Баланс: {self._balance} SOM"

    def __add__(self, other):
        if type(self.hero) == type(other.hero):
            return self._balance + other._balance
        else:
            raise ValueError("Нельзя складывать балансы разных типов героев")

    def __eq__(self, other):
        return self.hero.name == other.hero.name and self.hero.lvl == other.hero.lvl

# 5. Абстрактный класс SmsService
class SmsService(ABC):
    @abstractmethod
    def send_otp(self, phone):
        pass

class KGSms(SmsService):
    def send_otp(self, phone):
        return f"<text>Код: 1234</text><phone>{phone}</phone>"

class RUSms(SmsService):
    def send_otp(self, phone):
        return {"text": "Код: 1234", "phone": f"{phone}"}

mag = MageHero("Merlin", 50, 100, 150)
warrior = WarriorHero("Conan", 50, 10, 100)
print(mag.action())
print(warrior.action())

heroacc1 = BankAccount(mag, 5000, "magehero123")
heroacc2 = BankAccount(warrior, 3000, "warriorhero123")
print(heroacc1)
print(heroacc2)
print(BankAccount.get_bank_name())
print(f"Бонус за 50 уровень: {BankAccount.bonus_for_level(50)} SOM")

kg_sms = KGSms()
print(kg_sms.send_otp("+996777123456"))