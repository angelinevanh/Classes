# Conversation with the AI

Written automatically by `tutor.py`. Add your own notes under any entry: what you tried, what broke, what you changed. Those notes are what is graded.

---
## 2026-10-29 12:09, in .

**Me:** hi

**Tutor:**

Refused, off topic.

---
## 2026-10-30 09:03, in .

**Me:** 2.0_user_input.py

**Tutor:**

Refused, off topic.

---
## 2026-10-30 09:07, in .

**Me:** check my code

**Tutor:**

Refused, off topic.

---
## 2026-10-30 09:32, in .

**Me:** 2.1_string_manipulation.py check my code pls

**Tutor:**

Refused, off topic.

---
## 2026-10-30 09:35, in .

**Me:** 2.1_string_manipulation.py How do string methods work?

**Tutor:**

String methods are built-in functions that let you change or inspect strings.

```python
def clean_text(text):
    # TODO: remove leading spaces
    cleaned = text.strip()
    # TODO: convert to lowercase
    cleaned = cleaned.lower()
    # TODO: replace every comma with a space
    cleaned = cleaned.replace(',', ' ')
    return cleaned

# Example call
dirty = "  Hello, World!  "
print(clean_text(dirty))
```

What does the argument `text` become after `strip()`?
