import requests
import json

def get_google_suggestions(keyword):
    url = f"https://suggestqueries.google.com/complete/search?client=firefox&q={keyword}"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        suggestions = json.loads(response.text)[1]
        return suggestions
    else:
        print("Gagal mengambil data dari Google")
        return []

if __name__ == "__main__":
    keyword = input("Masukkan kata kunci: ")
    suggestions = get_google_suggestions(keyword)
    #output
    print("Keyword populer terkait:")
    for suggestion in suggestions:
        print("-", suggestion)
