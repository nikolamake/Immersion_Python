# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10%
# перед каждой операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

class Bankomat:

    TOP_WIHDRAW = 50           # сумма пополнения или снятия
    PERC_WITHDRAW = 0.015      # процент за снятие
    MIN_SUM_WIHDRAW = 30        # мин сум за снятие
    MAX_SUM_WIHDRAW = 600         # макс сум за снятие
    COUNT_PERC = 3              # кол-во операций после кот. добавляются проценты
    PERC_TOP = 0.03             # процент начисления после  COUNT_PERC
    SUMM_WEALTH = 5_000_000    # макс сумма без налога на богатство
    PERC_WEALT = 0.01           # процент налога на богатство

    def __init__(self):
        self.withdraw_amoun = 0                     # сумма для снятия
        self.summ = 0                               # изначальная сумма в банкомате
        self.operations_counter = 0               # кол-во проведенных операций

    def perc_withdraw(self):  # вычисляет сумму процентов за снятие
        if Bankomat.MIN_SUM_WIHDRAW <= Bankomat.PERC_WITHDRAW * self.withdraw_amoun < Bankomat.MAX_SUM_WIHDRAW:
            summ_perc = Bankomat.PERC_WITHDRAW * self.withdraw_amoun
        elif Bankomat.PERC_WITHDRAW * self.withdraw_amoun < Bankomat.MIN_SUM_WIHDRAW:
            summ_perc = Bankomat.MIN_SUM_WIHDRAW
        else:
            summ_perc = Bankomat.MAX_SUM_WIHDRAW
        return summ_perc

    def perc_bonus(self):                                     # доп 3 % после каждой 3-й операции
        if self.operations_counter % Bankomat.COUNT_PERC == 0:
            self.summ += self.summ * Bankomat.PERC_TOP

    def withdraw_cash(self):                                # метод для снятия наличных
        if self.summ > Bankomat.SUMM_WEALTH:                #проверка на сверхдоход 5_000_000
            self.summ -= Bankomat.PERC_WEALT * self.summ
        self.withdraw_amoun = int(input('Введите сумму для снятия со счета: '))
        if self.withdraw_amoun <= 0:
            print('Введена некорректная сумма!')
        elif self.withdraw_amoun + self.perc_withdraw() > self.summ:
            print('Недостаточно средств!')
        elif not self.withdraw_amoun % Bankomat.TOP_WIHDRAW == 0:
            print(f'Сумма не кратна {Bankomat.TOP_WIHDRAW}!')
        else:
            self.perc_bonus()
            self.operations_counter += 1
            self.summ -= (self.withdraw_amoun + self.perc_withdraw())
            print(f'Остаток суммы {self.summ} у.е')


    def deposit_cash(self):    # метод пополнения баланса
        if self.summ > Bankomat.SUMM_WEALTH:
            self.summ -= Bankomat.PERC_WEALT * self.summ
        deposit_amoun = int(input('Введите сумму пополнения счета: '))
        if not deposit_amoun % Bankomat.TOP_WIHDRAW == 0:
            print(f'Сумма не кратна {Bankomat.TOP_WIHDRAW}!')
        elif deposit_amoun <= 0:
            print('Введена некорректная сумма!')
        else:
            self.perc_bonus()
            self.operations_counter += 1
            self.summ += deposit_amoun
            print(f'Всего на счете {self.summ} у.е')


    def balance(self):
        print(f'Сумма на счете {self.summ} у.е')

    def start_bankomat(self):
        while True:
            print('\n Нажмите 1 >>> чтобы снять наличные \
                    \n Нажмите 2 >>> чтобы внести наличные\
                    \n Нажмите 3 >>> чтобы узнать баланс\
                    \n Нажмите 0 >>> для выхода')
            menu = input('Введите номер операции: ')

            match menu:
                case '1':
                    self.withdraw_cash()
                case '2':
                    self.deposit_cash()
                case '3':
                    self.balance()
                case '0':
                    exit()

f=Bankomat()
f.start_bankomat()


