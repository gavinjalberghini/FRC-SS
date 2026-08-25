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

## Description

FRC robot code is Java. Not "Java-ish," not a special robot dialect — the same
language you will see in Oracle's tutorials and in every WPILib example. If a
variable, a loop, or a class is fuzzy, every later ticket (hardware bring-up,
command bindings, autonomous) turns into guesswork on top of guesswork. This
ticket exists so the rest of the programmer and veteran tracks have something
solid to stand on.

This is a course, not a weekend skim. Twenty units, seventeen exercises. Read
each topic, **type the examples yourself**, and finish the exercise before you
move on. The exercises are where the learning sticks. Watching a twelve-hour
YouTube video on 1.5x and never compiling a file is how people arrive at build
season able to recognize Java and unable to write it.

You already have a GitHub account from [GitHub Basics](../github/) and a
personal `frc-learning` repository from [Git Fundamentals](../git/). Every
exercise in this ticket lands there: one branch per exercise (or per unit), a
pull request when a unit's programs run, a mentor looking at the same
acceptance criteria they will use on robot code. This site does not track
whether you finished. Close the team's exported issue only after a mentor can
compile what you pushed.

Work the units **in order**. Unit 14 assumes Unit 9. After this ticket you will
walk onto a real robot in [FRC Hardware & Firmware](../frc-hardware/) — the
Java does not get easier just because there are motors attached.

## Prerequisites

- [Git Fundamentals](../git/) completed: `frc-learning` cloned, you can
  branch, commit, push, and open a pull request.
- A computer you can install software on.
- The [WPILib VS Code installer](https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-2/wpilib-setup.html)
  (recommended — it includes a JDK and is what you will use for robot code)
  **or** a JDK 17+ plus any editor. VS Code without WPILib is fine for these
  exercises.

## What you'll learn

- How a Java program starts at `main`, what the primitive types are, and how
  `if`, `switch`, loops, arrays, and `ArrayList` actually behave when you run
  them.
- How to write methods, classes, enums, and a little inheritance — the same
  shapes WPILib subsystems and commands use.
- How to keep exercise solutions in Git so a mentor can run them, not just hear
  that you "did Java."

## How to work through the units

Type every example. Reading is not compiling. When an exercise is done:

1. Put it in `frc-learning/java/` as its own `.java` file (or a small folder
   per unit). Name files after the exercise: `Ex01Quarters.java`,
   `Ex02LeapYear.java`, and so on.
2. Commit on a branch that is not `main`. A branch per unit is plenty;
   a branch per exercise is better if you want smaller reviews.
3. Open a pull request when a unit's exercises run. Mention this ticket and
   the unit number in the PR body.

Ask for help after you have tried and can describe what you attempted. Paste
the compiler error or the wrong output, not "it doesn't work."

The units below are the course. The Tasks and Acceptance Criteria at the
bottom are how a mentor signs the ticket.

## Unit 1 — Getting started

After setting up your JDK and editor, the first thing to understand is how a
Java program runs. **Every Java program begins executing at a `main` method**,
and runs each line in order, top to bottom, starting from the first line of
`main`.

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
- **Comments** are ignored when the program runs: `// a single line`, or a
  block bookended by `/*` and `*/`.

