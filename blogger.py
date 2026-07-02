import os
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/blogger"]


def publish_to_blogger(title, content):
    blog_id = "6527685220934804145"

    creds = Credentials(
        token=None,
        refresh_token=os.environ["BLOGGER_REFRESH_TOKEN"],
        token_uri="https://oauth2.googleapis.com/token",
        client_id=os.environ["BLOGGER_CLIENT_ID"],
        client_secret=os.environ["BLOGGER_CLIENT_SECRET"],
        scopes=SCOPES,
    )

    # Exchange the refresh token for a fresh access token
    creds.refresh(Request())

    service = build("blogger", "v3", credentials=creds)

    post = {
        "kind": "blogger#post",
        "title": title,
        "content": content,
    }

    result = service.posts().insert(
        blogId=BLOG_ID,
        body=post,
        isDraft=False,
    ).execute()

    print("✅ Blogger post published!")
    print(result["url"])

    return result["url"]
