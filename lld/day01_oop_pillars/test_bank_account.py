import pytest

from lld.day01_oop_pillars.bank_account import (
    BankAccount,
    InsufficientFundsError,
    SavingsAccount,
    TransactionType,
)


def test_deposit_and_withdraw_update_balance_and_history():
    account = BankAccount("Vivek", 1000)
    account.deposit(500)
    account.withdraw(300)

    assert account.balance == 1200
    assert [(tx.type, tx.amount, tx.balance_after) for tx in account.transactions] == [
        (TransactionType.DEPOSIT, 500, 1500),
        (TransactionType.WITHDRAW, 300, 1200),
    ]


def test_cannot_overdraw():
    account = BankAccount("Vivek", 100)
    with pytest.raises(InsufficientFundsError):
        account.withdraw(101)
    assert account.balance == 100  # failed withdrawal changes nothing
    assert account.transactions == ()


@pytest.mark.parametrize("amount", [0, -50])
def test_amount_must_be_positive(amount):
    account = BankAccount("Vivek", 100)
    with pytest.raises(ValueError):
        account.deposit(amount)
    with pytest.raises(ValueError):
        account.withdraw(amount)


def test_balance_cannot_be_set_directly():
    account = BankAccount("Vivek", 100)
    with pytest.raises(AttributeError):
        account.balance = 1_000_000  # type: ignore[misc]


def test_history_cannot_be_edited_from_outside():
    account = BankAccount("Vivek", 100)
    account.deposit(50)
    history = account.transactions
    assert isinstance(history, tuple)  # no .append / .clear on a tuple


def test_savings_account_keeps_minimum_balance():
    savings = SavingsAccount("Ravi", 3000, min_balance=1000)
    savings.withdraw(2000)  # leaves exactly the minimum: allowed
    with pytest.raises(InsufficientFundsError):
        savings.withdraw(1)
    assert savings.balance == 1000


def test_savings_account_is_a_bank_account():
    savings = SavingsAccount("Ravi", 2000)
    assert isinstance(savings, BankAccount)
    savings.deposit(500)  # inherited behaviour, no code duplicated
    assert savings.balance == 2500


def test_savings_account_requires_minimum_to_open():
    with pytest.raises(ValueError):
        SavingsAccount("Ravi", 500, min_balance=1000)
