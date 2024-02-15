import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

from utils import write_to_csv, attach_to_allure_report


class BankingPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    @allure.step("Шаг 1: Открытие страницы авторизации")
    def open_authorization_page(self):
        self.driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")

    @allure.step("Шаг 2: Авторизация на сайте")
    def login(self, user_id):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[ng-click='customer()']"))).click()
        self.wait.until(EC.presence_of_element_located((By.ID, "userSelect")))
        Select(self.wait.until(EC.presence_of_element_located((By.ID, "userSelect")))).select_by_value(user_id)
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
        allure.attach(self.driver.get_screenshot_as_png(), name="LoginPage", attachment_type=allure.attachment_type.PNG)

    @allure.step("Шаг 3: Пополнение счета")
    def deposit(self, amount):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[ng-click='deposit()']"))).click()
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='amount']"))).send_keys(
            str(amount))
        self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "form[name='myForm'] button[type='submit']"))).click()
        allure.attach(self.driver.get_screenshot_as_png(), name="DepositPage",
                      attachment_type=allure.attachment_type.PNG)

    @allure.step("Шаг 4: Снятие со счета")
    def withdraw(self, amount):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[ng-click='withdrawl()']"))).click()
        # Ожидание появления элемента "Amount to be Withdrawn"
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//label[text()='Amount to be Withdrawn :']")))
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='amount']"))).send_keys(
            str(amount))
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
        allure.attach(self.driver.get_screenshot_as_png(), name="WithdrawPage",
                      attachment_type=allure.attachment_type.PNG)

    @allure.step("Шаг 5: Проверка, что баланс равен 0")
    def check_balance_is_zero(self):
        return self.wait.until(
            EC.text_to_be_present_in_element((By.XPATH, "//strong[@class='ng-binding'][text()='0']"), "0"))

    @allure.step("Шаг 6: Проверка страницы транзакций")
    def check_transactions_page(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[ng-click='transactions()']"))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//td[text()='Credit']")))
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//td[text()='Debit']")))
        allure.attach(self.driver.get_screenshot_as_png(), name="TransactionsPage",
                      attachment_type=allure.attachment_type.PNG)

    @allure.step("Шаг 7: Получение данных о транзакциях")
    def get_transaction_data(self):
        rows = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "table.table tbody tr")))
        data = []
        for row in rows:
            cols = row.find_elements(By.CSS_SELECTOR, "td")
            data.append([col.text for col in cols])
        return data

    @allure.step("Шаг 8: Проверка транзакций по сумме")
    def check_transactions_by_amount(self, deposit_amount, withdraw_amount):
        data = self.get_transaction_data()
        deposit_transaction = [row for row in data if row[1] == str(deposit_amount) and row[2] == 'Credit']
        withdraw_transaction = [row for row in data if row[1] == str(withdraw_amount) and row[2] == 'Debit']
        return deposit_transaction and withdraw_transaction

    @allure.step("Шаг 9: Запись данных в CSV и прикрепление файла к отчету Allure")
    def get_and_write_transaction_data(self):
        data = self.get_transaction_data()

        # Запись данных в CSV и прикрепление файла к отчету Allure
        csv_file = 'transactions.csv'
        write_to_csv(csv_file, data)
        attach_to_allure_report(csv_file)
