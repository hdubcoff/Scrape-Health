from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Homepage route
@app.route("/")
def home():
    return "Welcome to Scrape-Health! Visit /recipes to see functional recipes."

# Recipe scraping function
def scrape_ifm_recipes():
    url = "https://www.ifm.org/functional-medicine/food-plans/"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    recipe_links = soup.select("a[href*='recipe']")
    recipes = []

    for a in recipe_links:
        title = a.text.strip()
        link = a["href"]
        recipes.append({"title": title, "url": link})

    return recipes

# Recipes route
@app.route("/recipes")
def get_recipes():
    blood_sugar = request.args.get("blood_sugar", default="normal")
    sleep_score = request.args.get("sleep_score", default="good")

    # TODO: use blood_sugar and sleep_score in the future for filtering
    recipes = scrape_ifm_recipes()
    return jsonify(recipes)

# Run app locally (Render uses gunicorn, so this won’t run in production)
if __name__ == "__main__":
    app.run(debug=True)
