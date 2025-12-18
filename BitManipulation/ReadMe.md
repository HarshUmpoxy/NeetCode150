# Bit Manipulation for Technical Interviews (FAANG)

A crisp, high-yield guide to mastering Bit Manipulation.

## 1. Core Operators

| Operator | Symbol | Description | Example ($A=5 (101), B=3 (011)$) |
| :--- | :---: | :--- | :--- |
| **AND** | `&` | Both bits must be 1 | $5 \& 3 = 1 (001)$ |
| **OR** | `\|` | At least one bit is 1 | $5 \| 3 = 7 (111)$ |
| **XOR** | `^` | Bits must be different | $5 \wedge 3 = 6 (110)$ |
| **NOT** | `~` | Inverts all bits | $\sim 5 = -6$ (Two's complement) |
| **Left Shift** | `<<` | Shift bits left (Multiply by $2^k$) | $5 \ll 1 = 10 (1010)$ |
| **Right Shift** | `>>` | Shift bits right (Divide by $2^k$) | $5 \gg 1 = 2 (0010)$ |

> **Note**: Right shift `>>` is usually arithmetic (preserves sign bit) in Java/C++ for signed integers. Unsigned right shift `>>>` (Java) fills with 0.

---

## 2. Essential Properties & Relations

1.  **XOR Properties** (Critical for "Single Number" problems)
    *   `x ^ 0 = x`
    *   `x ^ x = 0`
    *   `x ^ y = y ^ x` (Commutative)
    *   `(x ^ y) ^ z = x ^ (y ^ z)` (Associative)

2.  **Two's Complement**
    *   `-x = ~x + 1`

3.  **De Morgan's Laws for Bits**
    *   `~(x & y) = ~x | ~y`
    *   `~(x | y) = ~x & ~y`

---

## 3. Common Bit Tricks (The "Cheat Sheet")

Assume `n` is the number and `k` is the bit position (0-indexed from right).

| Operation | Formula | Explanation |
| :--- | :--- | :--- |
| **Check Odd/Even** | `(n & 1) == 0` (Even) | LSB is 0 for even, 1 for odd. Faster than `%`. |
| **Get kth bit** | `(n >> k) & 1` | Shifts target bit to LSB and isolates it. |
| **Set kth bit** | `n | (1 << k)` | OR-ing with 1 forces the bit to 1. |
| **Unset (Clear) kth bit** | `n & ~(1 << k)` | AND-ing with 0 forces the bit to 0. |
| **Toggle kth bit** | `n ^ (1 << k)` | XOR with 1 flips the bit. |
| **Clear lowest set bit** | `n & (n - 1)` | **Crucial**. Removes the rightmost `1`. |
| **Get lowest set bit** | `n & -n` | Isolates the rightmost `1` (e.g., `10110` -> `00010`). |
| **Check Power of 2** | `n > 0 && (n & (n - 1)) == 0` | Powers of 2 have exactly one bit set. |

### Logic Breakdown
1. **Manipulating $k$-th bit**: Create a mask by shifting `1` to position $k$ (`1 << k`).
   - **Set**: **OR** (`|`) forces the bit to `1` (preserves others).
   - **Unset**: **AND** (`&`) with inverted mask (`~`) forces bit to `0`.
   - **Toggle**: **XOR** (`^`) flips the bit (0$\to$1, 1$\to$0).
2. **Rightmost Set Bit**: Subtracting 1 (`n - 1`) flips the rightmost `1` to `0` and all trailing `0`s to `1`s.
   - **Clear**: `n & (n - 1)` removes the rightmost `1`. (Powers of 2 have only one `1`, so this becomes 0).
   - **Isolate**: `n & -n` keeps *only* that rightmost `1`.
     *   **Why?** In Two's Complement, `-n = ~n + 1`.
     *   **Example**: `n = 6` (`00110`).
         1. `~n` reverses bits $\to$ `11001`.
         2. `-n` adds 1 to `~n` $\to$ `11010`.
         3. `n & -n` (`00110 & 11010`) $\to$ `00010`. The `+1` operation "carry" ripples up to the first `0` (which was the original rightmost `1`), aligning it perfectly with `n`.

---

## 4. Key Problem Patterns

### A. Count Set Bits (Hamming Weight)
**Naive**: Loop 32 times.
**Brian Kernighan’s Algorithm** ($O(\text{set bits})$):
Repeatedly clear the lowest set bit until $n$ is 0.
```python
def countSetBits(n):
    count = 0
    while n:
        n &= (n - 1)
        count += 1
    return count
```

### B. Single Number
Given array where every element appears twice except one.
**Logic**: $A \wedge A = 0$. The duplicates cancel out.
```python
def singleNumber(nums):
    res = 0
    for n in nums:
        res ^= n
    return res
```

### C. Missing Number
Array `[0, n]` missing one number.
**Logic**: XOR all indices `[0, n]` and all values `nums[i]`. Result is the missing number.
```python
def missingNumber(nums):
    res = len(nums)
    for i in range(len(nums)):
        res ^= i ^ nums[i]
    return res
```

### D. Swap Two Numbers (No Temp Var)
```python
a = a ^ b
b = a ^ b  # (a ^ b) ^ b = a
a = a ^ b  # (a ^ b) ^ a = b
```

### E. Range XOR
Compute XOR of all numbers from $0$ to $n$ (`0 ^ 1 ^ ... ^ n`) in $O(1)$.
The cumulative XOR repeats in a cycle of 4 based on `n % 4`.

| n % 4 | XOR(0..n) Result | Why? (Logic trace) |
| :--- | :--- | :--- |
| **0** | `n` | Cycle resets. |
| **1** | `1` | Previous was `n` (even). `n ^ (n+1) = 1`. |
| **2** | `n + 1` | Previous was `1`. `1 ^ n` (where `n` is even) $\to$ `n + 1`. |
| **3** | `0` | Previous was `n`. `n ^ n = 0`. |

**Why `2 -> n + 1`?**
If `n % 4 == 2`, then the previous term `XOR(0..n-1)` was `1`.
So `XOR(0..n) = 1 ^ n`. Since `n` is even (e.g., `2, 6, 10`), its LSB is `0`. `1 ^ n` simply flips the LSB to `1`, resulting in `n + 1`.

**Why `3 -> 0`?**
If `n % 4 == 3`, then the previous term `XOR(0..n-1)` was `n` (actually `(n-1) + 1`, which equals `n`).
So `XOR(0..n) = n ^ n`, which is always `0`.

**Formula**:
```python
def getXOR(n):
    rem = n % 4
    if rem == 0: return n
    if rem == 1: return 1
    if rem == 2: return n + 1
    if rem == 3: return 0
```
Use this to find XOR range $[L, R]$ as `getXOR(R) ^ getXOR(L-1)`.

### F. Reverse Bits / Reverse Integer
Iterate and build the result.
```python
def reverseBits(n):
    res = 0
    for _ in range(32):
        res = (res << 1) | (n & 1)
        n >>= 1
    return res
```

---

## 5. Advanced Applications

*   **Subsets (Power Set)**: Iterate from $0$ to $2^n - 1$. If $j$-th bit of $i$ is set, include `nums[j]`.
*   **Bitmask DP**: Used when $N$ is small ($N \le 20$).
    *   **Key Idea**: Use an integer `mask` as a compact boolean array. If the $i$-th bit is `1`, it means item $i$ is "visited" or "in set".
    *   **Complexity**: $2^N$ states. (Since $2^{20} \approx 10^6$, this fits within time limits).
    *   **Example (TSP)**: State is `(mask, last_visited_city)`.
        *   `mask = 5` (`101` binary) $\to$ Cities 0 and 2 visited.
        *   Transition: Try visiting separate unvisited city $j$ if `(mask >> j) & 1 == 0`.
