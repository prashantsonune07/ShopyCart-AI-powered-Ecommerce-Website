# ShopyCart — AI-Powered E-Commerce Website
### Full-Stack Django E-Commerce Platform with AI Shopping Assistant

> **"Shop smarter, not harder"**
> ShopyCart helps users discover and buy products through an AI assistant, group deals, and seamless payments — all in one platform.

---

## What is ShopyCart?

ShopyCart is a fully functional AI-powered e-commerce web application built with Django. It features ShopyAI — a smart chatbot that knows all products, a group deals system for collaborative savings and a complete order management system deployed on Render with PostgreSQL.

## Features

- 🛒 **Products** across 10 categories — Electronics, EarBuds, Camera, Fashion, Beauty, Sports, Home, Footwear, Gaming, Food
- 🤖 **ShopyAI Chatbot** — AI-powered shopping assistant with full product knowledge
- 👥 **Group Buying Deals** — Friends shop together for bigger discounts
- 🔐 **User Authentication** — Register, Login, Profile, Order History
- 📦 **Order Tracking** — Real-time order status updates
- 🛠️ **Django Admin Panel** — Manage products, orders and users

## Quick Start

```bash
git clone https://github.com/prashantsonune07/ShopyCart-AI-powered-Ecommerce-Website.git
cd ShopyCart-AI-powered-Ecommerce-Website/ecommerce
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000` in your browser.

## Project Structure

```
ShopyCart/
├── ecommerce/
│   ├── ecommerceapp/        # Models, Views, Admin
│   ├── authcart/            # Login & Register
│   ├── PayTm/               # PayTM payment gateway
│   ├── templates/           # HTML pages
│   ├── static/              # CSS, JS, images
│   ├── products.json        # 154 products fixture
│   └── manage.py
├── start_shopycart.bat      # Windows one-click launcher
└── README.md
```

## Tech Stack

- **Backend**: Django 4.2, Python
- **Database**: PostgreSQL (Render) / SQLite (local)
- **Frontend**: HTML, CSS, Vanilla JavaScript
- **AI Chatbot**: Claude AI (Anthropic) via API
- **Payments**: PayTM Payment Gateway
- **Deployment**: Render

## Live Demo

🌐 [https://shopycart-ai-powered-ecommerce-website.onrender.com](https://shopycart-ai-powered-ecommerce-website.onrender.com)

---


