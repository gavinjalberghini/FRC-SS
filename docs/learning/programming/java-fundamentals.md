---
layout: lesson
title: Java Fundamentals
subtitle: A self-paced Java course, from syntax to inheritance, built around 17 hands-on exercises.
permalink: /learning/programming/java-fundamentals/
role: programmer
order: 3
size: 3
time: "Self-paced (multi-week)"
---

## Overview

Robot code is written in Java, so every programmer needs a solid Java
foundation. This lesson is a self-paced course organized into 20 units. Read
each topic, try the examples, and complete the exercise(s) before moving on —
the exercises are where the learning sticks.

Work through the units **in order**; each one assumes the previous ones.

## Prerequisites

- A computer with a Java Development Kit (JDK) installed.
- A code editor (VS Code is recommended; it's also what we use for robot code).

## How to work through it

- [ ] Read the topics in a unit, typing out the examples yourself.
- [ ] Complete each exercise in its own `.java` file and run it.
- [ ] Commit your work to your **own** learning repository (the one you created in
      the [Git lesson](../git/)) on a branch, and push it.
- [ ] Ask for help when you get stuck — after you've tried and can describe what
      you attempted.

## Unit 1 — Getting started

After setting up your JDK and editor, the first thing to understand is how a Java
program runs. **Every Java program begins executing at a `main` method**, and runs
each line in order, top to bottom, starting from the first line of `main`.

```java
public class Main {
  public static void main(String[] args) {
    System.out.println("Hello, robot!"); // runs first
    System.out.println("Goodbye!");      // runs second
  }
}
```

A few syntax rules to internalize now, because they apply everywhere:

- Java is **case-sensitive** — `test` and `Test` are two different names.
- Every statement ends in a **semicolon** `;`.
- Variable and method names use **camelCase**: the first word is lowercase and
  later words are capitalized with no spaces, like `variableName`.
- **Curly braces** `{}` group related code into blocks.
- **Comments** are ignored when the program runs: `// a single line`, or a block
  bookended by `/*` and `*/`.

## Unit 2 — Variables, types & operators

Data is stored in **variables**, and every variable has a **type**. Java's basic
("primitive") types are:

- `int` — whole numbers
- `double` — decimal numbers
- `boolean` — `true` / `false`
- `char` — a single character, like `'a'`
- (`long`, `short`, `byte`, `float` exist too, but you'll rarely need them.)

Making a variable has two steps. **Declaration** states the type and name;
**initialization** assigns a starting value. They can be combined on one line:

```java
int count;            // declaration
count = 5;            // initialization
double speed = 0.5;   // declaration + initialization together
```

A **constant** is a variable declared with `final` — once initialized it can never
change. By convention constants are named in `ALL_CAPS` with underscores:

```java
final double WHEEL_DIAMETER_INCHES = 6.0;
```

The basic math operators (`+ - * /`) follow normal order of operations. Watch out:
**dividing two integers rounds down** (`7 / 2` is `3`). The modulo operator `%`
gives the remainder (`7 % 2` is `1`), and `++` / `--` increase or decrease a value
by one.

A single equals `=` is the **assignment** operator (make the left side equal the
right). Two equals `==` is the **equality check** (is the left equal to the right?):

```java
int x = 5 + 5;             // x becomes 10
boolean isTen = (x == 10); // true
```

You can combine math with assignment: `x += 1` is shorthand for `x = x + 1`.
Remember that plain math operators don't change a variable unless you also assign
the result back to it.

**Exercise 1 — Quarters.** Three friends share 65 quarters. Write a program that
prints: the total value of all quarters; how many are left over after an equal
split; the value of one friend's pile (excluding leftovers); the value if one
friend gives their pile to another; and the new total after the leftovers are
added in.

## Unit 3 — Booleans & decisions

Java enforces **type safety**: if you try to put a value of one type into a
variable of an incompatible type, the code won't compile. This catches mistakes
early.

To make decisions, you build **boolean expressions** — statements that evaluate to
`true` or `false` — using:

- **Logical operators:** `!` (NOT, reverses true/false), `&&` (AND, true only if
  both sides are true), `||` (OR, true if either side is true), and `!=` (not equal).
- **Relational operators:** `<`, `>`, `<=`, `>=`.

An **`if` statement** runs a block only when its condition is true. If you omit the
braces, only the single line immediately after the condition is included:

```java
if (speed > 0.5) {
  System.out.println("Going fast!");
}
```

An **`else`** block runs when the `if` condition is false. `if`/`else` statements
can be **nested** inside one another — keep paired braces at the same indentation
so you can see where each block begins and ends:

```java
if (isEnabled) {
  if (speed > 0.5) {
    System.out.println("Fast and enabled");
  } else {
    System.out.println("Slow but enabled");
  }
} else {
  System.out.println("Disabled");
}
```

**Exercise 2 — Leap year.** Write a program that determines whether a given year
is a leap year (divisible by 4, except century years, which must be divisible by
400).

## Unit 4 — Switch statements

When you'd otherwise write a long chain of `if`/`else` comparisons against one
value, a **`switch`** statement is cleaner. It evaluates an expression and jumps to
the matching `case` label. A `break` exits the switch; without it, execution "falls
through" into the next case. The `default` case runs when nothing matches.

```java
switch (gear) {
  case 1:
    System.out.println("Low gear");
    break;
  case 2:
    System.out.println("High gear");
    break;
  default:
    System.out.println("Neutral");
}
```

**Exercise 3 — Switch refactor.** Rewrite a small if/else program so it produces
the same output using a `switch` statement instead.

## Unit 5 — Scope & errors

**Scope** is the part of a program from which something is accessible. Scope is
defined by curly braces `{}`: anything declared inside a set of braces is visible
within those braces (including nested ones), but **not outside** them. So a variable
declared inside an `if` statement can't be used after that `if` ends.

When execution leaves a scope (the end of a loop, `if`, or method), the references
created in that scope are removed. Any object no longer referenced is automatically
cleaned up by **garbage collection** — you don't free memory manually in Java.

It helps to distinguish two kinds of bugs:

- A **syntax error** breaks the rules of the language and won't compile — for
  example, a missing semicolon or using a variable that was never declared.
- A **logic error** compiles and runs but produces the wrong result or behavior —
  like a calculator that says `2 + 2 = 5`, or a robot that drives backward when
  told to go forward.

## Unit 6 — Arrays

An **array** holds a fixed number of values of the **same type**. The type is the
element type followed by `[]`, e.g. `int[]`. You access an element by its **index**
(its offset from the start), and **indexes start at 0**. Reading past the end of the
array throws an `IndexOutOfBoundsException`.

```java
int[] scores = {10, 20, 30}; // initialize with values
int first = scores[0];       // 10  (index 0 is the first element)
scores[1] = 25;              // change the second element

String[] names = new String[3]; // an empty array of length 3
```

**Exercise 4 — Pet store inventory.** Use two arrays (animal names and counts) to
print a store's inventory, then replace one animal with another and re-print.

## Unit 7 — Loops

A **`while` loop** repeats its block as long as a condition is true. The condition
is checked **before** each pass, so if it's false to begin with, the body never
runs. Make sure the condition can eventually become false, or you'll create an
**infinite loop**:

```java
int i = 0;
while (i < 5) {
  System.out.println(i);
  i++; // without this, the loop never ends
}
```

A **`for` loop** is essentially a `while` loop with a built-in counter. Use it when
you know how many times you want to repeat. Its header has three parts:
initialization, a termination condition, and an increment:

```java
for (int i = 0; i < 5; i++) {
  System.out.println(i);
}
```

A **for-each loop** is shorthand for iterating over every element of an array (or
other iterable, like an `ArrayList`):

```java
int[] values = {3, 5, 8};
int sum = 0;
for (int v : values) {
  sum += v;
}
```

**Exercise 5 — Loops + inventory.** Redo Exercise 4 using a `while` loop to print
the first inventory and a `for` loop to print the second — no more than one print
statement per loop.

## Unit 8 — Generics & ArrayList

A **generic type** lets a class work with a type that's specified later, when an
object is created, instead of being fixed in advance. Generic types are written in
diamond braces `<>`.

The most common use is **`ArrayList`**, a resizable cousin of the array with many
helpful methods. It must be imported, and it uses a generic type to say what it
holds (one type per list):

```java
import java.util.ArrayList;

ArrayList<Double> readings = new ArrayList<>();
readings.add(4.3);          // append
readings.add(27.8);
readings.add(1, 5.5);       // insert at index 1
double first = readings.get(0);
readings.remove(0);         // remove by index
int howMany = readings.size();
```

Useful `ArrayList` methods include `add`, `add(index, element)`, `remove(index)`,
`remove(object)`, `get(index)`, `set(index, element)`, `size()`, `indexOf(object)`,
and `contains(object)`.

**Exercise 6 — ArrayList.** Create an `ArrayList` of doubles, add several values,
insert one between two existing values, remove one, replace one, then print every
element with a for-each loop.

**Practice problems.** For extra reps: fill an `int` array, print it with a `for`,
`while`, and `for-each` loop, then copy the values into an `ArrayList`, add one
more, and print again.

## Unit 9 — Methods

A **method** is a named sequence of code that performs one operation and can be
called from elsewhere — this is how you avoid copying the same code in many places.
Each method has a **signature** describing its visibility, return type, name, and
parameters (inputs).

There are three **visibility** modifiers: `public` (visible to anyone), `private`
(only within the same class), and `protected` (this class and its subclasses). The
**return type** can be any type; if a method returns nothing, its return type is
`void`. Parameters are listed as comma-separated values in parentheses, like the
inputs to a math function `f(x, y)`.

```java
// public, returns a double, named "average", takes two doubles
public double average(double a, double b) {
  return (a + b) / 2;
}
```

**Exercise 7 — Methods.** Write methods that take three integers and return the
smallest, the largest, and the average; plus one that prints all three and
returns nothing. Call them from `main`. (Add `static` after `public` since they're
in the main class.)

## Unit 10 — Recursion

**Recursion** is when a method calls itself. It's a way to break a complicated
problem into smaller, simpler versions of the same problem. Every recursive method
needs a **base case** — a condition where it stops calling itself and returns —
otherwise it recurses forever (the recursion equivalent of an infinite loop).

```java
public int factorial(int n) {
  if (n <= 1) {
    return 1;           // base case: stop here
  }
  return n * factorial(n - 1); // recursive case
}
```

**Exercise 8 — Factorial.** Write a recursive method that computes the factorial
of an integer, and use it to print 12!.

## Unit 11 — Exceptions (intro)

An **exception** is an event that disrupts normal execution at runtime. When code
"throws" an exception, information about what went wrong (its type and location) is
passed up to the surrounding code. Exceptions exist to stop undefined or dangerous
behavior, like using a `null` value or dividing by zero.

Common exceptions you'll meet:

- `NullPointerException` — using an object that is `null` (never initialized).
- `ArithmeticException` — an illegal math operation, like integer divide-by-zero.
- `IllegalArgumentException` — a method was called with invalid input.
- `IllegalStateException` — a method was called before its prerequisites were met.
- `IOException` — an input/output operation failed.

## Unit 12 — Objects, classes & Strings

A **class** describes a *type* of thing; an **object** is a specific *instance* of
that class. "Book" is a class; the particular book on your desk is an object. A
class can hold **fields** (variables/objects) and **methods**. By convention class
names are Capitalized and object names use camelCase.

You create an object with the `new` keyword, which calls the class's
**constructor** (a special method that shares the class's name and has no return
type):

```java
String name = new String("Ada");
String nickname = "Ada"; // a "string literal" — shorthand for the above
```

When comparing objects, be careful: `==` compares **memory addresses** (are these
the exact same object?), while `.equals()` compares **values** (are these
equivalent?). For text, almost always use `.equals()`.

A **`String`** is a sequence of characters. The `+` operator **concatenates**
(joins) strings, and `+=` joins-and-assigns. The `String` class has many useful
methods, including:

- `length()` — number of characters
- `charAt(index)` — the character at a position (starting at 0)
- `toUpperCase()` / `toLowerCase()`
- `substring(begin, end)` — a piece of the string
- `contains(text)` — is this text inside the string?
- `split(separator)` — break the string into an array of pieces
- `compareToIgnoreCase(other)` — compare ignoring upper/lowercase

```java
String sentence = "The quick brown fox";
int len = sentence.length();              // 19
String[] words = sentence.split(" ");     // ["The", "quick", "brown", "fox"]
```

**Exercise 9 — Strings.** Given a sentence, print its length, print a substring,
compare it (ignoring case) to another sentence, then `split` it on spaces and
print the number of words.

## Unit 13 — Input with Scanner

Java classes are organized into **packages**. To use a class from another package
you must **import** it (the `java.lang` package, which has `String`, `Math`, etc.,
is always available). The **`Scanner`** class reads a source of data as text —
useful for reading user input from the command line:

```java
import java.util.Scanner;

Scanner scanner = new Scanner(System.in); // read from the keyboard
System.out.print("Enter a number: ");
int n = Integer.parseInt(scanner.nextLine());
scanner.close(); // always close a Scanner when done
```

A `Scanner` breaks its input into **tokens** separated by a **delimiter**
(whitespace by default). Key methods are `hasNext()`, `next()`, and `nextLine()`.
Always call `close()` when finished — I/O objects use operating-system resources
that aren't reliably garbage-collected, and failing to close them leaks resources.

**Exercise 10 — Running average.** Read positive integers from user input into an
`ArrayList` until a negative number is entered, then print the average (don't
store the negative number).

## Unit 14 — Writing classes

So far you've used classes; now you'll write your own. A class is the **blueprint**
from which objects are created with `new`. Class names start with an uppercase
letter. A class contains **class-level variables** (fields), a **constructor**, and
**methods**.

Fields declared at the class level are in scope anywhere in the class. If you make
a field `public`, other classes can read/write it through an instance — which is
often *not* what you want. Making fields `private` and providing **get/set
methods** lets you control access to your data.

A **constructor** runs when you create an object with `new`. Like methods it can be
overloaded, but it has no return type. Constructors commonly initialize fields from
parameters:

```java
public class Motor {
  private String name;   // private field
  private int port;

  public Motor(String name, int port) { // constructor
    this.name = name;
    this.port = port;
  }

  public String getName() { // get method controls read access
    return name;
  }
}
```

**Exercise 11 — Custom classes.** Implement two small classes (for example, a
`Holiday` and a `Movie`) with fields, a constructor, and methods, and exercise
them from a `main` method.

## Unit 15 — Enums

An **enum** type is a special type whose value must be one of a fixed set of named
constants. Common examples are compass directions or days of the week. Because the
values are constants, they're named in `ALL_CAPS`. Use an enum whenever you have a
known, fixed set of choices (menu options, robot states, command flags, etc.):

```java
public enum Direction {
  NORTH, SOUTH, EAST, WEST
}

Direction heading = Direction.NORTH;
```

**Exercise 12 — Enums.** Refactor a program that uses integers to represent a
fixed set of choices so it uses an `enum` instead.

## Unit 16 — Exceptions & try/catch

Sometimes *you* want to throw an exception — most often when a **precondition**
isn't met or a **postcondition** can't be satisfied. You throw one with the `throw`
keyword:

```java
if (speed < 0) {
  throw new IllegalArgumentException("speed must not be negative");
}
```

To keep your program running even when an exception occurs, wrap risky code in a
**`try`/`catch`** block. If the `try` block throws, execution jumps to the `catch`
block instead of crashing:

```java
try {
  int value = myNumbers[10]; // might be out of bounds
} catch (IndexOutOfBoundsException e) {
  System.out.println("Something went wrong, but we kept running.");
}
```

**Exercise 13 — Try/catch.** Starting from code that throws an exception partway
through, add handling so that every print statement still runs.

## Unit 17 — The `static` modifier

By default, fields and methods belong to an **object**, so you need an instance to
use them. The **`static`** modifier makes a field/method belong to the **class
itself**, so it can be used without creating an object — and there's only ever one
copy of a static field, shared across all instances.

```java
double r = Math.random(); // Math is a class; random() is a static method
```

A static field shared across all instances is handy for things like a counter that
assigns each new object a unique ID.

**Exercise 14 — President.** Create a `President` class with a constructor and a
private `static boolean inOffice` that ensures only one `President` object can be
fully created. Add a `static` method that prints a message, and call it from `main`.

## Unit 18 — Nested classes

Java lets you define a class **inside** another class — a **nested class**. A nested
class can be static or non-static:

- A **static** nested class can be instantiated without an instance of the outer
  class, and can only access the outer class's static members.
- A **non-static** nested class requires an instance of the outer class first, and
  can access all of the outer class's members.

**Exercise 15 — Outer/inner classes.** Create an `OuterClass` with private fields
and a static `multiplier`. Add a non-static inner class whose method prints the
fields times the multiplier, and a static inner class that changes the multiplier.
Demonstrate the behavior before and after changing it.

## Unit 19 — Inheritance

**Inheritance** lets one class reuse another's data and methods. A **subclass**
(child) `extends` a **superclass** (parent), inheriting its fields and methods and
adding its own. The subclass can use the superclass's members, but **not** the other
way around — a parent can't see its child's additions.

```java
public class Vehicle {
  String brand;
}

public class Car extends Vehicle { // Car inherits "brand" from Vehicle
  String model;
}
```

**Exercise 16 — Vehicles.** Create a `Vehicle` superclass and `Car` / `Airplane`
subclasses that each add their own field and set a `mode`. Construct one of each
and print all of their values.

## Unit 20 — Documentation

Good code is documented in three complementary ways — ideally you keep all three
up to date:

- **READMEs** — Markdown files (`.md`) that explain *what* the program is and how to
  use it. Anyone, even a non-programmer, should be able to read it.
- **JavaDocs** — generated documentation describing *what* each class, method, and
  field is for. Special `/** ... */` comments are turned into browsable HTML by the
  `javadoc` command (e.g. `javadoc -d myDoc src/*`).
- **Code comments** — plain comments in the code explaining *how* it works to other
  developers.

**Exercise 17 — Document it.** Take your Exercise 16 solution and add code
comments (noting which class each field comes from) plus a generated JavaDoc that
explains each class and constructor.

## Resources

- [WPILib: Java/C++ installation & setup](https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-2/index.html)
- [Official Java Tutorials (Oracle)](https://docs.oracle.com/javase/tutorial/)
- [Java SE API documentation](https://docs.oracle.com/en/java/javase/17/docs/api/index.html)
- [Stack Overflow](https://stackoverflow.com/) — for troubleshooting specific errors.

## Notes

- Don't rush. It's better to truly understand Units 1–8 than to skim all 20.
- Keep your exercise solutions in version control — they make a great reference
  later, and reviewing them is good practice for code review.
