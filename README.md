# Reddit User Persona Extractor

This repository contains a simple Python script that:
- Takes a Reddit username as input.
- Scrapes the user’s posts and comments.
- Saves the raw data to a `.txt` file.
- (Optional) Uses an LLM to generate a user persona based on the scraped data.

---

## 📌 Requirements

- Python 3.x
- `praw` for Reddit API
- `dotenv` for environment variables
- OpenAI or any LLM (optional for persona generation)

---

## 📌 Setup Instructions

1️⃣ **Clone this repository**

```bash
git clone https://github.com/<your-username>/user-persona-extractor.git
cd user-persona-extractor