Skim Oracle's
[A Closer Look at the "Hello World!" Application](https://docs.oracle.com/javase/tutorial/getStarted/application/index.html)
if `public static void` still looks like noise. You do not need to memorize
every keyword yet. You need the program to print two lines when you run it.

## Unit 2 — Variables, types & operators

Data is stored in **variables**, and every variable has a **type**. Java's
basic ("primitive") types are:

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

A **constant** is a variable declared with `final` — once initialized it can
never change. By convention constants are named in `ALL_CAPS` with
underscores:

```java
final double WHEEL_DIAMETER_INCHES = 6.0;
```

The basic math operators (`+ - * /`) follow normal order of operations. Watch
out: **dividing two integers rounds down** (`7 / 2` is `3`). The modulo
operator `%` gives the remainder (`7 % 2` is `1`), and `++` / `--` increase or
decrease a value by one.

A single equals `=` is the **assignment** operator (make the left side equal
the right). Two equals `==` is the **equality check** (is the left equal to
the right?):

```java
int x = 5 + 5;             // x becomes 10
boolean isTen = (x == 10); // true
```

You can combine math with assignment: `x += 1` is shorthand for `x = x + 1`.
Remember that plain math operators don't change a variable unless you also
assign the result back to it.

Oracle's
[Variables](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/variables.html)
and
[Operators](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/op1.html)
pages are the deeper reference. Use them when a type or an operator surprises
you, then come back and write the exercise.

**Exercise 1 — Quarters.** Three friends share 65 quarters. Write a program
that prints: the total value of all quarters; how many are left over after an
equal split; the value of one friend's pile (excluding leftovers); the value
if one friend gives their pile to another; and the new total after the
leftovers are added in.

## Unit 3 — Booleans & decisions

Java enforces **type safety**: if you try to put a value of one type into a
variable of an incompatible type, the code won't compile. This catches
mistakes early.

To make decisions, you build **boolean expressions** — statements that
evaluate to `true` or `false` — using:

- **Logical operators:** `!` (NOT, reverses true/false), `&&` (AND, true only
  if both sides are true), `||` (OR, true if either side is true), and `!=`
  (not equal).
- **Relational operators:** `<`, `>`, `<=`, `>=`.

An **`if` statement** runs a block only when its condition is true. If you
omit the braces, only the single line immediately after the condition is
included:

```java
if (speed > 0.5) {
  System.out.println("Going fast!");
}
```

An **`else`** block runs when the `if` condition is false. `if`/`else`
statements can be **nested** inside one another — keep paired braces at the
same indentation so you can see where each block begins and ends:

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

Read
[The if-then and if-then-else Statements](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/if.html)
if you want more examples. On a robot this is "are we enabled, and is the
limit switch pressed?" — same shape, messier names.

**Exercise 2 — Leap year.** Write a program that determines whether a given
year is a leap year (divisible by 4, except century years, which must be
divisible by 400).

## Unit 4 — Switch statements

When you'd otherwise write a long chain of `if`/`else` comparisons against one
value, a **`switch`** statement is cleaner. It evaluates an expression and
jumps to the matching `case` label. A `break` exits the switch; without it,
execution "falls through" into the next case. The `default` case runs when
nothing matches.

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

**Exercise 3 — Switch refactor.** Rewrite a small if/else program so it
produces the same output using a `switch` statement instead.

## Unit 5 — Scope & errors

**Scope** is the part of a program from which something is accessible. Scope
is defined by curly braces `{}`: anything declared inside a set of braces is
visible within those braces (including nested ones), but **not outside** them.
So a variable declared inside an `if` statement can't be used after that `if`
ends.

When execution leaves a scope (the end of a loop, `if`, or method), the
references created in that scope are removed. Any object no longer referenced
is automatically cleaned up by **garbage collection** — you don't free memory
manually in Java. You will meet this again in
[Debugging & Performance](../debugging/) when per-loop allocations stall the
robot.

It helps to distinguish two kinds of bugs:

- A **syntax error** breaks the rules of the language and won't compile — for
  example, a missing semicolon or using a variable that was never declared.
- A **logic error** compiles and runs but produces the wrong result or
  behavior — like a calculator that says `2 + 2 = 5`, or a robot that drives
  backward when told to go forward.

## Unit 6 — Arrays

An **array** holds a fixed number of values of the **same type**. The type is
the element type followed by `[]`, e.g. `int[]`. You access an element by its
**index** (its offset from the start), and **indexes start at 0**. Reading
past the end of the array throws an `IndexOutOfBoundsException`.

```java
int[] scores = {10, 20, 30}; // initialize with values
int first = scores[0];       // 10  (index 0 is the first element)
scores[1] = 25;              // change the second element

String[] names = new String[3]; // an empty array of length 3
```

**Exercise 4 — Pet store inventory.** Use two arrays (animal names and counts)
to print a store's inventory, then replace one animal with another and
re-print.

## Unit 7 — Loops

A **`while` loop** repeats its block as long as a condition is true. The
condition is checked **before** each pass, so if it's false to begin with, the
body never runs. Make sure the condition can eventually become false, or
you'll create an **infinite loop**:

```java
int i = 0;
while (i < 5) {
  System.out.println(i);
  i++; // without this, the loop never ends
}
```

A **`for` loop** is essentially a `while` loop with a built-in counter. Use it
when you know how many times you want to repeat. Its header has three parts:
initialization, a termination condition, and an increment:

```java
for (int i = 0; i < 5; i++) {
  System.out.println(i);
}
```

A **for-each loop** is shorthand for iterating over every element of an array
(or other iterable, like an `ArrayList`):

```java
int[] values = {3, 5, 8};
int sum = 0;
for (int v : values) {
  sum += v;
}
```

Oracle's
[The for Statement](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/for.html)
is the short official version of what you just typed.

**Exercise 5 — Loops + inventory.** Redo Exercise 4 using a `while` loop to
print the first inventory and a `for` loop to print the second — no more than
one print statement per loop.

## Unit 8 — Generics & ArrayList

A **generic type** lets a class work with a type that's specified later, when
an object is created, instead of being fixed in advance. Generic types are
written in diamond braces `<>`.

The most common use is **`ArrayList`**, a resizable cousin of the array with
many helpful methods. It must be imported, and it uses a generic type to say
what it holds (one type per list):

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

Useful `ArrayList` methods include `add`, `add(index, element)`,
`remove(index)`, `remove(object)`, `get(index)`, `set(index, element)`,
`size()`, `indexOf(object)`, and `contains(object)`.

**Exercise 6 — ArrayList.** Create an `ArrayList` of doubles, add several
values, insert one between two existing values, remove one, replace one, then
print every element with a for-each loop.

**Practice problems.** For extra reps: fill an `int` array, print it with a
`for`, `while`, and `for-each` loop, then copy the values into an `ArrayList`,
add one more, and print again.

## Unit 9 — Methods

A **method** is a named sequence of code that performs one operation and can
be called from elsewhere — this is how you avoid copying the same code in many
places. Each method has a **signature** describing its visibility, return
type, name, and parameters (inputs).

There are three **visibility** modifiers: `public` (visible to anyone),
`private` (only within the same class), and `protected` (this class and its
subclasses). The **return type** can be any type; if a method returns nothing,
its return type is `void`. Parameters are listed as comma-separated values in
parentheses, like the inputs to a math function `f(x, y)`.

```java
// public, returns a double, named "average", takes two doubles
public double average(double a, double b) {
  return (a + b) / 2;
}
```

This is the unit [Commands as Functions](../commands-as-functions/) will
stand on. A command is a method you hand to the scheduler to run *later*. If
methods still feel like magic, stop here until Exercise 7 runs.

**Exercise 7 — Methods.** Write methods that take three integers and return
the smallest, the largest, and the average; plus one that prints all three and
returns nothing. Call them from `main`. (Add `static` after `public` since
they're in the main class.)

## Unit 10 — Recursion

**Recursion** is when a method calls itself. It's a way to break a complicated
problem into smaller, simpler versions of the same problem. Every recursive
method needs a **base case** — a condition where it stops calling itself and
returns — otherwise it recurses forever (the recursion equivalent of an
infinite loop).

```java
public int factorial(int n) {
  if (n <= 1) {
    return 1;           // base case: stop here
  }
  return n * factorial(n - 1); // recursive case
}
```

**Exercise 8 — Factorial.** Write a recursive method that computes the
factorial of an integer, and use it to print 12!.

## Unit 11 — Exceptions (intro)

An **exception** is an event that disrupts normal execution at runtime. When
code "throws" an exception, information about what went wrong (its type and
location) is passed up to the surrounding code. Exceptions exist to stop
undefined or dangerous behavior, like using a `null` value or dividing by
zero.

Common exceptions you'll meet:

- `NullPointerException` — using an object that is `null` (never initialized).
- `ArithmeticException` — an illegal math operation, like integer
  divide-by-zero.
- `IllegalArgumentException` — a method was called with invalid input.
- `IllegalStateException` — a method was called before its prerequisites were
  met.
- `IOException` — an input/output operation failed.

You will read real stack traces in
[Debugging & Performance](../debugging/). For now, know the names and what
usually caused them.

## Unit 12 — Objects, classes & Strings

A **class** describes a *type* of thing; an **object** is a specific
*instance* of that class. "Book" is a class; the particular book on your desk
is an object. A class can hold **fields** (variables/objects) and **methods**.
By convention class names are Capitalized and object names use camelCase.

You create an object with the `new` keyword, which calls the class's
**constructor** (a special method that shares the class's name and has no
return type):

```java
String name = new String("Ada");
String nickname = "Ada"; // a "string literal" — shorthand for the above
```

When comparing objects, be careful: `==` compares **memory addresses** (are
these the exact same object?), while `.equals()` compares **values** (are
these equivalent?). For text, almost always use `.equals()`.

A **`String`** is a sequence of characters. The `+` operator **concatenates**
(joins) strings, and `+=` joins-and-assigns. The `String` class has many
useful methods, including:

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

**Exercise 9 — Strings.** Given a sentence, print its length, print a
substring, compare it (ignoring case) to another sentence, then `split` it on
spaces and print the number of words.

## Unit 13 — Input with Scanner

Java classes are organized into **packages**. To use a class from another
package you must **import** it (the `java.lang` package, which has `String`,
`Math`, etc., is always available). The **`Scanner`** class reads a source of
data as text — useful for reading user input from the command line:

```java
import java.util.Scanner;

Scanner scanner = new Scanner(System.in); // read from the keyboard
System.out.print("Enter a number: ");
int n = Integer.parseInt(scanner.nextLine());
scanner.close(); // always close a Scanner when done
```

A `Scanner` breaks its input into **tokens** separated by a **delimiter**
(whitespace by default). Key methods are `hasNext()`, `next()`, and
`nextLine()`. Always call `close()` when finished — I/O objects use
operating-system resources that aren't reliably garbage-collected, and failing
to close them leaks resources.

**Exercise 10 — Running average.** Read positive integers from user input into
an `ArrayList` until a negative number is entered, then print the average
(don't store the negative number).

## Unit 14 — Writing classes

So far you've used classes; now you'll write your own. A class is the
**blueprint** from which objects are created with `new`. Class names start
with an uppercase letter. A class contains **class-level variables** (fields),
a **constructor**, and **methods**.

Fields declared at the class level are in scope anywhere in the class. If you
make a field `public`, other classes can read/write it through an instance —
which is often *not* what you want. Making fields `private` and providing
**get/set methods** lets you control access to your data.

A **constructor** runs when you create an object with `new`. Like methods it
can be overloaded, but it has no return type. Constructors commonly initialize
fields from parameters:

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

A WPILib `Subsystem` is this idea with extra framework around it. Practice it
here, on a `Holiday` or a `Movie`, before you meet `Intake` and
`CommandSwerveDrivetrain`. Oracle's
[Classes and Objects](https://docs.oracle.com/javase/tutorial/java/javaOO/classes.html)
is the longer version.

**Exercise 11 — Custom classes.** Implement two small classes (for example, a
`Holiday` and a `Movie`) with fields, a constructor, and methods, and exercise
them from a `main` method.

## Unit 15 — Enums

An **enum** type is a special type whose value must be one of a fixed set of
named constants. Common examples are compass directions or days of the week.
Because the values are constants, they're named in `ALL_CAPS`. Use an enum
whenever you have a known, fixed set of choices (menu options, robot states,
command flags, etc.):

```java
public enum Direction {
  NORTH, SOUTH, EAST, WEST
}

Direction heading = Direction.NORTH;
```

Alliance color in [Match State & Alliance Color](../alliance-color/) is the
same idea: `Alliance.Red` or `Alliance.Blue`, not `0` and `1`.

**Exercise 12 — Enums.** Refactor a program that uses integers to represent a
fixed set of choices so it uses an `enum` instead.

## Unit 16 — Exceptions & try/catch

Sometimes *you* want to throw an exception — most often when a **precondition**
isn't met or a **postcondition** can't be satisfied. You throw one with the
`throw` keyword:

```java
if (speed < 0) {
  throw new IllegalArgumentException("speed must not be negative");
}
```

To keep your program running even when an exception occurs, wrap risky code in
a **`try`/`catch`** block. If the `try` block throws, execution jumps to the
`catch` block instead of crashing:

```java
try {
  int value = myNumbers[10]; // might be out of bounds
} catch (IndexOutOfBoundsException e) {
  System.out.println("Something went wrong, but we kept running.");
}
```

**Exercise 13 — Try/catch.** Starting from code that throws an exception
partway through, add handling so that every print statement still runs.

## Unit 17 — The `static` modifier

By default, fields and methods belong to an **object**, so you need an
instance to use them. The **`static`** modifier makes a field/method belong to
the **class itself**, so it can be used without creating an object — and
there's only ever one copy of a static field, shared across all instances.

```java
double r = Math.random(); // Math is a class; random() is a static method
```

A static field shared across all instances is handy for things like a counter
that assigns each new object a unique ID. `main` is static because the JVM
has to start the program before any instance exists.

**Exercise 14 — President.** Create a `President` class with a constructor and
a private `static boolean inOffice` that ensures only one `President` object
can be fully created. Add a `static` method that prints a message, and call it
from `main`.

## Unit 18 — Nested classes

Java lets you define a class **inside** another class — a **nested class**. A
nested class can be static or non-static:

- A **static** nested class can be instantiated without an instance of the
  outer class, and can only access the outer class's static members.
- A **non-static** nested class requires an instance of the outer class first,
  and can access all of the outer class's members.

WPILib `Constants` files often use static nested classes (`Constants.Drive`,
`Constants.Intake`) to group numbers. That is this unit, applied to a robot.

**Exercise 15 — Outer/inner classes.** Create an `OuterClass` with private
fields and a static `multiplier`. Add a non-static inner class whose method
prints the fields times the multiplier, and a static inner class that changes
the multiplier. Demonstrate the behavior before and after changing it.

## Unit 19 — Inheritance

**Inheritance** lets one class reuse another's data and methods. A
**subclass** (child) `extends` a **superclass** (parent), inheriting its
fields and methods and adding its own. The subclass can use the superclass's
members, but **not** the other way around — a parent can't see its child's
additions.

```java
public class Vehicle {
  String brand;
}

public class Car extends Vehicle { // Car inherits "brand" from Vehicle
  String model;
}
```

Command-based robot code uses this constantly: `SubsystemBase`, `Command`,
`InstantCommand`. You do not need to write a class hierarchy for this
exercise. You need to see `extends` and not freeze.

**Exercise 16 — Vehicles.** Create a `Vehicle` superclass and `Car` /
`Airplane` subclasses that each add their own field and set a `mode`.
Construct one of each and print all of their values.

## Unit 20 — Documentation

Good code is documented in three complementary ways — ideally you keep all
three up to date:

- **READMEs** — Markdown files (`.md`) that explain *what* the program is and
  how to use it. Anyone, even a non-programmer, should be able to read it.
- **JavaDocs** — generated documentation describing *what* each class, method,
  and field is for. Special `/** ... */` comments are turned into browsable
  HTML by the `javadoc` command (e.g. `javadoc -d myDoc src/*`).
- **Code comments** — plain comments in the code explaining *how* it works to
  other developers.

**Exercise 17 — Document it.** Take your Exercise 16 solution and add code
comments (noting which class each field comes from) plus a generated JavaDoc
that explains each class and constructor.

## Tasks

1. **Install a JDK and an editor.** Follow
   [WPILib: Installing VS Code and the WPILib tools](https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-2/wpilib-setup.html)
   if you do not already have them from a later robot ticket. Confirm
   `java --version` prints 17 or newer. If command-line Java is new, watch
   [Programming with Mosh: Java Full Course for Beginners](https://www.youtube.com/watch?v=eIrMbAQSU34)
   through the "Hello World" section (the first ~30 minutes), then come back
   and type Unit 1 yourself. [Bro Code's Java course](https://www.youtube.com/watch?v=xk4_1vDrzzo)
   is a longer alternate. Videos supplement these units. They do not replace
   the exercises.

2. **Make a home for the exercises.** In your `frc-learning` repo, create a
   `java/` folder and a short `java/README.md` that says you are working this
   ticket. Branch off `main` (`git checkout -b java-unit-01` or similar). You
   will keep using this folder for every unit.

3. **Work Units 1–8 in order.** Type the examples. Complete Exercises 1–6 and
   the Unit 8 practice problems. Commit each exercise as it starts to run —
   `git status`, `git add` the file, a commit message that names the exercise.
   After Unit 8, open a pull request titled something like "Java units 1–8
   exercises" and ask a mentor to run two of them.

4. **Work Units 9–16.** Complete Exercises 7–13. Same Git habit: branch (or
   keep committing on the unit branch), push, PR when a cluster of exercises
   runs. Exercise 10 needs keyboard input; include a comment at the top of
   the file that tells a mentor what to type.

5. **Work Units 17–20.** Complete Exercises 14–17. Generate JavaDoc for
   Exercise 17 into `java/ex17-docs/` (or similar) and commit it, or commit a
   screenshot of the generated HTML plus the source comments. Update
   `java/README.md` with a one-line index of every exercise file.

6. **Hand the repo to a mentor.** Paste the `frc-learning` URL (and the PR
   links) on the team's exported issue if they use one, or send them directly.
   Be ready to share your screen and run any exercise the mentor picks.

## Acceptance Criteria

- [ ] `java --version` is 17 or newer on the computer you use for this
      ticket.
- [ ] `frc-learning/java/` exists on a pushed branch and contains a README
      that lists the exercise files.
- [ ] Exercises 1–17 each live in their own `.java` file (or a clearly named
      per-exercise folder). A mentor can compile and run them without
      guessing which class is `main`.
- [ ] Each exercise was committed on a branch that is not the default branch.
      At least one pull request was opened for review (units 1–8 is the
      earliest acceptable checkpoint; more PRs are better).
- [ ] Exercise 10's file documents the input a reviewer should type.
- [ ] Exercise 17 includes code comments and JavaDoc (generated HTML in the
      repo, or a screenshot plus the `/** ... */` source).
- [ ] A mentor has watched you run at least two exercises live, including
      one from Units 9–19 (methods or classes, not only `println`).

## Resources

- [WPILib: VS Code and WPILib setup](https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-2/wpilib-setup.html)
- [Official Java Tutorials (Oracle)](https://docs.oracle.com/javase/tutorial/)
- [Oracle: Hello World closer look](https://docs.oracle.com/javase/tutorial/getStarted/application/index.html)
- [Oracle: Variables](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/variables.html)
- [Oracle: Operators](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/op1.html)
- [Oracle: if-then](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/if.html)
- [Oracle: The for Statement](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/for.html)
- [Oracle: Classes and Objects](https://docs.oracle.com/javase/tutorial/java/javaOO/classes.html)
- [Java SE 17 API documentation](https://docs.oracle.com/en/java/javase/17/docs/api/index.html)
- [Programming with Mosh: Java Full Course for Beginners (YouTube)](https://www.youtube.com/watch?v=eIrMbAQSU34)
- [Bro Code: Java Full Course (YouTube)](https://www.youtube.com/watch?v=xk4_1vDrzzo)
- [Stack Overflow](https://stackoverflow.com/) — for a specific compiler error,
  not as a substitute for writing the exercise

## Notes

- Don't rush. It is better to truly understand Units 1–8 than to skim all 20.
  Veteran tickets assume loops, lists, and methods are boring.
- Keep exercise solutions in version control. They make a reference later, and
  reviewing them is practice for the code review you will eventually give.
- Do not paste a chatbot's entire solution into `frc-learning` and call the
  unit done. If you use a hint, you still type the program and you still have
  to explain it.
- Integer division (`7 / 2 == 3`) and `==` on strings are the two mistakes
  that show up on the robot as "the code looks right."
- The next ticket, [FRC Hardware & Firmware](../frc-hardware/), is about the
  devices your Java will eventually talk to. You do not need to finish every
  extra practice problem before you start it, but Exercises 1–7 should already
  be on a branch.
