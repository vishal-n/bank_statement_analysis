### Submission details:
### Name: Vishal Kaushik
### Email: vishalkaushik2002@gmail.com
### Phone number: +91 9591470582


### To reorder the transaction records in a bank statement
import sys
import pandas as pd
from itertools import permutations


def reorder_transactions(transactions):
    """
    To re-order the transactions in the right order
    """

    try:
        parsed_transactions = []

        for transaction in transactions:
            parts = [x.strip() for x in transaction.split(',')]
            date, narration, debit, credit, closing_balance = parts
            debit = float(debit)
            credit = float(credit)
            closing_balance = float(closing_balance)
            parsed_transactions.append((date, narration, debit, credit, closing_balance))
        
        opening_balance = 10000.0

        for perm in permutations(parsed_transactions):
            balance = opening_balance
            valid = True
            ordered_transactions = []

            for date, narration, debit, credit, closing_balance in perm:
                expected_balance = balance - debit + credit

                if expected_balance == closing_balance:
                    ordered_transactions.append((date, narration, debit, credit, closing_balance))
                    balance = closing_balance
                else:
                    valid = False
                    break
            
            if valid:
                ordered_transactions_df = pd.DataFrame(ordered_transactions, columns=["Date", "Narration", "Debit Amount", "Credit Amount", "Closing Balance"])
                return ordered_transactions_df
        
        return None

    except Exception as e:
        print(f"Unable to re-order the transaction: {e}")
        sys.exit(1)


### To process the input
n = int(input().strip())
transactions = [input().strip() for _ in range(n)]

### To compute the correct sequence of transactions
sorted_transactions_df = reorder_transactions(transactions)
if sorted_transactions_df is not None:
    print("\n")
    print(sorted_transactions_df)
else:
    print("\nError: Could not find a valid sequence.")
