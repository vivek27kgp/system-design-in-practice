"""Bank account: encapsulation + inheritance.

The balance can only change through deposit()/withdraw(), so the rule
"balance never goes below the allowed minimum" is enforced in ONE place.
Money is stored in whole rupees (int) — never use float for money (0.1 + 0.2 != 0.3).
"""
from dataclasses import dataclass
from enum import Enum


class TransactionType(Enum):
    DEPOSIT = "deposit"
    WITHDRAW = "withdraw"


@dataclass(frozen=True)
class Transaction:
    type: TransactionType
    amount: int
    balance_after: int


class InsufficientFundsError(Exception):
    pass


class BankAccount:
    def __init__(self, owner: str, opening_balance: int = 0):
        if opening_balance < 0:
            raise ValueError("opening balance cannot be negative")
        self._owner = owner
        self._balance = opening_balance
        self._transactions: list[Transaction] = []

    # --- read-only views: there are no setters, so `account.balance = 10**9` fails ---
    @property
    def owner(self) -> str:
        return self._owner

    @property
    def balance(self) -> int:
        return self._balance

    @property
    def transactions(self) -> tuple[Transaction, ...]:
        return tuple(self._transactions)  # a copy, so callers can't edit our history

    # --- the only ways to change the balance ---
    def deposit(self, amount: int) -> None:
        self._check_positive(amount)
        self._balance += amount
        self._record(TransactionType.DEPOSIT, amount)

    def withdraw(self, amount: int) -> None:
        self._check_positive(amount)
        if self._balance - amount < self.minimum_balance():
            raise InsufficientFundsError(
                f"cannot withdraw ₹{amount}: balance ₹{self._balance}, minimum ₹{self.minimum_balance()}"
            )
        self._balance -= amount
        self._record(TransactionType.WITHDRAW, amount)

    def minimum_balance(self) -> int:
        """Hook that subclasses override to change the rule without touching withdraw()."""
        return 0

    def _record(self, kind: TransactionType, amount: int) -> None:
        self._transactions.append(Transaction(kind, amount, self._balance))

    @staticmethod
    def _check_positive(amount: int) -> None:
        if amount <= 0:
            raise ValueError("amount must be positive")

    def __repr__(self) -> str:
        return f"{type(self).__name__}(owner={self._owner!r}, balance=₹{self._balance})"


class SavingsAccount(BankAccount):
    """Inheritance: reuses everything from BankAccount, changes only the minimum-balance rule."""

    def __init__(self, owner: str, opening_balance: int = 0, min_balance: int = 1000):
        if opening_balance < min_balance:
            raise ValueError(f"savings account needs at least ₹{min_balance} to open")
        super().__init__(owner, opening_balance)
        self._min_balance = min_balance

    def minimum_balance(self) -> int:
        return self._min_balance
