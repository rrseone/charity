# 🌍 Charity -- Donation & Fundraising Platform

A full-stack **Charity & Crowdfunding Web Application** built with
**Django & Django REST Framework**, designed to help individuals and
organizations raise funds, manage campaigns, and enable seamless
donations.

------------------------------------------------------------------------

## 🚀 Overview

**Charity** is a scalable platform where:

-   Organizations can create fundraising campaigns\
-   Users can donate securely\
-   Admins can manage and monitor activities\
-   Transparency and usability are prioritized

------------------------------------------------------------------------

## ✨ Core Features

### 👤 User System

-   User registration & authentication\
-   Profile management\
-   Secure login/logout system

### 💰 Donations

-   Donate to campaigns\
-   Track donation history\
-   Transparent contribution records

### 📢 Campaign Management

-   Create, update, delete campaigns\
-   Set goals and deadlines\
-   Upload campaign images & details

### 🛠️ Admin Features

-   Manage users and campaigns\
-   Moderate content\
-   Monitor donations

------------------------------------------------------------------------

## 🧱 Tech Stack

### Backend

-   Python 3.x\
-   Django\
-   Django REST Framework

### Frontend

-   HTML5\
-   CSS3 / Bootstrap\
-   JavaScript / Angular

### Database

-   SQLite / PostgreSQL / MySQL

------------------------------------------------------------------------

## ⚙️ Installation

``` bash
git clone https://github.com/rrseone/charity.git
cd charity
python -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

------------------------------------------------------------------------

## 📁 Project Structure

    charity/
    ├── apps/
    ├── templates/
    ├── static/
    ├── media/
    ├── manage.py
    └── requirements.txt

------------------------------------------------------------------------

## 🔌 API Endpoints (Sample)

  Method   Endpoint          Description
  -------- ----------------- ----------------
  POST     /api/register/    Register user
  POST     /api/login/       Login user
  GET      /api/campaigns/   List campaigns
  POST     /api/donate/      Make donation

------------------------------------------------------------------------

## 🌱 Future Improvements

-   Payment gateway integration\
-   Admin analytics dashboard\
-   Email notifications\
-   Multi-language support

------------------------------------------------------------------------

## 🤝 Contributing

1.  Fork the repo\
2.  Create a branch\
3.  Commit changes\
4.  Push and open PR

------------------------------------------------------------------------

## 📄 License

MIT License

------------------------------------------------------------------------

## 👨‍💻 Author

**Rehan Rashid**

------------------------------------------------------------------------

## ⭐ Support

Give this project a ⭐ if you like it!
