## 📁 Тестовое задание на вакансию SDET (Разработчик в тестировании)
<details>
  <summary>Само задание</summary>
  
  Данное тестовое задание предназначено для выявления следующих навыков:  
  • Умение работать самостоятельно;  
  • Скорость выполнения задач;  
  • Работа с современными технологиями.  

Во время выполнения тестового задания важно по максимуму проявить эти
качества.  

При выполнении работы необходимо использовать следующие
технологии:  

1) Selenium GRID (тесты запускать через GRID обязательно)
2) Использовать паттерн проектирования автотестов Page Object
3) Реализовать формирование отчетов о пройденных тестах через Allure

В задании необходимо:  

1) Использовать Python/Java, подключить библиотеку Selenium Webdriver;
2) С помощью Selenium открыть браузер, открыть страницу страницу
https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login;
3) Авторизоваться пользователем «Harry Potter»;
4) Вычислить N-е число Фибоначчи, где N - это текущий день месяца + 1.
Пример: сегодня 08.02.2023, 9-е чисто Фибоначчи равно 21;
5) Выполнить пополнение счета (Deposit) на сумму равную вычисленному в
п.4 числу;
6) Выполнить списание со счета (Withdrawl) на сумму равную вычисленному
в п.4 числу;
7) Выполнить проверку баланса - должен быть равен нулю;
8) Открыть страницу транзакций и проверить наличие обеих транзакций;
9) Сформировать файл формата csv, в который выгрузить данные о
проведенных транзакциях;
Файл должен содержать строки следующего формата
<Дата-времяТранзакции Сумма ТипТранзакции>, где
Формат Дата-времяТранзакции - "ДД Месяц ГГГГ ЧЧ:ММ:СС"
Формат Сумма - число
Формат ТипТранзакции - значение из списка [Credit, Debit]
10) Оформить сформированный файл как вложение к отчету allure.
  
</details>

## 🛠️ Установка
Для установки зависимостей проекта выполните следующую команду:
```bash
pip install -r requirements.txt
```
Для запуска Selenium Grid выполните следующую команду, находясь в папке, где находится файл selenium-server-4.17.0.jar :
```bash
java -jar selenium-server-4.17.0.jar standalone
```
## 🏃 Запуск тестов
Для запуска тестов и генерации отчетов Allure используйте следующую команду:
```bash
pytest tests/test_banking_page.py --alluredir %reports%
```
## 📁 Просмотр отчетов Allure
Для просмотра отчета Allure используйте команду следующего вида в зависимости от расположения ваших директорий:
```bash
C:\Users\WORK\Downloads\allure-2.27.0\bin\allure serve C:\Users\WORK\PycharmProjects\SimbirSoft\%reports%
```
## 📁 Скриншот примера сформированного отчета Allure 
<p align="center">
  <img src="/allure.jpg">
</p>
