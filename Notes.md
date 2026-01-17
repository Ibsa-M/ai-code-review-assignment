# Notes – AI Code Review Assignment (Eskalate)

## Approach
I reviewed the provided code focusing on correctness, readability, and edge cases.
I analyzed the original implementation and introduced logical improvements while
keeping the solution simple and easy to understand.

---

## Task 2 – Email Validation Logic
The original implementation only checked for the presence of the "@" character,
which resulted in multiple false positives.

The improved solution ensures:
- Each email is a string
- Exactly one "@" exists
- The local part is non-empty
- The domain part contains a "."

This approach improves validation accuracy without unnecessary complexity.

---

## Design Decisions
- Avoided regular expressions to keep the solution readable
- Used simple string operations
- Balanced correctness with simplicity

---

## Limitations
- Does not support all valid email formats (e.g., plus addressing)
- Limited input validation for non-list inputs
- Not fully RFC-compliant

---

## AI Usage
AI tools were used to assist in identifying potential issues and best practices.
All suggestions were manually reviewed and adapted.

---

## Future Improvements
- Introduce regex-based validation if stricter rules are required
- Add unit tests for edge cases
- Improve input validation

---

## Final Notes
This submission focuses on demonstrating thoughtful code review and responsible
AI-assisted development rather than over-engineering.
