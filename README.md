# 🛒 BazaarBuddy - AI-Powered B2B Marketplace

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/release/python-312/)
[![Django 5.2.4](https://img.shields.io/badge/django-5.2.4-green.svg)](https://djangoproject.com/)
[![Live Demo](https://img.shields.io/badge/demo-live-success)](https://bazaar-buddy-kg2u.onrender.com)

> A modern B2B marketplace platform designed specifically for street food vendors and suppliers in India, featuring AI-powered inventory management, real-time analytics, and seamless supplier-vendor connections.

[![GitHub Repo stars](https://img.shields.io/github/stars/JadenBritto/Bazaar-Buddy?style=social)](https://github.com/JadenBritto/Bazaar-Buddy/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/JadenBritto/Bazaar-Buddy?style=social)](https://github.com/JadenBritto/Bazaar-Buddy/network/members)
[![GitHub watchers](https://img.shields.io/github/watchers/JadenBritto/Bazaar-Buddy?style=social)](https://github.com/JadenBritto/Bazaar-Buddy/watchers)
[![GitHub followers](https://img.shields.io/github/followers/JadenBritto?style=social)](https://github.com/JadenBritto)

## 🌟 Features

### 🎯 **Core Functionality**
- **Dual Dashboard System**: Separate interfaces for vendors and suppliers with role-based access
- **AI-Powered Analytics**: Smart inventory suggestions using DailyPortion AI
- **Real-Time Data**: Interactive charts and performance metrics
- **Supplier Discovery**: Google Maps integration for finding nearby suppliers

### 🤖 **AI Capabilities**
- **DailyPortion AI**: Weather and event-based inventory recommendations
- **Demand Prediction**: Historical data analysis for better forecasting
- **Business Insights**: AI-generated growth recommendations

### 🎨 **User Experience**
- **Responsive Design**: Mobile-first approach with Tailwind CSS
- **Dark/Light Mode**: Automatic system preference detection with manual toggle
- **Interactive Maps**: Google Maps integration for supplier discovery
- **Modern UI**: Smooth animations and dynamic components

## 🚀 Quick Start

### Live Demo
Visit the live application: **[bazaar-buddy-kg2u.onrender.com](https://bazaar-buddy-kg2u.onrender.com)**

### Local Development

1. **Clone the repository**
git clone https://github.com/JadenBritto/Bazaar-Buddy.git
cd Bazaar-Buddy



2. **Set up virtual environment**
python -m venv .venv
source .venv/bin/activate # On Windows: .venv\Scripts\activate



3. **Install dependencies**
pip install -r requirements.txt



4. **Configure environment variables**
cp .env.example .env

Add your API keys to .env file


5. **Set up database**
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser


6. **Run the application**
python manage.py runserver



Visit `http://127.0.0.1:8000` to see the application in action.

## 🛠️ Tech Stack

| Category | Technologies |
|----------|-------------|
| **Backend** | Django 5.2.4, Python 3.12, SQLite/PostgreSQL |
| **Frontend** | Tailwind CSS, JavaScript ES6+, Chart.js |
| **AI & APIs** | Google Gemini API, Google Maps API, Weather API |
| **Deployment** | Render, Gunicorn, WhiteNoise |

## 📁 Project Structure
<pre>
bazaar-buddy/
├── mysite/ # Django project settings
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── user/ # User authentication app
│ ├── models.py # UserProfile model
│ ├── views.py # Authentication views
│ └── urls.py
├── myapp/ # AI features app
│ ├── views.py # DailyPortion AI
│ └── urls.py
├── templates/ # HTML templates
├── static/ # CSS, JS, images
├── requirements.txt
└── manage.py
</pre>


## 🔧 Configuration

### Required Environment Variables

SECRET_KEY=your-secret-key
DEBUG=False
DATABASE_URL=postgresql://...
GEMINI_API_KEY=your-gemini-api-key
GOOGLE_MAPS_API_KEY=your-google-maps-key
ALLOWED_HOSTS=bazaar-buddy-kg2u.onrender.com,localhost



### User Roles

The platform supports two user types:
- **Suppliers**: Manage product listings and track orders
- **Vendors**: Discover suppliers and manage inventory

## 🚀 Deployment

### Deploy to Render

1. Connect your GitHub repository to Render
2. Set environment variables in Render dashboard
3. **Build Command**: `pip install -r requirements.txt`
4. **Start Command**: `gunicorn mysite.wsgi:application`

### Deploy to Heroku

Install Heroku CLI and login
heroku create bazaar-buddy
heroku config:set SECRET_KEY=your-secret-key
heroku config:set DEBUG=False
git push heroku main



## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please read our [Contributing Guidelines](CONTRIBUTING.md) for more details.

## 🗺️ Roadmap

- [ ] Mobile App Development
- [ ] Payment Gateway Integration
- [ ] Multi-language Support
- [ ] Advanced AI Recommendations
- [ ] Real-time Chat Support
- [ ] Enhanced Inventory Management

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎉 Acknowledgments

- **Chart.js** for beautiful data visualizations
- **Tailwind CSS** for rapid UI development
- **Google APIs** for maps and AI capabilities
- **Django Community** for the amazing framework

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/JadenBritto/Bazaar-Buddy/issues)
- **Discussions**: [GitHub Discussions](https://github.com/JadenBritto/Bazaar-Buddy/discussions)

**Built with ❤️ for the Indian street food community**

[![Made with Love](https://img.shields.io/badge/Made%20with-❤️-red.svg)](https://github.com/JadenBritto)
[![GitHub](https://img.shields.io/badge/GitHub-JadenBritto-blue?logo=github)](https://github.com/JadenBritto)
