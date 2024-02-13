from datetime import datetime
import csv
import allure


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


# Получение текущего дня месяца
day = datetime.now().day
# Вычисление числа Фибоначчи
fib_number = fibonacci(day + 1)


def write_to_csv(filename, data):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date-Time", "Amount", "Transaction Type"])  # Заголовок
        writer.writerows(data)  # Данные


def attach_to_allure_report(filename):
    with open(filename, 'r') as file:
        allure.attach(file.read(), name=filename, attachment_type=allure.attachment_type.CSV)
