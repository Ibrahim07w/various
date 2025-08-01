# 📬 Hacker News Newsletter Email Bot

This Python script scrapes the top stories from [Hacker News](https://news.ycombinator.com/) and sends them as a nicely formatted HTML email using Gmail SMTP. Ideal for setting up a daily tech newsletter for yourself or your team.

---

## 🚀 Features

- Scrapes top headlines from Hacker News
- Composes an HTML email with clickable article links
- Uses Gmail SMTP to send emails securely
- Automatically includes the date in the subject line
- Simple and customizable for other sources

---

## 🛠️ Technologies Used

- `requests` – to fetch Hacker News HTML
- `beautifulsoup4` – to parse and extract story links
- `email.mime` & `smtplib` – for sending formatted HTML emails
- `datetime` – for timestamps in the subject
