# 🎉 AAYAM Event Registration System

A modern web-based event registration platform built for **Karnavati University**.  
This system allows students to explore events, register easily, and view gallery content — all in one place.

---

## 🚀 Features

### 🧾 Event Registration
- Simple and clean registration form
- No login required
- Stores data in CSV (`registrations.csv`)

### 🖼️ Event Posters
- Dynamic event cards
- Custom images for each event
- Emoji fallback if no image provided

### 📸 Gallery (Admin Controlled)
- Upload photos and videos via Admin Panel
- Students can only view content
- Data stored in browser (localStorage)

### 💬 Feedback System
- Students can submit feedback
- Stored in `comments.csv`
- Displayed on homepage

### 🌗 Dark / Light Mode
- Toggle UI theme

---

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python (Flask)
- **Storage:** CSV files (no database)
- **Hosting Ready:** Google Cloud compatible

---

## 📁 Project Structure

```
CAPSTONE-PROJECT/
│
├── app.py
├── registrations.csv
├── comments.csv
│
├── templates/
│   └── index.html
│
├── static/
│   ├── aayam-logo.png
│   ├── ku-logo.png
│   │
│   ├── events/
│   │   ├── techfest.jpg
│   │   ├── cultural.jpg
│   │   └── ...
│   │
│   ├── gallery/
│       ├── photos/
│       ├── videos/
│       └── thumbs/
```

---

## ⚙️ Setup Instructions

### 1️⃣ Install Dependencies

```
pip install flask
```

### 2️⃣ Run the App

```
python app.py
```

### 3️⃣ Open in Browser

```
http://127.0.0.1:5000/
```

---

## 🧾 Registration System

Data is stored in `registrations.csv`.

---

## 💬 Comment System

Data is stored in `comments.csv`.

---

## 🖼️ Adding Event Posters

1. Place images in `static/events/`
2. Update in `index.html`:

```
img: '/static/events/techfest.jpg'
```

---

## 📸 Gallery System

### 🔐 Admin Access
Password: `aayam2026`

---

## ⚠️ Important Notes

- Always use `/static/...` paths
- File names are case-sensitive

---

## 👨‍💻 Author

Developed by **Jeel Patel**  
Capstone Project — Google Cloud Digital Leader
