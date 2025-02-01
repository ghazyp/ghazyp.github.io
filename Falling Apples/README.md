# Falling Apples

## Problem Statement
You are given a **2D rectangular grid** where each cell contains either an apple (`a`), an obstacle (`#`), or is empty (`.`). The goal is to simulate **gravity** such that all apples fall to their final positions.

### **Gravity Rules**:
1. **Obstacles (`#`) do not move**.
2. **Whenever an empty cell (`.`) is immediately below an apple (`a`), the apple moves down into the empty cell**.

Your task is to print the final configuration of the board after all apples reach their lowest possible positions.

## Input Format
- The first line contains two integers, `R` and `C`, representing the **number of rows** and **columns** of the grid.
  - `1 ≤ R ≤ 50,000`
  - `1 ≤ C ≤ 10`
- The next `R` lines each contain a string of length `C`, representing the grid.
  - Each character is either:
    - `.` (empty space)
    - `a` (apple)
    - `#` (obstacle)

## Output Format
- Print **R lines**, representing the final state of the grid after all apples have fallen.

## Examples

### **Sample Input 1**
```
10 10
..a.......
..a.......
..a.......
....a.....
..........
..#.a.....
..........
.....a....
..#....a..
..........
```

### **Sample Output 1**
```
..........
..........
..a.......
..a.......
..a.......
..#.......
..........
..........
..#.a.....
....aa.a..
```

### **Sample Input 2**
```
4 5
aaa.a
aa.a.
a.a..
...a.
```

### **Sample Output 2**
```
.....
a....
aaaa.
aaaaa
```

## Implementation Notes
- **Efficiency is key** due to constraints where `R` can be as large as **50,000**.
- **Avoid naive simulation**, iterating step by step, as it may be too slow for large inputs.
- Instead, process **each column independently** from bottom to top, shifting apples downward efficiently.

## License
This problem is sourced from **ACM-ICPC 2016 Mid-Central Regional Problem B: Falling Apples** and is used for educational purposes.

