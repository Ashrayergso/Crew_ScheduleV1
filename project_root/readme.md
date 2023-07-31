# Crew Assignment App

This is a Django-based web application that automates the assignment of crew members to ships. The application considers various factors such as crew position, contract duration, and vacation time for optimal assignment.

## Tech Stack

- Django framework for building the application
- PostgreSQL for the database
- Python
- Conda for Python environment isolation

## Requirements

The application implements user authentication using Django's built-in authentication.

## Data Models

The Django models included are:

- `CrewMember`
- `Cert`
- `Qualification`
- `Ship`
- `Positions`
- `Assignment`
- `ShipCrewAllowance`

## Views

The application includes list/detail views for each model, views to create/edit assignments, an automatic assignment view, and views to filter/sort ship and crew lists.

## Core Feature

The core feature of the application is the `assignCrewToShips` function, which automates the assignment of crew to ships.

## UI Components

UI components include Django templates for each view, with CSS and JavaScript files in the static directory for styling and interactivity.

## URL Configuration

The URL configuration defines the views and maps URLs to them.

## Project Focus

The primary focus of the project is to automate crew scheduling, thereby increasing efficiency and reducing errors.

## Tasks

The tasks executed are:

- Developing a Django-based application to automate crew member assignment to ships.
- Ensuring the application considers factors such as crew position, contract duration, vacation time, etc., for optimal assignment.
- Promoting efficiency and reducing errors in crew scheduling.

## UI Design

The user interface is clean and intuitive, with a main navigation bar for accessing different views. Each data model has its own list/detail view, presented in a table format for easy readability. The overall design is modern and professional, with a consistent color scheme and typography.

## Backend

The backend is built using Django. It contains models, views for each model, and URL patterns for each view. Django REST framework is used for API endpoints.

## Frontend

The frontend is built using Django's template system, complemented with CSS for styling and JavaScript for interactivity.

## Messages

The application uses Django's messaging framework to display messages like:

- "CREW_FETCH_SUCCESS": Displayed when the crew members are successfully fetched from the database.
- "SHIP_FETCH_SUCCESS": Displayed when the ships are successfully fetched from the database.
- "ASSIGNMENT_SUCCESS": Displayed when a new assignment is successfully created.
- "ASSIGNMENT_FAILURE": Displayed when there is an error creating a new assignment.

## UI Components and Views

The UI components and views are built using Django's template language. CSS is used for styling. The application is responsive and intuitive, with a modern design. Error handling and alerts are a crucial part of the application to ensure a smooth user experience.

## Installation

Refer to the `instructions.txt` file for detailed instructions on how to deploy the app.

## Dependencies

Refer to the `requirements.txt` file for a list of dependencies required to run the app.