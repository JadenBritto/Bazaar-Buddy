# 🛒 Bazaar Buddy

**Bazaar Buddy** is a Django-based platform designed to help vendors and suppliers manage local street food businesses effectively. It provides intelligent tools for pricing alerts, daily inventory planning, and business growth insights — optimized with Tailwind CSS for a modern UI.

🌐 **Live Site**: [bazaar-buddy-kg2u.onrender.com](https://bazaar-buddy-kg2u.onrender.com/)

---

## 📌 Features

- 🧾 **User Roles**: Register as a Supplier or a Regular User  
- 📈 **Mandi Price Alerts** ("Subah Bazaar"): Get updated local prices for smart purchasing  
- 📊 **Order Planning** ("DailyPortion"): Suggest daily buying quantity using past sales, weather, and trends  
- 📬 **Contact Support**: Reach out directly for feedback or help  
- 💅 Built with **Tailwind CSS** via `django-tailwind`

---

## 🚀 Tech Stack

- **Backend**: Django, PostgreSQL  
- **Frontend**: Tailwind CSS via django-tailwind  
- **Deployment**: Render  
- **Authentication**: Django's built-in auth system

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/JadenBritto/Bazaar-Buddy.git
cd Bazaar-Buddy

2. Create Virtual Environment
bash
Copy
Edit
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
3. Install Requirements
bash
Copy
Edit
pip install -r requirements.txt
4. Tailwind Setup (for development)
bash
Copy
Edit
cd theme  # navigate to Tailwind theme app
npm install
cd ..
python manage.py tailwind build
5. Run Migrations
bash
Copy
Edit
python manage.py migrate
6. Run Server
bash
Copy
Edit
python manage.py runserver
