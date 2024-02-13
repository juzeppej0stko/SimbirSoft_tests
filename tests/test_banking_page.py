from pages.Banking_Page import BankingPage
from utils import fib_number


def test_transactions(driver):
    banking_page = BankingPage(driver)
    banking_page.open_main_page()
    banking_page.login()
    banking_page.deposit(fib_number)
    banking_page.withdraw(fib_number)
    banking_page.check_balance()
    banking_page.check_transactions()
    banking_page.get_and_write_transaction_data()
