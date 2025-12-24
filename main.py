from src.extract.users import get_users
from src.transform.transform import generate_ai_news
from src.load.load import update_user

def main():
    users = get_users()

    for user in users:
        # TRANSFORM (IA ou mock)
        news_text = generate_ai_news(user)

        user["news"].append({
            "icon": "https://img.icons8.com/ios-filled/50/info.png",
            "description": news_text
        })

        # LOAD
        success = update_user(user)
        print(f"{user['name']} updated? {success}")

if __name__ == "__main__":
    main()
