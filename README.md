# Utility Hub 2.0 — Technical Documentation

## Overview

Utility Hub 2.0 is a command-line Python application that combines two everyday tools: a task manager and a basic calculator. The project demonstrates the use of functions, loops, conditional logic, and input validation to create an interactive user experience.

## Features

### 1. User Registration

The application prompts users to enter a username and create a password. Passwords must contain at least eight characters, and users must confirm their password before continuing.

### 2. To-Do List

The task manager allows users to:

* Add new tasks.
* View existing tasks.
* Remove tasks.
* Exit the task manager.

The application validates user selections and provides feedback when an input is invalid or a requested task cannot be found.

**Note:** Tasks are stored in memory and are not saved after the program terminates.

### 3. Calculator

The calculator supports four basic arithmetic operations:

* Addition
* Subtraction
* Multiplication
* Division

It validates numeric inputs and prevents division by zero. Users can perform multiple calculations without restarting the application.

## How to Run the Application

1. Ensure Python is installed on your computer.

2. Save the program in a Python file, such as `utility_hub.py`.

3. Open a terminal in the directory containing the file.

4. Run the following command:

   `python utility_hub.py`

5. Follow the prompts to register and select either the To-Do List or the Calculator.

## Code Structure

The application is organized into functions, each responsible for a specific task:

* `personal_account()` — collects the username.
* `accPass()` — creates and confirms the password.
* `is_number()` — checks whether an input can be converted to a number.
* `toDoList()` — manages task creation, viewing, and removal.
* `calculator()` — processes arithmetic operations and validates inputs.

A main menu connects the features and allows users to navigate between them.

## Input Validation and Error Handling

Input validation helps prevent common errors during program execution. The calculator rejects nonnumeric inputs and checks for division by zero. The registration process checks password length and confirmation. The task manager handles empty task lists and requests to remove tasks that do not exist.

## Limitations and Future Improvements

Potential improvements include:

* Storing tasks so they remain available after the application closes.
* Using secure password-handling practices instead of displaying passwords in plain text.
* Improving navigation between menus and handling unexpected inputs more consistently.
* Adding automated tests for the calculator, registration, and task-management functions.

## Conclusion

Utility Hub 2.0 was developed to practice Python programming and build an interactive application from smaller, reusable functions. Documenting its features, code structure, limitations, and potential improvements helps make the program easier to understand, maintain, and extend.
