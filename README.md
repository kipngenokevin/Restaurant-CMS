# Content Management System For Restaurants

## Team
Kevin Kipngeno

**Roles**:
* Design the User Interface for the system
* Write algorithms and methods for the system
* Test and deploy the system

## Technologies
* Python - Backend development
* MySql - Database Management
* HTML, CSS, Javascript - Front End Development
* Flask - Web Framework

## Challenge
The project aims to make it easy to make it easy for restaurants and restaurant owners to manage items in their menu. 
Currently most restaurant menus are hosted as pdf’s where a user scans and downloads the menu file, or gets a printed copy from the waiters & waitresses. This project aims to make it easy for the content managers who develop menus, design layouts and update prices for the food available in restaurants.

## Risks
Server errors. By chance if the server goes down, it means the service will  go offline and restaurant customers will not enjoy viewing the menu conveniently.

Security of data. If by chance there is a security breach, and the competition gets access to the competitors menu, they can write or delete sensitive information.

## Infrastructure
The data that will populate the menus is data that is publicly available on restaurant websites.

## Existing Solutions
Websites that are static that display restaurant menus
Online menus that are displayed in food ordering apps like Uber.

## API's and Methods
I will be using the Flask framework to set up my API endpoints. An endpoint will look like this for example:
https://kipngeno.tech/fetch/breakfast

## Data Modelling
The content management system captures the contents available in restaurants and stores them in a table. A single table for food items will suffice. Records will look like this:

| Food Items Table |
| ---------------- |
| id |
| created_at |
| updated_at |
| name |
| description |
| category |
| first_price |
| second_price |

## User Stories
The restaurant guest is seated and wants to see the menu. They look around and find a QR code displayed on the table or on a stand. The guest uses their phone's camera app to scan the QR code. Scanning the code automatically directs them to a mobile-friendly webpage showcasing the restaurant's complete menu. This webpage is designed for easy navigation on a phone, with clear categories, descriptions, and pricing for each item. Ideally, the menu should be high-resolution and include enticing pictures of the dishes to further tempt the guest (optional).
