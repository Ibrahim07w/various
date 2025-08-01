# 📬 Hacker News Newsletter Email Bot

This Python script automatically scrapes the top stories from [Hacker News](https://news.ycombinator.com/) and sends them as a formatted HTML email to a specified recipient.

---

## 🚀 Features

- 🔍 Extracts the latest top stories from Hacker News
- 📨 Sends email using Gmail SMTP with HTML formatting
- 🔒 Uses secure TLS connection for sending
- 📅 Includes automatic timestamp in the email subject
- 🐍 Built with Python and standard libraries

---

## 🛠️ Technologies

- `requests` – for fetching the webpage
- `beautifulsoup4` – for parsing HTML
- `smtplib` & `email.mime` – for composing and sending the email
- `datetime` – for adding timestamps
