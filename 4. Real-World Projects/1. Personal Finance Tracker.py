"""
Real-World Project 1: Personal Finance Tracker
===============================================

A complete personal finance management application that demonstrates:
- File handling (JSON for data persistence)
- Object-Oriented Programming
- Data analysis and visualization concepts
- Error handling
- Date/time operations
- User input validation

Features:
1. Add income and expenses
2. Categorize transactions
3. View balance and reports
4. Save/load data from files
5. Generate monthly summaries
"""

import json
from datetime import datetime, date
from pathlib import Path
from typing import List, Dict, Optional


class Transaction:
    """Represents a single financial transaction"""
    
    def __init__(self, amount: float, category: str, description: str, 
                 trans_type: str, date_str: Optional[str] = None):
        self.id = datetime.now().timestamp()
        self.amount = amount
        self.category = category
        self.description = description
        self.trans_type = trans_type  # 'income' or 'expense'
        self.date = date_str if date_str else datetime.now().strftime("%Y-%m-%d")
    
    def to_dict(self) -> Dict:
        """Convert transaction to dictionary"""
        return {
            'id': self.id,
            'amount': self.amount,
            'category': self.category,
            'description': self.description,
            'trans_type': self.trans_type,
            'date': self.date
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Transaction':
        """Create Transaction from dictionary"""
        return cls(
            amount=data['amount'],
            category=data['category'],
            description=data['description'],
            trans_type=data['trans_type'],
            date_str=data['date']
        )
    
    def __str__(self) -> str:
        sign = "+" if self.trans_type == "income" else "-"
        return f"{self.date} | {sign}${self.amount:.2f} | {self.category} | {self.description}"


class FinanceTracker:
    """Main finance tracking application"""
    
    CATEGORIES = {
        'income': ['Salary', 'Freelance', 'Investments', 'Gifts', 'Other'],
        'expense': ['Food', 'Transport', 'Housing', 'Utilities', 'Entertainment', 
                   'Healthcare', 'Shopping', 'Education', 'Other']
    }
    
    def __init__(self, data_file: str = "finance_data.json"):
        self.data_file = Path(data_file)
        self.transactions: List[Transaction] = []
        self.load_data()
    
    def load_data(self) -> bool:
        """Load transactions from JSON file"""
        try:
            if self.data_file.exists():
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    self.transactions = [Transaction.from_dict(t) for t in data]
                print(f"✓ Loaded {len(self.transactions)} transactions")
                return True
            else:
                print("ℹ No existing data file found. Starting fresh.")
                return False
        except Exception as e:
            print(f"✗ Error loading data: {e}")
            return False
    
    def save_data(self) -> bool:
        """Save transactions to JSON file"""
        try:
            with open(self.data_file, 'w') as f:
                json.dump([t.to_dict() for t in self.transactions], f, indent=2)
            print(f"✓ Saved {len(self.transactions)} transactions")
            return True
        except Exception as e:
            print(f"✗ Error saving data: {e}")
            return False
    
    def add_transaction(self, amount: float, category: str, description: str, 
                       trans_type: str) -> bool:
        """Add a new transaction"""
        try:
            if trans_type not in ['income', 'expense']:
                raise ValueError("Type must be 'income' or 'expense'")
            
            if amount <= 0:
                raise ValueError("Amount must be positive")
            
            transaction = Transaction(amount, category, description, trans_type)
            self.transactions.append(transaction)
            self.save_data()
            print(f"✓ Added {trans_type}: ${amount:.2f}")
            return True
        except Exception as e:
            print(f"✗ Error adding transaction: {e}")
            return False
    
    def get_balance(self) -> float:
        """Calculate current balance"""
        income = sum(t.amount for t in self.transactions if t.trans_type == 'income')
        expenses = sum(t.amount for t in self.transactions if t.trans_type == 'expense')
        return income - expenses
    
    def get_summary(self) -> Dict:
        """Get financial summary"""
        income = sum(t.amount for t in self.transactions if t.trans_type == 'income')
        expenses = sum(t.amount for t in self.transactions if t.trans_type == 'expense')
        
        # Category breakdown
        expense_by_category = {}
        for t in self.transactions:
            if t.trans_type == 'expense':
                expense_by_category[t.category] = expense_by_category.get(t.category, 0) + t.amount
        
        return {
            'total_income': income,
            'total_expenses': expenses,
            'balance': income - expenses,
            'transaction_count': len(self.transactions),
            'expense_by_category': expense_by_category
        }
    
    def get_monthly_report(self, year: int, month: int) -> Dict:
        """Generate report for specific month"""
        monthly_transactions = [
            t for t in self.transactions 
            if t.date.startswith(f"{year}-{month:02d}")
        ]
        
        income = sum(t.amount for t in monthly_transactions if t.trans_type == 'income')
        expenses = sum(t.amount for t in monthly_transactions if t.trans_type == 'expense')
        
        return {
            'month': f"{year}-{month:02d}",
            'income': income,
            'expenses': expenses,
            'balance': income - expenses,
            'transactions': len(monthly_transactions)
        }
    
    def list_transactions(self, limit: int = 10) -> List[str]:
        """List recent transactions"""
        sorted_trans = sorted(self.transactions, key=lambda t: t.date, reverse=True)
        return [str(t) for t in sorted_trans[:limit]]
    
    def delete_transaction(self, trans_id: float) -> bool:
        """Delete a transaction by ID"""
        for i, t in enumerate(self.transactions):
            if t.id == trans_id:
                del self.transactions[i]
                self.save_data()
                return True
        return False


def print_menu():
    """Display main menu"""
    print("\n" + "=" * 50)
    print("PERSONAL FINANCE TRACKER")
    print("=" * 50)
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Balance & Summary")
    print("4. View Recent Transactions")
    print("5. Monthly Report")
    print("6. Export Data")
    print("7. Exit")
    print("=" * 50)


def select_category(trans_type: str) -> str:
    """Let user select a category"""
    categories = FinanceTracker.CATEGORIES[trans_type]
    print(f"\n{trans_type.capitalize()} Categories:")
    for i, cat in enumerate(categories, 1):
        print(f"  {i}. {cat}")
    
    while True:
        try:
            choice = int(input("Select category (number): "))
            if 1 <= choice <= len(categories):
                return categories[choice - 1]
            print("Invalid choice!")
        except ValueError:
            print("Please enter a number!")


def get_float_input(prompt: str) -> float:
    """Get validated float input"""
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            print("Value must be positive!")
        except ValueError:
            print("Please enter a valid number!")


def main():
    """Main application loop"""
    tracker = FinanceTracker()
    
    while True:
        print_menu()
        choice = input("Enter your choice (1-7): ").strip()
        
        if choice == '1':  # Add Income
            amount = get_float_input("Enter amount: $")
            category = select_category('income')
            description = input("Description: ").strip()
            tracker.add_transaction(amount, category, description, 'income')
        
        elif choice == '2':  # Add Expense
            amount = get_float_input("Enter amount: $")
            category = select_category('expense')
            description = input("Description: ").strip()
            tracker.add_transaction(amount, category, description, 'expense')
        
        elif choice == '3':  # View Summary
            summary = tracker.get_summary()
            print("\n" + "=" * 50)
            print("FINANCIAL SUMMARY")
            print("=" * 50)
            print(f"Total Income:   ${summary['total_income']:.2f}")
            print(f"Total Expenses: ${summary['total_expenses']:.2f}")
            print(f"Current Balance: ${summary['balance']:.2f}")
            print(f"Transactions: {summary['transaction_count']}")
            
            if summary['expense_by_category']:
                print("\nExpenses by Category:")
                for cat, amount in sorted(summary['expense_by_category'].items()):
                    percentage = (amount / summary['total_expenses'] * 100) if summary['total_expenses'] > 0 else 0
                    print(f"  {cat}: ${amount:.2f} ({percentage:.1f}%)")
        
        elif choice == '4':  # View Transactions
            limit = int(input("How many recent transactions? (default 10): ") or "10")
            transactions = tracker.list_transactions(limit)
            print("\n" + "=" * 50)
            print("RECENT TRANSACTIONS")
            print("=" * 50)
            if transactions:
                for t in transactions:
                    print(t)
            else:
                print("No transactions yet!")
        
        elif choice == '5':  # Monthly Report
            try:
                year = int(input("Year (YYYY): "))
                month = int(input("Month (MM): "))
                report = tracker.get_monthly_report(year, month)
                print("\n" + "=" * 50)
                print(f"MONTHLY REPORT - {report['month']}")
                print("=" * 50)
                print(f"Income: ${report['income']:.2f}")
                print(f"Expenses: ${report['expenses']:.2f}")
                print(f"Balance: ${report['balance']:.2f}")
                print(f"Transactions: {report['transactions']}")
            except ValueError:
                print("Invalid date format!")
        
        elif choice == '6':  # Export Data
            filename = input("Export filename (default: export.json): ") or "export.json"
            try:
                with open(filename, 'w') as f:
                    json.dump([t.to_dict() for t in tracker.transactions], f, indent=2)
                print(f"✓ Data exported to {filename}")
            except Exception as e:
                print(f"✗ Export failed: {e}")
        
        elif choice == '7':  # Exit
            print("\nThank you for using Personal Finance Tracker!")
            print("Your data has been saved.")
            break
        
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()

"""
HOW TO USE THIS PROJECT:
========================

1. Run the script: python "4. Real-World Projects/1. Personal Finance Tracker.py"

2. The app will:
   - Load any existing data from finance_data.json
   - Show you a menu of options
   - Let you add income and expenses
   - Track your balance automatically
   - Generate reports and summaries

3. Your data is automatically saved after each transaction

4. Features to explore:
   - Add multiple income sources
   - Categorize expenses
   - View spending patterns by category
   - Generate monthly reports
   - Export data for backup

SKILLS DEMONSTRATED:
====================
✓ File I/O (JSON)
✓ Classes and Objects
✓ Error Handling
✓ Data Structures (Lists, Dictionaries)
✓ Date/Time Operations
✓ User Input Validation
✓ Type Hints
✓ Documentation
"""
