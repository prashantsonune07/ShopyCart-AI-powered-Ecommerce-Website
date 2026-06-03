# ShopyCart — AI-Powered E-Commerce Platform

### Smart Shopping with Group Deals & Claude AI Assistant

> **"Shop Smarter, Save Together"**
> ShopyCart ensures every shopper finds the best deal — powered by AI that understands your taste and group buying that rewards community.

---

🌐 **Live Demo:** [shopycart-ai-powered-ecommerce-website.onrender.com](https://shopycart-ai-powered-ecommerce-website-dp5h.onrender.com)


## What is ShopyCart?

ShopyCart is a full-stack Django e-commerce platform built for the modern Indian shopper. It uses **Claude AI** as a personal shopping assistant and features a unique **Group Buying** system where friends join deals together to unlock massive discounts — the more people join, the lower the price drops.


### Core Flow

```
User Visits  →  AI Recommends  →  User Explores  →  Joins Group Deal  →  Saves Big
(homepage)     (Claude-powered)   (154+ products)   (friends invited)    (up to 70% off)
                                                           ↓
                                                   If goal not reached:
                                                   No charge (zero risk)
```


## Features

- 🤖 AI Personal Shopper — Claude-powered chat with natural language commands
- 🤝 Group Buying Deals — Live deals where more joiners = lower price
- 🛍️ Smart Product Discovery — Category filters, AI score rankings, trending picks
- ❤️ Wishlist — Save products and add all to cart in one click
- ⚖️ Product Compare — Compare up to 4 products side-by-side
- 🔐 Auth System — Signup/login with email verification and password reset
- 📦 Order Management — Place orders, track status, view history in profile
- 💳 Checkout & Payment — UPI, Card, NetBanking, and COD options
- 📱 Responsive Design — Works on desktop, tablet, and mobile
- 🎨 Modern UI — Custom cursor animation, smooth transitions, aesthetic typography


## Project Structure

```
ecommerce/
├── ecommerce/
│   ├── settings.py          # Django settings (env-based config)
│   ├── urls.py              # Root URL configuration
│   └── wsgi.py
├── ecommerceapp/
│   ├── models.py            # Product, Orders, OrderUpdate, Contact
│   ├── views.py             # All main views + AJAX category filter
│   ├── urls.py              # App URL patterns
│   └── admin.py             # Django admin configuration
├── authcart/
│   ├── views.py             # Login, signup, password reset
│   ├── urls.py              # Auth URL patterns
│   └── utils.py             # Token generator for email verification
├── templates/
│   ├── index.html           # Homepage with AI banner + group deals
│   ├── allproducts.html     # Full catalog with category filters
│   ├── groupdeals.html      # Group deals page with join modal
│   ├── checkout.html        # Checkout with address form
│   ├── payment.html         # Payment methods page
│   ├── paymentstatus.html   # Order confirmation with confetti
│   ├── profile.html         # My orders + order tracking
│   ├── login.html           # Animated split-screen login
│   └── signup.html          # Animated split-screen signup
├── static/                  # CSS, JS, images
├── requirements.txt         # Python dependencies
├── build.sh                 # Render build script
└── manage.py
```

---


## Local Setup


### Prerequisites

- Python 3.11+ (`python --version`)
- pip
- Git


### Installation

```bash
# Clone the repo
git clone https://github.com/prashantsonune07/ShopyCart-AI-powered-Ecommerce-Website.git
cd ShopyCart-AI-powered-Ecommerce-Website/ecommerce

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Load sample products
python manage.py loaddata products.json

# Start the server
python manage.py runserver
```

Open your browser at: `http://127.0.0.1:8000`


### Windows — Quick Start

Open CMD in your project folder and run:
```bash
python manage.py runserver
```
Then open `http://127.0.0.1:8000` in your browser.

---


## Tech Stack

| Layer | Technology |
|---|---|
| **AI Model** | Claude Sonnet via Anthropic API |
| **Backend** | Python · Django 4.2 · Gunicorn |
| **Database** | PostgreSQL (Render) · SQLite (local) |
| **Frontend** | Vanilla HTML · CSS · JavaScript |
| **Fonts** | Bebas Neue · DM Sans (Google Fonts) |
| **Images** | Unsplash (URL-based, no file storage) |
| **Deployment** | Render (Web Service + PostgreSQL) |
| **Static Files** | WhiteNoise |

---


## AI Shopping Assistant Commands

The Claude-powered chatbot understands natural language:

| What you type | What happens |
|---|---|
| `"add headphones to cart"` | Adds matching product to cart instantly |
| `"wishlist the dress"` | Saves product to wishlist |
| `"show my cart"` | Displays cart items with total |
| `"show all products"` | Shows mini product grid in chat |
| `"checkout"` | Redirects to checkout page |
| `"best deals today"` | Shows top discounted products with cards |
| Click chip buttons | Instant filtered product cards with actions |


## Environment Variables (Render)

| Key | Description |
|---|---|
| `SECRET_KEY` | Django secret key |
| `DATABASE_URL` | PostgreSQL internal URL from Render |
| `DEBUG` | Set to `False` in production |
| `PYTHON_VERSION` | Set to `3.11.9` |

---


*Built with ♥ in India — Powered by Django & Claude AI*
