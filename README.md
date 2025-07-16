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
https://github.com/Ashwini-200/gen_AI_reddit_kojied_raw_Hungry-Move-6603_raw_data_2001data_

2️⃣ Install dependencies

pip install -r requirements.txt

3️⃣ Create a .env file

REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
REDDIT_USERNAME=your_reddit_username
REDDIT_PASSWORD=your_reddit_password
OPENAI_API_KEY=your_openai_api_key  # Optional, for persona step

4️⃣ Run test script

python test_reddit.py

You should see:✅ Logged in as: your_reddit_username
5️⃣ Run scraper
python reddit_scraper.py


