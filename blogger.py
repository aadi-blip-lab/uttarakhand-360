from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/blogger"]
BLOG_ID = "2861908869738357216"


def publish_to_blogger(title, content):
    flow = InstalledAppFlow.from_client_secrets_file(
        "client_secret.json",
        SCOPES
    )

    creds = flow.run_local_server(port=0)

    service = build("blogger", "v3", credentials=creds)

    post = {
        "title": title,
        "content": content
    }

    result = service.posts().insert(
        blogId=BLOG_ID,
        body=post,
        isDraft=False
    ).execute()

    print("✅ Blogger post published!")
    print(result["url"])
