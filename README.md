# User Input in the Python Terminal

This lesson explains, step by step, how a Python program reads information
typed by a user in a terminal, converts that text to other data types, and
displays the results with f-strings. The runnable example is
[`user_input_examples.py`](./user_input_examples.py).

## Requirements

- Python 3
- A terminal
- No third-party packages

## Run the example

Open a terminal in this repository and run:

```shell
python user_input_examples.py
```

On some systems, the Python command is `python3`:

```shell
python3 user_input_examples.py
```

The program asks for your name, age, and height. Type an answer and press
**Enter** after each prompt. For the height, use a decimal point, for example
`1.68`.

## 1. What happens when a program asks for input?

When a program runs in a terminal, it can display a prompt and wait for the
person running it to type a response. The built-in `input()` function performs
this interaction:

```python
name = input("What is your name? ")
```

Python displays the prompt text, waits for the user to press **Enter**, and
then continues. The typed response is assigned to `name`.

The prompt is optional:

```python
answer = input()
```

Without a prompt, the program still waits for input, but it does not display a
question first. A prompt usually ends with a space so the user's answer does
not appear immediately next to the question.

### `input()` always returns a string

Even when the user types digits, `input()` returns text (`str`), not a number:

```python
age_text = input("How old are you? ")
print(type(age_text))
```

If the user types `21`, the type is still `str`. In other words, the value is
the text `"21"`, not the integer `21`. Pressing **Enter** ends the response;
the newline used to submit it is not included in the returned string.

`input()` does not remove other whitespace for you. If a person types spaces
before or after an answer, those spaces remain. Use `.strip()` when surrounding
whitespace should be removed:

```python
name = input("What is your name? ").strip()
```

`.strip()` returns a new string with whitespace removed from both ends. It does
not remove spaces between words.

## 2. Convert input text to another type

Because `input()` returns a string, convert the response before using it as a
number in calculations. Calling a type such as `int` or `float` this way is
commonly called **type conversion** (or, informally, casting).

### Convert to an integer with `int()`

```python
age_text = input("How old are you? ")
age = int(age_text)
print(age + 1)
```

If the user types `21`, `int()` converts the text `"21"` to the integer `21`,
so adding one produces `22`.

`int()` accepts text that represents an integer, such as `"21"` or `"-4"`.
It does not accept a decimal string such as `"21.5"`:

```python
int("21")    # 21
int("21.5")  # raises ValueError
```

### Convert to a decimal number with `float()`

Use `float()` when the answer may contain a decimal part:

```python
height_text = input("How tall are you in meters? ")
height = float(height_text)
```

For example, `float("1.68")` produces the floating-point number `1.68`.
In this example, enter a decimal point (`.`), not a comma.

### Convert a value to text with `str()`

`str()` converts many values to text. This can be useful when joining text with
a value using `+`:

```python
age = 21
message = "Age: " + str(age)
```

F-strings, introduced later in this lesson, are usually clearer for combining
text and values.

### Conversion is not validation

Conversion checks whether text can be represented as a type; it does not check
whether the answer makes sense for your program. For example, `int("-5")` is a
valid conversion even if an age should not be negative. Programs should check
their own rules after conversion.

## 3. Handle invalid input

If text cannot be converted, Python raises a `ValueError`. Without handling
that exception, the program stops with an error message. Use `try` and
`except ValueError` to respond clearly:

```python
age_text = input("How old are you? ")

try:
    age = int(age_text)
except ValueError:
    print("Please enter a whole number, such as 21.")
else:
    print(f"Next year, you will be {age + 1}.")
```

Python runs the statements in `try` first. If conversion raises
`ValueError`, it runs the `except` block. If conversion succeeds, it runs the
`else` block. The example program converts both its numeric responses inside a
`try` block and exits with a helpful message if either response is invalid.

## 4. Put values into output with f-strings

An **f-string** is a string prefixed with `f`. Put a Python expression inside
curly braces (`{}`) to include its value in the text:

```python
name = "Maya"
age = 21
print(f"Hello, {name}. You are {age} years old.")
```

The output is:

```text
Hello, Maya. You are 21 years old.
```

Python evaluates each expression inside the braces and inserts the result.
Expressions can include calculations:

```python
print(f"Next year, you will be {age + 1}.")
```

### Format numbers

A format specifier follows a colon inside the braces:

```python
height = 1.68
price = 1234.5

print(f"Height: {height:.2f} meters")
print(f"Price: ${price:,.2f}")
```

- `:.2f` displays a floating-point number with two digits after the decimal
  point. For example, `1.68` and `1.70`.
- `:,.2f` also groups thousands with commas. For example, `$1,234.50`.
- Formatting affects how a value is displayed; it does not change the original
  value's type.

To display a literal brace rather than start an expression, double it:

```python
print(f"Use {{name}} to show the braces.")
```

This prints `Use {name} to show the braces.`

## 5. Follow the example from input to output

The example program follows this sequence:

1. It calls `input()` to ask for a name, age, and height.
2. It calls `.strip()` to remove accidental whitespace around the name.
3. It converts the age text with `int()` and the height text with `float()`.
4. It catches `ValueError` and explains what to enter if conversion fails.
5. It uses f-strings to display the answers, calculate the age next year, and
   format the height to two decimal places.

For example, if the answers are `Maya`, `21`, and `1.68`, the final output
includes:

```text
Hello, Maya!
You are 21 years old.
Next year, you will be 22.
Your height is 1.68 meters.
```

Your output will contain the answers you typed.

## Common mistakes

| Mistake | Why it happens | What to do |
|---|---|---|
| Adding a number directly to input text | `input()` returns `str` | Convert it first with `int()` or `float()` |
| Entering letters when the program expects a number | The text cannot be converted | Catch `ValueError` and explain the expected input |
| Using `int()` for a decimal such as `"1.5"` | A decimal string is not an integer literal | Use `float()` for decimal input |
| Expecting `.strip()` to remove spaces between words | `.strip()` only removes whitespace at the ends | Keep internal spaces or process the text separately |
| Expecting a formatted number to change the variable | An f-string format controls display only | Store a converted or rounded value separately if needed |

Do not use `eval()` to convert user input. It executes Python code rather than
performing a safe conversion. Use `int()`, `float()`, and appropriate input
checks instead.

## Practice

1. Ask for a favorite color and print a sentence containing it with an
   f-string.
2. Ask for two whole numbers, convert them with `int()`, and print their sum.
3. Ask for a price, convert it with `float()`, and display it with two decimal
   places.
4. Try entering text instead of a number in the example. Read the error
   message, then enter a valid number.

## Remember

- `input()` displays an optional prompt and waits for a response.
- The result of `input()` is always a string.
- Convert numeric text with `int()` or `float()` before doing arithmetic.
- Invalid conversions can raise `ValueError`; handle it when appropriate.
- Use f-strings to combine text and values clearly.
- A conversion does not automatically validate whether an answer is sensible.
