# Documentation

The Math Bot is a text-based bot. Currently, it only accepts text commands in a certain syntax and returns string outputs in replies. If needed, we can add the capability to generate graphs as well, but currently only text output is supported.

> **NOTE:** Undocumented functions are planned but not implemented yet.

## General Syntax

There is a **trigger prefix** that activates the bot and causes it to start processing commands. Ask your server's moderator or other users for the trigger prefix. Generally, it is `$mathbot` if the variables in the [main.py](mathbot/main.py) have not been changed.

The commands are written as:

```
<trigger> <command> [arg1 arg2 ...]
```

For example:

```
$mathbot mean 1 2 3 4
$mathbot var 10 30 30 14 1 6 25
$mathbot uniform
$mathbot flip 20
...
```

A command can have 0 or more arguments and it varies.

## Simulation Functions

These functions can be used to generate 1 random variate or a list of random variates. In order to stay under the 2000 character limit imposed by Discord's API, the maximum number of variates to be generated is limited to **250**. This can be changed in the [main.py](mathbot/main.py), but it is recommended to keep this value.

### Uniform

**Command string(s)**: `uniform`

**Description**: The variates are sampled from a uniform distribution with the lower limit inclusive and the upper limit exclusive. Floating point values are generated.

| Arguments                       | Explanation                                           | Example                     |
| ------------------------------- | ----------------------------------------------------- | --------------------------- |
| None                            | Return 1 uniform variate from `[0, 1)`                | `$mathbot uniform`          |
| **count**                       | Return `count` uniform variates from `[0, 1)`         | `$mathbot uniform 10`       |
| **upper**, **count**            | Return `count` uniform variates from `[0, upper)`     | `$mathbot uniform 12.5 10`  |
| **lower**, **upper**, **count** | Return `count` uniform variates from `[lower, upper)` | `$mathbot uniform -2 +2 10` |

| Argument | Type             |
| -------- | ---------------- |
| count    | positive integer |
| upper    | float            |
| lower    | float            |

Note that the bot is robust enough to sample from `[upper, 0)` if `upper` is negative. It can also exchange the values of `lower` and `upper` to ensure `lower < upper`.

### Bernoulli

**Command string(s)**: `flip`, `bernoulli`

**Description**: Returns the result of performing Bernoulli trials (like coin flips) with the specified probability (or 50% by default) of success (i.e. 1). Success is returned as 1 and failure is returned as 0.

| Arguments        | Explanation                                                             | Example                |
| ---------------- | ----------------------------------------------------------------------- | ---------------------- |
| None             | Return the result of one coin flip                                      | `$mathbot flip`        |
| **count**        | Return the result of `count` coin flips with 50% probability of success | `$mathbot flip 10`     |
| **p**, **count** | Return the result of `count` coin flips with probability `p` of success | `$mathbot flip 0.8 10` |

| Argument | Type             |
| -------- | ---------------- |
| count    | positive integer |
| p        | positive float   |

Note that `p` is normalized to be in the range `[0, 1)`. Hence a value of `50` gets converted to `0.5`, `2.5` gets converted to `0.25` and so on. The divisor is the least power of 10 greater than the number.

### Binomial

**Command string(s)**: `nflip`, `binom`, `binomial`

**Description**: Returns the result of performing binomial trials with parameters `n`, and `p`, or `n` Bernoulli trials (like coin flips) at once with the specified probability `p` (or 50% by default) of success (i.e. 1) for each individual trial (flip). The total number of successful trials is returned as an integer.

| Arguments        | Explanation                                                             | Example                |
| ---------------- | ----------------------------------------------------------------------- | ---------------------- |
| None             | Return the result of one coin flip                                      | `$mathbot flip`        |
| **count**        | Return the result of `count` coin flips with 50% probability of success | `$mathbot flip 10`     |
| **p**, **count** | Return the result of `count` coin flips with probability `p` of success | `$mathbot flip 0.8 10` |

| Argument | Type             |
| -------- | ---------------- |
| count    | positive integer |
| p        | positive float   |

As in the case with Bernoulli trials, `p` is normalized.

### Normal

**Command string(s)**: `normal`, `gauss`, `gaussian`

**Description**: Returns normally distributed Gaussian variates. The default variates have a mean of 0 and a standard deviation of 1.

| Arguments                    | Explanation                                                | Example                    |
| ---------------------------- | ---------------------------------------------------------- | -------------------------- |
| None                         | Returns one standard normal variate.                       | `$mathbot gauss`           |
| **count**                    | Returns `count` standard normal variates.                  | `$mathbot gauss 10`        |
| **sigma**, **count**         | Returns `count` variates with mean of 0 and stdev `sigma`. | `$mathbot gauss 2.5 40`    |
| **mu**, **sigma**, **count** | Returns `count` variates with mean `mu` and stdev `sigma`. | `$mathbot gauss 20 0.2 10` |

| Argument | Type             |
| -------- | ---------------- |
| count    | positive integer |
| sigma    | positive float   |
| mu       | float            |

### Exponential

