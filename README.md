# Unrained 🌦️

Unrained is a sleek and modern weather app built with Django. It allows users to search for weather information by city name, view detailed weather data, and enjoy a clean, responsive user interface. The app integrates with the OpenWeatherMap API to fetch real-time weather data.

## Features

-   **City Search**: Search for weather information by city name.

-   **City Selection**: Choose from a list of matching cities if multiple results are found.

-   **Detailed Weather Data**: View temperature, humidity, wind speed, sunrise/sunset times, and more.

-   **Responsive Design**: Works seamlessly on desktop and mobile devices.

-   **CSRF Protection**: Secure forms with Django's built-in CSRF protection.

-   **Deployment Ready**: Configured for easy deployment on Railway.

## Technologies Used

-   Backend: Django (Python)

-   Frontend: HTML, CSS, JavaScript

-   API: OpenWeatherMap

-   Deployment: Vercel

-   Static Files: Whitenoise

### Getting Started

#### Prerequisites

-   Python 3.8+

-   Django 4.0+

-   An OpenWeatherMap API key (sign up at OpenWeatherMap)

#### Installation

1. Clone the Repository:

```bash
git clone https://github.com/your-username/unrained.git
cd unrained
```

2. Set Up a Virtual Environment:

```bash
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
```

3. Install Dependencies:

```bash
pip install -r requirements.txt
```

4. Set Up Environment Variables:

Edit the `.env.example` file in the root directory with your assigned keys:

```bash
API_KEY=YOUR_OPEN_WEATHER_API_KEY # available on registration (free)
SECRET_KEY=YOUR_DJANGO_SECRET_KEY # found in unrained/settings.py
API_ANALYTICS_KEY=YOUR_ANALYTICS_API_KEY # https://www.apianalytics.dev/
```

and then rename the file to `.env`.

5. Run Migrations:

```bash
python manage.py migrate
```

6. Collect Static Files:

```bash
python manage.py collectstatic
```

7. Run the Development Server:

```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000 in your browser to see the app in action.

## Contact

If you have any questions or feedback, feel free to reach out:

-   [Email](mailto:alex@devarno.com)
-   [Bluesky](https://bsky.app/profile/devarno.com/)
-   [GitHub](https://github.com/Dev4rno/)
