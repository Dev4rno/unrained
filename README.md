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

-   Deployment: Railway

-   Static Files: Whitenoise

-   Version Control: Git

### Getting Started

#### Prerequisites

-   Python 3.8+

-   Django 4.0+

-   An OpenWeatherMap API key (sign up at OpenWeatherMap)

#### Installation

1. Clone the Repository:

git clone https://github.com/your-username/unrained.git
cd unrained 2. Set Up a Virtual Environment:

python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate 3. Install Dependencies:

```bash
pip install -r requirements.txt
Set Up Environment Variables:
```

4. Create a .env file in the root directory and add your OpenWeatherMap API key:

```bash
OPENWEATHERMAP_API_KEY=your_api_key_here
SECRET_KEY=your_django_secret_key_here
DEBUG=True # Set to False in production
```

5. Run Migrations:

```bash
python manage.py migrate
Collect Static Files:
```

```bash
python manage.py collectstatic
Run the Development Server:
```

```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000 in your browser to see the app in action.

## Project Structure

```plaintext
unrained/
├── unrained/ # Project settings and configurations
│ ├── **init**.py
│ ├── settings.py
│ ├── urls.py
│ ├── asgi.py
│ └── wsgi.py
├── weather/ # Weather app
│ ├── migrations/
│ ├── **init**.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── tests.py
│ ├── views.py
│ └── templates/ # Templates for the weather app
│ └── weather/
│ ├── city_search.html
│ ├── city_selection.html
│ └── weather_result.html
├── manage.py
├── requirements.txt
├── Procfile # Railway deployment configuration
├── .env # Environment variables
└── .gitignore
```

Deployment
Deploying to Railway
Install the Railway CLI:

npm install -g @railway/cli
Log in to Railway:

railway login
Link Your Project:

railway link
Set Environment Variables:
Add your environment variables (e.g., OPENWEATHERMAP_API_KEY, SECRET_KEY) in the Railway dashboard or using the CLI:

railway env set OPENWEATHERMAP_API_KEY=your_api_key_here
railway env set SECRET_KEY=your_django_secret_key_here
railway env set DEBUG=False
Deploy Your App:

railway up
Visit Your App:
Once deployed, Railway will provide a URL for your app (e.g., https://unrained-production.up.railway.app).

Configuration
Environment Variables
Variable Description Example Value
OPENWEATHERMAP_API_KEY OpenWeatherMap API key your_api_key_here
SECRET_KEY Django secret key your_django_secret_key_here
DEBUG Enable/disable debug mode False (production)
ALLOWED_HOSTS Allowed hostnames for the app ["unrained-production.up.railway.app"]
CSRF_TRUSTED_ORIGINS Trusted origins for CSRF protection ["https://unrained-production.up.railway.app"]
Contributing
Contributions are welcome! Here’s how you can contribute:

Fork the Repository:
Click the "Fork" button at the top right of the repository page.

Clone Your Fork:

git clone https://github.com/your-username/unrained.git
cd unrained
Create a New Branch:

git checkout -b feature/your-feature-name
Make Changes and Commit:

git add .
git commit -m "Add your feature"
Push to Your Fork:

git push origin feature/your-feature-name
Create a Pull Request:
Go to the original repository and click "New Pull Request."

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
OpenWeatherMap: For providing the weather data API.

Django: For the powerful web framework.

Railway: For the easy-to-use deployment platform.

Contact
If you have any questions or feedback, feel free to reach out:

Your Name: Your Email

GitHub: Your GitHub Profile