**Command string(s)**: `exp`, `exponential`, `poisson`

**Description**: Returns exponentially distributed Poisson variates.

| Arguments             | Explanation                                                   | Example                   |
| --------------------- | ------------------------------------------------------------- | ------------------------- |
| **lambda**            | Returns 1 exponential variate with parameter `lambda`.        | `$mathbot poisson 10`     |
| **lambda**, **count** | Returns `count` exponential variates with parameter `lambda`. | `$mathbot poisson 2.5 40` |

| Argument | Type              |
| -------- | ----------------- |
| count    | positive integer  |
| lambda   | nonnegative float |

## Statistics Functions

These functions take a list of **real valued** (float) arguments and return the desired statistics about them.

### Mean

**Command strings**: `mean`, `avg`, `average`

**Description**: Returns the arithmetic mean of the given arguments.

**Minimum arguments**: 1

**Example**:

```
$mathbot mean 10 24 14 5 6 34 24 25
```

### Median

**Command strings**: `median`

**Description**: Returns the median of the given arguments.

**Minimum arguments**: 1

**Example**:

```
$mathbot median 8 5 9 4 2 7 9 6 4 3 6 8 4
```

### Mode

**Command strings**: `mode`

**Description**: Returns the mode of the given arguments.

**Minimum arguments**: 1

**Example**:

```
$mathbot mode 3 3 6 6 4 2 6 7 4 3 6 8 7 5 3 3 6 7
```

### Variance

**Command strings**: `var`, `variance`

**Description**: Returns the sample variance of the given arguments.

**Minimum arguments**: 2

**Example**:

```
$mathbot var 350 252 525 314 145 252
```

### Standard Deviation

**Command strings**: `stdev`, `stddev`, `standard-deviation`

**Description**: Returns the sample standard deviation of the given arguments.

**Minimum arguments**: 2

**Example**:

```
$mathbot var 1 5 6 3 6 3 6 7 3 1
```

### Population Variance

**Command strings**: `pvar`, `pvariance`, `population-variance`

**Description**: Returns the population variance of the given arguments.

**Minimum arguments**: 1

**Example**:

```
$mathbot pvar 350 252 525 314 145 252
```

### Population Standard Deviation

**Command strings**: `pstdev`, `pstddev`, `population-standard-deviation`

**Description**: Returns the population standard deviation of the given arguments.

**Minimum arguments**: 1

**Example**:

```
$mathbot var 1 5 6 3 6 3 6 7 3 1
```

## Utility Functions

## Range

**Command strings**: `range`, `loop`

**Description**: Returns a list of integers from the smallest to the largest. Both limits are inclusive.

| Arguments           | Explanation                              | Example               |
| ------------------- | ---------------------------------------- | --------------------- |
| **limit**           | Returns integers from 1 to `limit`.      | `$mathbot loop 10`    |
| **start**, **stop** | Returns integers from `start` to `stop`. | `$mathbot loop 20 35` |

| Argument | Type                                 |
| -------- | ------------------------------------ |
| limit    | integer with abs value less than 250 |
| start    | integer with abs value less than 250 |
| stop     | integer with abs value less than 250 |

Note that if `start` > `stop`, a descending range is returned.

### Sum

**Commands strings**: `sum`

**Description**: Returns the sum of the numeric arguments (floats).

**Minimum arguments**: 1

**Example**:

```
$mathbot sum 10 12 30 12 10 0 1 30
```

### Sort

#### Ascending Order

**Command strings**: `sort`

**Description**: Returns a sorted list of the given arguments in ascending order. The strings are sorted alphabetically.

**Minimum arguments**: 1

**Example**:

```
$mathbot sort this can sort strings of words as well
```

#### Descending Order

**Command strings**: `dsort`

**Description**: Returns a sorted list of the given arguments in descending order. The strings are sorted alphabetically but in reverse.

**Minimum arguments**: 1

**Example**:

```
$mathbot dsort this can sort strings of words as well
```

### Shuffle

**Command strings**: `mix`, `shuffle`

**Description**: Shuffles the given list of arguments.

**Minimum arguments**: 1

**Example**:

```
$mathbot mix one two three four five
```

### Reverse

**Command strings**: `reverse`

**Description**: Reverses the given list of argument.

**Minimum arguments**: 1

**Example**:

```
$mathbot reverse one two three four five
```

### Sample

**Command strings**: `sample`, `draw`

**Description**: Randomly samples the required number items from the list provided without replacement.

**Syntax**:

```
$mathbot draw <count> [item1 item2 item3 ...]
```

Here **count** should be less than the number of items provided. If not, the entire list is shuffled and returned.

**Example**:

```
$mathbot draw 3 sam roy jean joy bill
```

### Choose

**Command strings**: `choose`, `pick`

**Description**: Randomly selects the required number of items from the list without replacement. Can have repeats.

**Syntax**:

```
$mathbot choose <count> [item1 item2 item3 ...]
```

The **count** can be any positive integer (within the generator limit).

**Example**:

```
$mathbot choose 10 sam roy jean joy bill
```
