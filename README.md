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
