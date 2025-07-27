🛒 BazaarBuddy - AI-Powered B2B Marketplace
A modern B2B marketplace platform designed specifically for street food vendors and suppliers in India, featuring AI-powered inventory management, real-time analytics, and seamless supplier-vendor connections.

[![Live Demo](https://img.shields.s://img.shields.io/ Functionality**

Dual Dashboard System: Separate interfaces for vendors and suppliers with role-based access

AI-Powered Analytics: Smart inventory suggestions using DailyPortion AI

Real-Time Data: Interactive charts and performance metrics

Supplier Discovery: Google Maps integration for finding nearby suppliers

🤖 AI Capabilities
DailyPortion AI: Weather and event-based inventory recommendations

Demand Prediction: Historical data analysis for better forecasting

Business Insights: AI-generated growth recommendations

🎨 User Experience
Responsive Design: Mobile-first approach with Tailwind CSS

Dark/Light Mode: Automatic system preference detection with manual toggle

Interactive Maps: Google Maps integration for supplier discovery

Modern UI: Smooth animations and dynamic components

🚀 Quick Start
Live Demo
Visit the live application: bazaar-buddy-kg2u.onrender.com

Local Development
Clone the repository

bash
git clone https://github.com/JadenBritto/Bazaar-Buddy.git
cd Bazaar-Buddy
Set up virtual environment

bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
Install dependencies

bash
pip install -r requirements.txt
Configure environment variables

bash
cp .env.example .env
# Add your API keys to .env file
Set up database

bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
Run the application

bash
python manage.py runserver
Visit http://127.0.0.1:8000 to see the application in action.

🛠️ Tech Stack
Category	Technologies
Backend	Django 5.2.4, Python 3.12, SQLite/PostgreSQL
Frontend	Tailwind CSS, JavaScript ES6+, Chart.js
AI & APIs	Google Gemini API, Google Maps API, Weather API
Deployment	Render, Gunicorn, WhiteNoise
📁 Project Structure
text
bazaar-buddy/
├── mysite/                 # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── user/                   # User authentication app
│   ├── models.py          # UserProfile model
│   ├── views.py           # Authentication views
│   └── urls.py
├── myapp/                  # AI features app
│   ├── views.py           # DailyPortion AI
│   └── urls.py
├── templates/              # HTML templates
├── static/                 # CSS, JS, images
├── requirements.txt
└── manage.py
🔧 Configuration
Required Environment Variables
text
SECRET_KEY=your-secret-key
DEBUG=False
DATABASE_URL=postgresql://...
GEMINI_API_KEY=your-gemini-api-key
GOOGLE_MAPS_API_KEY=your-google-maps-key
ALLOWED_HOSTS=bazaar-buddy-kg2u.onrender.com,localhost
User Roles
The platform supports two user types:

Suppliers: Manage product listings and track orders

Vendors: Discover suppliers and manage inventory

🚀 Deployment
Deploy to Render
Connect your GitHub repository to Render

Set environment variables in Render dashboard

Build Command: pip install -r requirements.txt

Start Command: gunicorn mysite.wsgi:application

Deploy to Heroku
bash
# Install Heroku CLI and login
heroku create bazaar-buddy
heroku config:set SECRET_KEY=your-secret-key
heroku config:set DEBUG=False
git push heroku main
🤝 Contributing
We welcome contributions! Here's how you can help:

Fork the repository

Create a feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

Please read our Contributing Guidelines for more details.

🗺️ Roadmap
 Mobile App Development

 Payment Gateway Integration

 Multi-language Support

 Advanced AI Recommendations

 Real-time Chat Support

 Enhanced Inventory Management

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

🎉 Acknowledgments
Chart.js for beautiful data visualizations

Tailwind CSS for rapid UI development

Google APIs for maps and AI capabilities

Django Community for the amazing framework

📞 Support
Issues: GitHub Issues

Discussions: GitHub Discussions

Built with ❤️ for the Indian street food community

[![GitHub stars](https://img.shields.io/github/stars/JadenBritto/Bazorks](https://img.shields.io/github/forks/JadenBritto/BazadenBritto/Bazaar-Buddy/network/members
