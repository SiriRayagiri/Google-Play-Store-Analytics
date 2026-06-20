from google_play_scraper import app

result = app(
    'com.whatsapp',
    lang='en',
    country='us'
)

print("App Name:", result['title'])
print("Rating:", result['score'])
print("Installs:", result['installs'])
print("Reviews:", result['reviews'])
print("Genre:", result['genre'])
print("Developer:", result['developer'])