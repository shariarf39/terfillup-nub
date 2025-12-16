# 🎓 NUB Student Portal TER Automation

This repository contains a **single Python automation script** that uses **Playwright** to automatically complete and submit the **Teacher Evaluation Report (TER)** on the **NUB Student Portal**.

All functionality is implemented in **one file only**, making it easy to run, modify, and maintain.

---

## 🚀 Features

* Automated login using Student ID & Password
* Automatic navigation to **TER Fill Up**
* Course and section selection
* Auto-answering all TER questions
* Feedback text auto-fill (Like / Dislike)
* TER form submission
* Runs in visible (non-headless) browser mode

---

## 🛠️ Technology Stack

* **Language:** Python 3
* **Automation Framework:** Playwright (Sync API)
* **Browser:** Chromium

---

## 📄 Project File

```
ter_automation.py   ← Single file containing the full automation logic
```

No additional folders, configuration files, or modules are required.

---

## ⚙️ Requirements

* Python **3.8 or higher**
* pip (Python package manager)

---

## 📦 Installation

Install Playwright and required browser:

```bash
pip install playwright
playwright install
```

---

## ▶️ How to Run

```bash
python ter_automation.py
```

The browser will open automatically and complete the TER submission process.

---

## 🔧 Configuration

Edit the same Python file to update your credentials:

```python
page.get_by_placeholder("Student ID").fill("YOUR_STUDENT_ID")
page.get_by_placeholder("Password").fill("YOUR_PASSWORD")
```

### 📝 Feedback Customization

```python
page.get_by_label("What did you like about this").fill("behaviour is good . teaching style also good")
page.get_by_label("What did you dislike about").fill("i don't dislike")
```

---

## 🧪 Browser Mode

Current setting:

```python
headless=False
```

To run silently without UI:

```python
headless=True
```

---

## ⚠️ Disclaimer

> This script is intended **for personal and educational use only**.
> Do not use it to violate university rules, policies, or system terms.

---

## 🔐 Security Notice

* Never upload real credentials to GitHub
* Always remove or replace sensitive information before committing

---

## 👨‍💻 Author

**Md Fahim Shariar**
App Developer | Flutter | Java | Laravel | Cyber Security

GitHub: [https://github.com/shariarf39](https://github.com/shariarf39)

---

⭐ If this project helped you, please give the repository a **star**.
