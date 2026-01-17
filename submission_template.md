# AI Code Review Assignment – Eskalate

## Task 1: Average Order Value

### Issue Identified
On the original code the code function sums only non-cancelled orders
then divides it by the total number of orders, resulting in an incorrect average.

for example:
If there are 5 orders means that and 2 are cancelled:
Total includes only 3 orders
Count is still 5
the average (total/count ) becomes incorrect
and also if all are cancelled, it become devision by zero which is invalid

### Correction I Made
The code was updated to count only non-cancelled orders with sum their amount.
so the average (total/count ) becomes only non-cancelled values average which is correct.
and also avoid division by zero.

### Why the Fix is Correct
The average order value must be based only on valid orders.
only when there is non-cancelled, the amount is added and count is increased both are done together means when addition of sum is done its count value increased.

## Task 2: Count Valid Emails

### Issue I Identified
Checking only for the "@" symbol incorrectly marks invalid email addresses as valid.

considers an email valid if it contains "@" but this information need more clarification.
Examples this code wrongly counts as valid:
"@"
"abc@"
"@gmail"
"test@@"
These are not valid email addresses, but the function counts them.
so the original implementation only checked for the presence of the "@" symbol, which caused many invalid email addresses to be counted as valid.

### Correction Made
Basic validation was added to ensure a proper username and domain structure.
I added input validation, removed unnecessary whitespace, and made that each email to should contains exactly one "@" symbol, a valid username, and a domain with a dot.

### Why the Fix is Correct
The updated logic safely filters out invalid email formats while remaining simple and readable. It improves accuracy without overcomplicating the solution.
I used also used regex which is professional and best because of it is:
Industry-standard validation
Accurate email checking
Cleaner logic
so the updated logic filters out clearly invalid emails.

## Task 3: Aggregate Valid Measurements

### Issue Identified
when it say "count = len(values)" the function divides by the total list length instead of counting valid measurements.so:
None values are ignored in the sum
But they are still counted
This gives a wrong average
If all values are None, ZeroDivisionError will happen
### Correction Made
Only non-None values are counted and division by zero is prevented.
I modified the code to count only valid (non-None) measurements.
even if it is None I added a safeguard to prevent division by zero.

### Why the Fix is Correct
The average should be calculated using only valid measurements. This fix is used to ensures accuracy and prevents runtime errors.
and also if there is a None the division by zero is prevented
