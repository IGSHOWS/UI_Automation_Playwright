# Playwright QA Assignment – Task 1

## 📌 Overview
This project automates a critical end-to-end user flow using Playwright (Python) with Page Object Model (POM) design pattern.

---

## 🔁 Automated Flow
Login → Inventory → Logout

---

## 🧠 Why this flow?
Login is a critical entry point of any application. It ensures proper authentication and access to system features.  
This test validates the core user journey end-to-end.

---

## 🏗️ Tech Stack
- Playwright (Python)
- Pytest
- Page Object Model (POM)

---

## 📁 Project Structure

```
playwright-qa-assignment/
│
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│
├── tests/
│   ├── test_e2e_login_flow.py
│
├── utils/
│   ├── config.py
│
├── conftest.py
├── requirements.txt
├── README.md
```

## ⚙️ Setup Instructions

1. Clone the repository  
```
git clone <https://github.com/IGSHOWS/UI_Automation_Playwright.git>
```

2. Navigate to project directory  
```
cd UI_Automation_Playwright
```

3. (Optional) Create virtual environment  
```
python -m venv venv
```

4. Activate virtual environment  

Windows:
```
venv\Scripts\activate
```

Mac/Linux:
```
source venv/bin/activate
```

5. Install dependencies  
```
pip install -r requirements.txt
```

6. Install Playwright browsers  
```
playwright install
```

---

## ▶️ Run Tests

pytest

---

## 🏗️ Tech Versions

- Python: 3.10+
- Playwright: 1.x
- Pytest: 7.x

---

## ✅ Key Highlights
- End-to-end automation  
- POM-based framework  
- Centralized configuration (no hardcoding)  
- Proper assertions  
- Playwright auto-wait (no hard waits)  

---

## ⚙️ Configuration
Base URL and credentials are stored in:

utils/config.py

---

## 🤖 AI Usage
AI tools (ChatGPT) were used to assist in:
- Structuring the automation framework  
- Improving test flow design  
- Suggesting better assertions  

All implementations were reviewed and validated manually.

---

## 👨‍💻 Author
Ishlok Gupta