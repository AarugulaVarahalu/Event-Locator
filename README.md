Event Management System

Overview
This Django project is an Event Management System that allows users to upload event data from a CSV file, search for events based on date, and perform CRUD operations on events via a RESTful API.

Features
Upload Events: Users can upload event data from a CSV file containing event name, city name, date, time, latitude, and longitude.
Search Events: Users can search for events based on a specified date range.
CRUD Operations: Events can be created, read, updated, and deleted through the provided API endpoints.

Setup
Clone the repository:
git clone https://github.com/your_username/event-management.git

Install dependencies:
pip install -r requirements.txt

Apply migrations:
python manage.py migrate

Run the development server:
python manage.py runserver

Access the application at http://localhost:8000.

Usage
Uploading Events
Navigate to the "Upload Events" page.
Choose a CSV file containing event data and submit the form.

Searching Events
Navigate to the "Search Events" page.
Enter a date range and submit the form to view events within that range.

API Endpoints
GET /api/events/: Retrieve a list of all events.
POST /api/events/: Create a new event.
GET /api/events/{id}/: Retrieve details of a specific event.
PUT /api/events/{id}/: Update details of a specific event.
DELETE /api/events/{id}/: Delete a specific event.





![Screenshot (226)](https://github.com/AarugulaVarahalu/Event-Locator/assets/118363042/d2640535-163b-404f-b681-408411fe1399)


![Screenshot (227)](https://github.com/AarugulaVarahalu/Event-Locator/assets/118363042/7a262b3e-5c18-4ef3-aa0a-3b21ca3390fc)


![Screenshot (228)](https://github.com/AarugulaVarahalu/Event-Locator/assets/118363042/9e8487fa-3908-41c0-afbc-cde23b4e76c9)


![Screenshot (229)](https://github.com/AarugulaVarahalu/Event-Locator/assets/118363042/47542b06-c1eb-4217-a637-d7ebd9285a76)


![Screenshot (230)](https://github.com/AarugulaVarahalu/Event-Locator/assets/118363042/ca9a136d-caa3-4d49-a457-934f8d3c107b)


![Screenshot (231)](https://github.com/AarugulaVarahalu/Event-Locator/assets/118363042/d947a43f-13ff-4fbb-9bc9-59d5cbd0f02b)


![Screenshot (234)](https://github.com/AarugulaVarahalu/Event-Locator/assets/118363042/9e299b8c-c0da-4948-9268-5af06a5cae3e)


![Screenshot (232)](https://github.com/AarugulaVarahalu/Event-Locator/assets/118363042/81fd46f7-9400-418e-a9a3-205dbdef0444)


![Screenshot (233)](https://github.com/AarugulaVarahalu/Event-Locator/assets/118363042/5b6de65a-e1ec-4bdf-99f1-999c9f44ad84)

