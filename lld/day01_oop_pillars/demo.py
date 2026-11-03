"""Day 1 visual walkthrough of the 4 OOP pillars.

Run:  python -m lld.day01_oop_pillars.demo
"""
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from lld.day01_oop_pillars.bank_account import BankAccount, InsufficientFundsError, SavingsAccount
from lld.day01_oop_pillars.shapes import Circle, Rectangle, Shape, Triangle, total_area

console = Console()


def pillar(title: str, analogy: str) -> None:
    console.print()
    console.print(Panel(analogy, title=f"[bold]{title}[/bold]", border_style="cyan", expand=False))


def show_encapsulation() -> None:
    pillar("1. Encapsulation", "🏧 An ATM hides the cash vault. You only get buttons: deposit, withdraw.")
    account = BankAccount("Vivek", 5000)
    account.deposit(2000)
    account.withdraw(1500)

    table = Table(title=f"{account!r} — transaction history")
    table.add_column("#", justify="right")
    table.add_column("Type")
    table.add_column("Amount", justify="right")
    table.add_column("Balance after", justify="right")
    for i, tx in enumerate(account.transactions, start=1):
        colour = "green" if tx.type.value == "deposit" else "red"
        table.add_row(str(i), f"[{colour}]{tx.type.value}[/{colour}]", f"₹{tx.amount}", f"₹{tx.balance_after}")
    console.print(table)

    for label, attempt in [
        ("account.withdraw(10_000)", lambda: account.withdraw(10_000)),
        ("account.balance = 1_000_000", lambda: setattr(account, "balance", 1_000_000)),
    ]:
        try:
            attempt()
        except (InsufficientFundsError, AttributeError) as error:
            console.print(f"  🔒 [yellow]{label}[/yellow] → blocked: [italic]{error}[/italic]")


def show_abstraction() -> None:
    pillar("2. Abstraction", "🚗 You press the pedal; you don't need to know how the engine works.")
    try:
        Shape()  # type: ignore[abstract]
    except TypeError as error:
        console.print(f"  [yellow]Shape()[/yellow] → {error}")
    console.print("  Shape is only a contract: 'every shape has area() and perimeter()'.")


def show_inheritance() -> None:
    pillar("3. Inheritance", "🏦 A savings account IS-A bank account, with one extra rule: keep ₹1000.")
    regular = BankAccount("Asha", 3000)
    savings = SavingsAccount("Ravi", 3000, min_balance=1000)
    for account in (regular, savings):
        try:
            account.withdraw(2500)
            console.print(f"  ✅ {account!r} withdrew ₹2500")
        except InsufficientFundsError as error:
            console.print(f"  ❌ {type(account).__name__}: {error}")


def show_polymorphism() -> None:
    pillar("4. Polymorphism", "📯 Same 'horn' button: a bike beeps, a truck honks. Same call, different behaviour.")
    shapes: list[Shape] = [Circle(2), Rectangle(3, 4), Triangle(3, 4, 5)]
    table = Table(title="Same method call: shape.area()")
    table.add_column("Object")
    table.add_column("Area", justify="right")
    table.add_column("Perimeter", justify="right")
    for shape in shapes:
        table.add_row(repr(shape), f"{shape.area():.2f}", f"{shape.perimeter():.2f}")
    console.print(table)
    console.print(f"  total_area(...) = [bold]{total_area(shapes):.2f}[/bold]  (never checks the type!)")

    console.print("\n  [bold]Bonus: value vs identity equality[/bold]")
    console.print(f"  Circle(2) == Circle(2)                           → {Circle(2) == Circle(2)}  (dataclass __eq__)")
    console.print(f"  BankAccount('A', 0) == BankAccount('A', 0)       → {BankAccount('A', 0) == BankAccount('A', 0)}  (different accounts)")


if __name__ == "__main__":
    console.rule("[bold magenta]Day 1 · OOP Pillars")
    show_encapsulation()
    show_abstraction()
    show_inheritance()
    show_polymorphism()
    console.rule()
