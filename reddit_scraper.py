import praw
from dotenv import load_dotenv
import os

# Load .env
load_dotenv()

# Reddit credentials
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

def get_user_data(target_username, post_limit=10, comment_limit=10):
    user = reddit.redditor(target_username)

    posts = []
    comments = []

    for submission in user.submissions.new(limit=post_limit):
        posts.append(f"Title: {submission.title}\nText: {submission.selftext}\nURL: {submission.url}\n")

    for comment in user.comments.new(limit=comment_limit):
        comments.append(f"Comment: {comment.body}\n")

    return posts, comments

def save_raw_data(target_username, posts, comments):
    filename = f"{target_username}_raw_data.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write("=== POSTS ===\n\n")
        for post in posts:
            f.write(post + "\n")

        f.write("\n=== COMMENTS ===\n\n")
        for comment in comments:
            f.write(comment + "\n")

    print(f"✅ Raw data saved to {filename}")

if __name__ == "__main__":
    target_username = input("Enter Reddit username: ")
    posts, comments = get_user_data(target_username)
    save_raw_data(target_username, posts, comments)
