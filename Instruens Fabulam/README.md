# Instruens Fabulam

## Description
**Instruens Fabulam** (Latin for "Drawing a Chart") is a programming challenge where you must format and display tables according to specific rules. Given structured input, your task is to output a properly formatted table using ASCII characters.

## Problem Statement
The input consists of one or more table descriptions, followed by a line whose first character is `*`, signaling the end of input. Each table description includes:

- A **header line** defining the number and alignment of columns using:
  - `<` for left-justified
  - `=` for centered
  - `>` for right-justified
- At least **two and at most 21 data lines**, where:
  - Entries are separated by `&`
  - The first row represents column titles
  - Remaining rows represent the table body
- **Restrictions:**
  - No leading or trailing spaces in entries
  - Only spaces (no tabs) are used in formatting
  - The characters `<`, `=`, `>`, `&`, and `*` appear only in their specified roles

## Input Format
```
<>=>
TITLE&VERSION&OPERATING SYSTEM&PRICE
Slug Farm&2.0&FreeBSD&49.99
Figs of Doom&1.7&Linux&9.98
Smiley Goes to Happy Town&11.0&Windows&129.25
Wheelbarrow Motocross&1.0&BeOS&34.97
>
What is the answer?
42
<>
Tweedledum&Tweedledee
"Knock, knock."&"Who's there?"
"Boo."&"Boo who?"
"Don't cry, it's only me."&(groan)
*
```

## Output Format
```
@-----------------------------------------------------------------@
| TITLE                     | VERSION | OPERATING SYSTEM |  PRICE |
|---------------------------+---------+------------------+--------|
| Slug Farm                 |     2.0 |     FreeBSD      |  49.99 |
| Figs of Doom              |     1.7 |      Linux       |   9.98 |
| Smiley Goes to Happy Town |    11.0 |     Windows      | 129.25 |
| Wheelbarrow Motocross     |     1.0 |       BeOS       |  34.97 |
@-----------------------------------------------------------------@
@---------------------@
| What is the answer? |
|---------------------|
|                  42 |
@---------------------@
@---------------------------------------------@
| Tweedledum                 |     Tweedledee |
|----------------------------+----------------|
| "Knock, knock."            | "Who's there?" |
| "Boo."                     |     "Boo who?" |
| "Don't cry, it's only me." |        (groan) |
@---------------------------------------------@
```
## Implementation Details
- The total table width does not exceed **79 characters** (excluding newlines).
- **Dashes (`-`)** are used for horizontal lines, never underscores.
- **`@`** characters mark the table corners.
- **`+`** characters appear at intersections in the horizontal separator.
- The **widest entry** in each column determines its width.
- **Centered entries** have extra space placed **on the right** if uneven.

## Solution Approach
1. **Parse Input:** Read the header line to determine column count and alignment.
2. **Process Data Lines:** Store each row while tracking column widths.
3. **Format Output:** Construct table borders, titles, and body using the required characters.
4. **Print Table:** Ensure correct spacing and justification.

## Running the Program
- The source file should be named **fab.c**, **fab.cpp**, **fab.java**, or **fab.pas**.
- It reads from `fab.in` and writes to `fab.out`.

## License
This challenge is derived from an ACM programming competition problem and is for educational purposes only.

