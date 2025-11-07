# Задание 1 – Банковский аккаунт (инкапсуляция)
import random
import string
class BankAccount:
   def __init__(self, name, balance, password):
       self.name = name                 # открытый
       self._balance = balance          # защищённый
       self.__password = password       # приватный

   def deposit(self, amount, password):
       if self.__password == password:
          self._balance += amount
          return self._balance
       else:
          return 'Неверный пароль!'

   def withdraw(self, amount, password):
       if self.__password == password:
           if self._balance >= amount:
               self._balance -= amount
               return self._balance
           else:
               return 'Недостаточно средств!'
       else:
          return 'Неверный пароль!'

   def change_password(self, old_password, new_password):
       if self.__password == old_password:
          self.__password = new_password
          return 'Пароль изменён'
       else:
          return 'Старый пароль неверный!'

   def get_balance(self, password):
       if self.__password == password:
           return self._balance
       else:
           return 'Неверный пароль!'

   def reset_pin(self, password):
       if self.__password == password:
           new_pin = self.__generate_pin()
           self.__password = new_pin
           return new_pin
       else:
           return 'Неверный пароль!'

   def __generate_pin(self):
       pin = ''.join(random.choice(string.digits) for _ in range(4))
       return pin

print('=== Тест BankAccount ===')
luka = BankAccount('Luka', 500, '2301luka')
print(luka.deposit(50,'2301luka'))
print(luka.withdraw(600,'2301luka'))
print(luka.get_balance('2301luka'))
print(luka.change_password("wrong", "new"))
print(luka.change_password("2301luka", "new"))
new_pin = luka.reset_pin('new')
print(f'Новый PIN: {new_pin}')
print(luka.get_balance(new_pin))

# Задание 2 – Отправка уведомлений (абстрактный класс)
from abc import ABC, abstractmethod

class NotificationSender(ABC):
    @abstractmethod
    def send(self, message, recipient):
        pass

class EmailSender(NotificationSender):
    def __init__(self):
        self._service = "Gmail"

    def send(self, message, recipient):
        return f"Email sent to {recipient}"

    def get_service(self):
        return f"Сервис: {self._service}"

class SmsSender(NotificationSender):
    def __init__(self):
        self._service = "Twilio"

    def send(self, message, recipient):
        return f"SMS sent to {recipient}"

    def get_service(self):
        return f"Сервис: {self._service}"

class PushSender(NotificationSender):
    def __init__(self):
        self._service = "Firebase"

    def send(self, message, recipient):
        return f"Push sent to {recipient}"

    def get_service(self):
        return f"Сервис: {self._service}"

print('\n=== Тест NotificationSender ===')
email = EmailSender()
print(email.send("Здароу", "lukaaxn@mail.ru"))
print(email.get_service())
sms = SmsSender()
print(sms.get_service())
push = PushSender()
print(push.get_service())

# Задание 3 – Система входа и переводов:
class UserAuth:
    def __init__(self, username, account: BankAccount, notifier: NotificationSender):
        self.username = username
        self.account = account
        self.notifier = notifier

    def login(self, password):
        result = self.account.get_balance(password)
        if isinstance(result, int):
            print(self.notifier.send(f"Успешный вход: {self.username}", "system"))
            return True
        else:
            return False

    def transfer(self, amount, password, recipient_account: BankAccount):
        if not self.login(password):
            return "Ошибка авторизации"

        withdraw_result = self.account.withdraw(amount, password)
        if isinstance(withdraw_result, str):
            return withdraw_result

        recipient_account._balance += amount

        print(self.notifier.send(f"Перевод {amount} отправлен", "system"))
        print(self.notifier.send(f"Получено {amount} от {self.username}", "system"))

        return f"Перевод успешен. Новый баланс: {self.account._balance}"


print("\n=== Тест UserAuth ===")
alt = BankAccount("Alt", 100, "alt_pass")
nur = BankAccount("Nur", 100, "nur_pass")
notifier = SmsSender()
auth = UserAuth("alt_doe", alt, notifier)
auth.login("alt_pass")
result = auth.transfer(20, "alt_pass", nur)
print(result)
print(f"Alt balance: {alt.get_balance('alt_pass')}")
print(f"Nur balance: {nur.get_balance('nur_pass')}")