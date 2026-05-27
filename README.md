# ShopyCart — AI-Powered E-Commerce Platform
### Smart Shopping with Group Deals & Claude AI Assistant

> **"Shop Smarter, Save Together"**
> ShopyCart combines AI-powered personalization with group buying to give every shopper the best deals.

---

## 🌐 Live Demo

🛒 **[https://shopycart-ai-powered-ecommerce-website.onrender.com](https://shopycart-ai-powered-ecommerce-website.onrender.com)**

---

## ✨ What is ShopyCart?

ShopyCart is a full-stack Django e-commerce platform built for the modern Indian shopper. It uses **Claude AI** as a personal shopping assistant and features a unique **Group Buying** system where friends can join deals together to unlock massive discounts — the more people join, the lower the price drops.

---

## 🚀 Features

- 🤖 **AI Personal Shopper** — Powered by Claude AI, helps users find products, compare options, add to cart, and manage wishlist through natural conversation
- 🤝 **Group Buying Deals** — Join live group deals with friends; price drops as more people join (up to 70% off)
- 🛍️ **Smart Product Discovery** — Category filters, AI score rankings, trending picks, and personalized recommendations
- ❤️ **Wishlist** — Save products and add all to cart in one click
- ⚖️ **Product Compare** — Compare up to 4 products side-by-side with AI score and best price badges
- 🔐 **Auth System** — Full signup/login with email verification and password reset
- 📦 **Order Management** — Place orders, track status, view order history in profile
- 💳 **Checkout & Payment** — Secure checkout with UPI, Card, NetBanking, and COD options
- 📱 **Responsive Design** — Works beautifully on desktop, tablet, and mobile
- 🎨 **Modern UI** — Custom cursor animation, smooth transitions, Bebas Neue typography, dark/light sections

---

## 🖼️ Screenshots

| Homepage | AI Chatbot | Group Deals |
|---|---|---|
| Hero with AI banner and product grid | Claude-powered chat with smart commands | Live deals with progress bars and join flow |

| All Products | Checkout | Profile |
|---|---|---|
| Category filter with 154+ products | Multi-step payment flow with confetti | Order history with tracking |

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | Django 4.2.16 (Python 3.11) |
| **Database** | PostgreSQL (Render) / SQLite (local) |
| **AI** | Claude Sonnet via Anthropic API |
| **Frontend** | Vanilla HTML, CSS, JavaScript |
| **Fonts** | Bebas Neue, DM Sans (Google Fonts) |
| **Images** | Unsplash (URL-based, no file storage needed) |
| **Auth** | Django built-in + email verification |
| **Deployment** | Render (Web Service + PostgreSQL) |
| **Static Files** | WhiteNoise |

---

## 📁 Project Structure

```
ecommerce/
├── ecommerce/
│   ├── settings.py          # Django settings (env-based config)
│   ├── urls.py              # Root URL configuration
│   └── wsgi.py
├── ecommerceapp/
│   ├── models.py            # Product, Orders, OrderUpdate, Contact
│   ├── views.py             # All main views + AJAX handlers
│   ├── urls.py              # App URL patterns
│   └── admin.py             # Django admin config
├── authcart/
│   ├── views.py             # Login, signup, password reset
│   ├── urls.py              # Auth URL patterns
│   └── utils.py             # Token generator for email verification
├── templates/
│   ├── index.html           # Homepage with AI banner + group deals
│   ├── allproducts.html     # Full catalog with category filters
│   ├── allproducts_cards.html # AJAX partial for category filtering
│   ├── groupdeals.html      # Group deals page with join modal
│   ├── checkout.html        # Checkout with address form
│   ├── payment.html         # Payment methods page
│   ├── paymentstatus.html   # Order confirmation with confetti
│   ├── profile.html         # My orders + order tracking
│   ├── login.html           # Animated login page
│   └── signup.html          # Animated signup page
├── static/                  # CSS, JS, images
├── requirements.txt
├── build.sh                 # Render build script
└── manage.py
```

---

## ⚙️ Local Setup

### Prerequisites
- Python 3.11+
- Git

### Steps

**1. Clone the repo:**
```bash
git clone https://github.com/prashantsonune07/ShopyCart-AI-powered-Ecommerce-Website.git
cd ShopyCart-AI-powered-Ecommerce-Website/ecommerce
```

**2. Create virtual environment:**
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

**3. Install dependencies:**
```bash
pip install -r requirements.txt
```

**4. Run migrations:**
```bash
python manage.py migrate
```

**5. Create superuser (for admin panel):**
```bash
python manage.py createsuperuser
```

**6. Load sample products:**
```bash
python manage.py loaddata products.json
```

**7. Start the server:**
```bash
python manage.py runserver
```

Open **[http://127.0.0.1:8000](http://127.0.0.1:8000)** in your browser.

---

## 🌍 Deployment on Render

### Environment Variables Required

| Key | Description |
|---|---|
| `SECRET_KEY` | Django secret key |
| `DATABASE_URL` | PostgreSQL internal URL from Render |
| `DEBUG` | Set to `False` in production |
| `PYTHON_VERSION` | Set to `3.11.9` |

### Build & Start Commands

```bash
# Build Command
./build.sh

# Start Command
gunicorn ecommerce.wsgi:application
```

---

## 🤖 AI Shopping Assistant Commands

The Claude-powered chatbot understands natural language:

| Command | Action |
|---|---|
| `"add headphones to cart"` | Adds matching product to cart |
| `"wishlist the dress"` | Saves to wishlist |
| `"show my cart"` | Displays cart with total |
| `"show all products"` | Shows mini product grid |
| `"checkout"` | Redirects to checkout |
| `"best deals today"` | Shows top discounted products |
| Click chip buttons | Instant filtered product cards |

---

## 🗃️ Database Models

```python
Product       # product_name, category, subcategory, price, desc, image (URL)
Orders        # items_json, amount, name, email, address, paymentstatus
OrderUpdate   # order_id, update_desc, delivered, timestamp
Contact       # name, email, desc, phonenumber
```

---

## 👨‍💻 Author

**Prashant Sonune**
- GitHub: [@prashantsonune07](https://github.com/prashantsonune07)
- Live: [shopycart-ai-powered-ecommerce-website.onrender.com](https://shopycart-ai-powered-ecommerce-website.onrender.com)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

*Built with ♥ in India — Powered by Django & Claude AI*
