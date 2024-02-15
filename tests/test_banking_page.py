import allure
from pages.Banking_Page import BankingPage
from utils import fib_number


@allure.feature('Banking Page Transactions')
@allure.story('Transaction Test')
@allure.severity(allure.severity_level.CRITICAL)
def test_transactions(driver):
    banking_page = BankingPage(driver)
    deposit_amount = fib_number
    withdraw_amount = fib_number

    with allure.step("Open authorization page"):
        banking_page.open_authorization_page()

    with allure.step("Login with user 2"):
        banking_page.login("2")  # "2" - Harry Potter

    with allure.step("Deposit"):
        banking_page.deposit(deposit_amount)

    with allure.step("Withdraw"):
        banking_page.withdraw(withdraw_amount)

    with allure.step("Check balance is zero"):
        assert banking_page.check_balance_is_zero()

    with allure.step("Check transactions page"):
        banking_page.check_transactions_page()

    with allure.step("check transactions by amount"):
        assert banking_page.check_transactions_by_amount(deposit_amount, withdraw_amount)

    with allure.step("Get and write transaction data"):
        banking_page.get_and_write_transaction_data()
