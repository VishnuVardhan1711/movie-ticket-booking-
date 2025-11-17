from flask import Flask, render_template, request

app = Flask(__name__)

# Dummy movie list
movies = [
    {"id": 1, "name": "Avengers: Endgame"},
    {"id": 2, "name": "Inception"},
    {"id": 3, "name": "Interstellar"},
    {"id": 4, "name": "The Dark Knight"}
]

@app.route("/")
def index():
    return render_template("index.html", movies=movies)

@app.route("/book/<int:movie_id>")
def book(movie_id):
    selected = next((m for m in movies if m["id"] == movie_id), None)
    return render_template("book.html", movie=selected)

@app.route("/confirm", methods=["POST"])
def confirm():
    name = request.form["name"]
    movie = request.form["movie"]
    seats = request.form["seats"]
    time = request.form["time"]
    return render_template("success.html", name=name, movie=movie, seats=seats, time=time)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
