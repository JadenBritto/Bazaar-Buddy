# 🛒 BazaarBuddy - AI-Powered B2B Marketplace

[![Live Demo](https://img.shields.io/badge/Live%20Demo-bazaar--buddy--kg2u.onrender.com-green)](https://bazaar-buddy-kg2u.onrender.com)
[![Django](https://img.shields.io/badge/Django-5.2.4-092E20?logo=django)](https://djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python)](https://python.org/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-06B6D4?logo=tailwindcss)](https://tailwindcss.com/)

BazaarBuddy is a modern B2B marketplace platform designed specifically for street food vendors and suppliers in India. It features AI-powered inventory management, real-time analytics, and seamless supplier-vendor connections.

## 🌟 Features

### 🏪 **Dual Dashboard System**
- **Vendor Dashboard**: Order management, supplier discovery, analytics
- **Supplier Dashboard**: Product listings, order tracking, business insights

### 🤖 **AI-Powered Analytics**
- **DailyPortion AI**: Smart inventory suggestions based on weather, events, and historical data
- **Demand Prediction**: Weather-based demand forecasting
- **Business Insights**: AI-generated recommendations for growth

### 📊 **Real-Time Analytics**
- Interactive charts with Chart.js
- Revenue tracking and order analytics
- Performance metrics and KPIs
- Timeframe-based data visualization (7/30/90 days)

### 🎨 **Modern UI/UX**
- **Responsive Design**: Mobile-first approach with Tailwind CSS
- **Dark/Light Mode**: System preference detection with manual toggle
- **Smooth Animations**: CSS transitions and JavaScript animations
- **Interactive Components**: Dynamic popups, notifications, and forms

### 🗺️ **Supplier Discovery**
- **Interactive Maps**: Google Maps integration for nearby suppliers
- **Search & Filter**: Advanced filtering by category, distance, rating
- **Supplier Profiles**: Detailed supplier information and ratings

### 🔐 **Authentication System**
- **Role-Based Access**: Separate access for vendors and suppliers
- **Profile Management**: Complete user profile system
- **Secure Sessions**: Django's built-in authentication

## 🚀 Live Demo

Visit the live application: **[bazaar-buddy-kg2u.onrender.com](https://bazaar-buddy-kg2u.onrender.com)**

## 📸 Screenshots

### Vendor Dashboard
![Vendor Dashboard](path/to/vendor-dashboard-screenshot.png)

### AI Analytics
![AI Analytics](path/to/ai-analytics-screenshot.png)

### Dark Mode
![Dark Mode](path/to/dark-mode-screenshot.png)

## 🛠️ Tech Stack

### Backend
- **Django 5.2.4** - Web framework
- **Python 3.12** - Programming language
- **SQLite** - Database (development)
- **PostgreSQL** - Database (production)

### Frontend
- **Tailwind CSS** - Styling framework
- **JavaScript ES6+** - Interactive functionality
- **Chart.js** - Data visualization
- **Font Awesome** - Icons

### AI & APIs
- **Google Gemini API** - AI-powered suggestions
- **Google Maps API** - Location services
- **Weather API** - Weather-based predictions

### Deployment
- **Render** - Cloud hosting platform
- **Gunicorn** - WSGI server
- **WhiteNoise** - Static file serving

## 📦 Installation

### Prerequisites
- Python 3.12+
- Node.js (for Tailwind CSS compilation, optional)
- Git

### Local Development Setup

1. **Clone the repository**
git clone https://github.com/yourusername/bazaar-buddy.git
cd bazaar-buddy



2. **Create virtual environment**
python -m venv .venv
source .venv/bin/activate # On Windows: .venv\Scripts\activate


3. **Install dependencies**
pip install -r requirements.txt



4. **Environment variables**
Create .env file
cp .env.example .env

Add your API keys
GEMINI_API_KEY=your_gemini_api_key
GOOGLE_MAPS_API_KEY=your_google_maps_api_key
SECRET_KEY=your_django_secret_key
DEBUG=True



5. **Database setup**
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser



6. **Run development server**
python manage.py runserver



Visit `http://127.0.0.1:8000` to see the application.

## 📁 Project Structure

bazaar-buddy/
├── mysite/ # Django project settings
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── user/ # User authentication app
│ ├── models.py # UserProfile model
│ ├── views.py # Authentication views
│ ├── urls.py
│ └── migrations/
├── myapp/ # AI features app
│ ├── views.py # DailyPortion AI
│ └── urls.py
├── templates/
│ └── user/
│ ├── base.html # Base template
│ ├── login.html # Authentication pages
│ ├── signup.html
│ ├── vendor_dashboard.html
│ └── supplier_dashboard.html
├── static/
│ ├── css/
│ ├── js/
│ └── images/
├── requirements.txt
├── manage.py
└── README.md



## 🎯 Key Components

### User Authentication
- **Custom UserProfile Model**: Role-based user system
- **Dual Registration**: Separate flows for vendors and suppliers
- **Access Control**: Dashboard-specific permissions

### AI Features
- **DailyPortion**: AI inventory suggestions
- **Weather Integration**: Temperature-based demand prediction
- **Event Analysis**: Local event impact on sales

### Dashboard Features
- **Real-time Charts**: Revenue and order analytics
- **Quick Actions**: Order placement, supplier search
- **Supplier Discovery**: Map-based supplier finding
- **Dark Mode**: System preference with manual toggle

## 🔧 Configuration

### Environment Variables
SECRET_KEY=your-secret-key
DEBUG=False
DATABASE_URL=postgresql://...
GEMINI_API_KEY=your-gemini-api-key
GOOGLE_MAPS_API_KEY=your-google-maps-key
ALLOWED_HOSTS=bazaar-buddy-kg2u.onrender.com,localhost



### Database Models
UserProfile Model
USER_TYPE_CHOICES = (
('supplier', 'Supplier'),
('regular', 'Vendor'),
)



## 🚀 Deployment

### Deploy to Render

1. **Connect Repository**: Link your GitHub repository to Render
2. **Environment Variables**: Set all required environment variables
3. **Build Command**: `pip install -r requirements.txt`
4. **Start Command**: `gunicorn mysite.wsgi:application`

### Deploy to Heroku

1. **Install Heroku CLI**
2. **Create Heroku app**
heroku create bazaar-buddy


3. **Set environment variables**
heroku config:set SECRET_KEY=your-secret-key
heroku config:set DEBUG=False

4. **Deploy**
git push heroku main



## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### Development Workflow
1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎉 Acknowledgments

- **Chart.js** for beautiful data visualizations
- **Tailwind CSS** for rapid UI development
- **Google APIs** for maps and AI capabilities
- **Django Community** for the amazing framework

## 📞 Support

- **Email**: support@bazaarbuddy.com
- **Issues**: [GitHub Issues](https://github.com/yourusername/bazaar-buddy/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/bazaar-buddy/discussions)

## 🗺️ Roadmap

- [ ] Mobile App Development
- [ ] Payment Gateway Integration
- [ ] Multi-language Support
- [ ] Advanced AI Recommendations
- [ ] Inventory Management System
- [ ] Real-time Chat Support

---

<div align="center">
  <strong>Built with ❤️ for the Indian street food community</strong>
  <br>
  <a href="https://bazaar-buddy-kg2u.onrender.com">Live Demo</a> •
  <a href="#installation">Installation</a> •
  <a href="#contributing">Contributing</a>
</div>
Additional Files to Create:
1. .env.example
text
SECRET_KEY=your-django-secret-key-here
DEBUG=True
GEMINI_API_KEY=your-gemini-api-key
GOOGLE_MAPS_API_KEY=your-google-maps-api-key
DATABASE_URL=sqlite:///db.sqlite3
ALLOWED_HOSTS=localhost,127.0.0.1
2. requirements.txt (if not exists)
text
Django==5.2.4
gunicorn==21.2.0
whitenoise==6.6.0
psycopg2-binary==2.9.9
python-decouple==3.8
requests==2.31.0
3. CONTRIBUTING.md
text
# Contributing to BazaarBuddy

Thank you for your interest in contributing to BazaarBuddy! This document provides guidelines for contributing.

## Code of Conduct
- Be respectful and inclusive
- Focus on constructive feedback
- Help others learn and grow

## How to Contribute
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## Development Setup
Follow the installation instructions in README.md

## Reporting Issues
Use GitHub Issues to report bugs or request features.
