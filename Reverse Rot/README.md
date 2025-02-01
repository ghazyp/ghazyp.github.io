# Reverse Rot

## Problem Statement
**Reverse Rot** is a text encoding scheme that first **reverses** a given string and then performs a **rotation** on its characters using a predefined order. This scheme is an extension of the classic ROT13 cipher.

### **Character Rotation Order**:
```
ABCDEFGHIJKLMNOPQRSTUVWXYZ_.
```
- **Underscore (`_`) follows `Z`**, and the **period (`.`) follows `_`**.
- A forward rotation of `1` means:
  - `'A' → 'B'`, `'B' → 'C'`, ..., `'Z' → '_'`, `'.' → 'A'`
  - Similarly, a rotation of `N` shifts each character forward by `N` places in this order.

## Input Format
- Each input line consists of an **integer `N`** (rotation amount) followed by a **string**.
- `N` is between `1` and `27`.
- The string consists of **1 to 40 characters**, including only:
  - **Capital letters (`A-Z`)**
  - **Underscores (`_`)**
  - **Periods (`.`)**
- The last line of input contains only the number `0`, indicating the end of input.

## Output Format
- For each test case, output the **encoded string** after applying:
  1. **Reversal** of the original string.
  2. **Rotation** of each character by `N` positions.

## Example

### **Sample Input**
```
1 ABCD
3 YO_THERE.
1 .DOT
14 ROAD
9 SHIFTING_AND_ROTATING_IS_NOT_ENCRYPTING
2 STRING_TO_BE_CONVERTED
1 SNQZDRQDUDQ
0
```

### **Sample Output**
```
EDCB
CHUHKWBR.
UPEA
ROAD
PWRAYF_LWNHAXWH.RHPWRAJAX_HMWJHPWRAORQ.
FGVTGXPQEAGDAQVAIPKTVU
REVERSE_ROT
```

## Implementation Notes
- **Reverse the input string** before applying the rotation.
- **Use a lookup table or modular arithmetic** to handle character shifts efficiently.
- **Stop processing when `0` is encountered as the input line.**

## License
This problem is sourced from **ACM Mid-Central Programming Competition 2014** and is used for educational purposes.

