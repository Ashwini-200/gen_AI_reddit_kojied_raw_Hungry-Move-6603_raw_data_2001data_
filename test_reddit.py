import praw
from dotenv import load_dotenv
import os

# Load .env variables
load_dotenv()

# Read your .env values
client_id = os.getenv("REDDIT_CLIENT_ID")
client_secret = os.getenv("REDDIT_CLIENT_SECRET")
username = os.getenv("REDDIT_USERNAME")
password = os.getenv("REDDIT_PASSWORD")

# Create Reddit instance
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    username=username,
    password=password,
    user_agent=f"Reddit Persona Script by u/{username}"
)

# Test: Print your logged in user
print("✅ Logged in as:", reddit.user.me())

# Test: Fetch latest 5 posts by any user
print("\n🔍 Latest 5 posts by u/kojied:")
user = reddit.redditor("kojied")
for submission in user.submissions.new(limit=5):
    print(f"- {submission.title} | {submission.url}")
