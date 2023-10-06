# Tasker v0.1

Tasker is a simple terminal-based task manager written in Python. It allows you to add, delete, list, and rename tasks, all within your command line interface. This README provides an overview of the application's features and how to use it.

## Features

-   **Simple Interface:** Tasker is easy to use and navigate. It's a great way to manage your tasks without leaving the command line.
-   **JSON Storage:** Tasker stores your tasks in a JSON file, so you can access them even after closing the application.
-   **Add Tasks:** Add tasks along with their descriptions.
-   **Delete Tasks:** Remove tasks from the list.
-   **List Tasks:** View a list of all tasks.
-   **Rename Tasks:** Change the name of a task.
-   **Greet User:** Get a friendly greeting based on the time of day.

## Prerequisites

-   Python 3.6 or higher. You can download it [here](https://www.python.org/downloads/).
-   The `colorama` library for terminal styling. You can install it using `pip`:

    ```bash
    pip install colorama
    ```

## Usage

1. Run the program in the terminal:

    ```bash
    python tasker.py
    ```

2. You'll be greeted with a friendly message based on the time of day (morning, afternoon, or evening).
3. Use the following commands to interact with Tasker:

    - `1` - Add a task to the list.
    - `2` - Delete a task from the list.
    - `3` - View a list of all tasks.
    - `4` - Change the name of a task.
    - `help` - View a list of all commands.
    - `greet` - Get a greeting message again.
    - `exit` - Exit the program.

4. Follow the prompts to perform the desired task. You can add, delete, list, or rename tasks as needed.
5. When you're done, type `exit` to close the application.

## Author

Felix Groot - [fgroot-netlify.app](https://fgroot.netlify.app)

## License

This project is licensed under the MIT License.
