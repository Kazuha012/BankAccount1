Bugs & Fixes - [2082/02/03]
-Issue: Deposit method allowed zero deposits.
  -Cause: No validation for zero or negative deposit values.
  -Fix: Added a condition to reject zero deposits before logging transactions.

-Issue: Interest applied to negative balances.
  -Cause: Interest logic didn't check for balance limits.
  -Fix: Implemented a condition to apply interest only if balance > 0.
  