
import requests
api_key = "be8bf552000159fb743078aec27cb9d5"
id= "624860"

params = {
    "api_key": api_key,
    "language": "en-US",
}

response = requests.get(url=f"https://api.themoviedb.org/3/movie/{id}", params=params)
response.raise_for_status()

data = response.json()
print(data["overview"])
