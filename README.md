# Branching-Out

## Description

This project is a small Python application for filtering user data from a JSON file.
It was created to practice Git workflows with branches, fast-forward merges, commits, pushes, and a Pull Request on GitHub.

## Features

* Load user data from `users.json`
* Filter users by name
* Filter users by minimum age
* Filter users by email

## Project Structure

```text
Branching-Out/
├── users.json
├── filter_users.py
└── README.md
```

## How to Run

Run the Python script from the project folder:

```bash
python3 filter_users.py
```

Then choose one of the available filter options:

```text
name
age
email
```

## Git Workflow

This project uses separate feature branches:

* `feature-filter-by-age`
* `feature-filter-by-email`

The email feature was merged into `main` using a GitHub Pull Request.
