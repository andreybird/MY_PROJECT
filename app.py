from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/plots')
def plots():
    return render_template("plots.html")


@app.route('/MedianAgeCovidSmallPlot')
def MedianAgeCovidSmall():
    return render_template("MedianAge_CovidSmall.html")


@app.route('/MedianAgeCovidBigPlot')
def MedianAgeCovidBig():
    return render_template("MedianAge_CovidBig.html")


@app.route('/GiniCovid')
def GiniCovid():
    return render_template("Gini coefficient_Covid.html")


@app.route('/IndexCovid')
def IndexCovid():
    return render_template("Index of trust_Covid.html")

@app.route('/GiniAge')
def GiniAge():
    return render_template("AgeOnGini.html")


if __name__ == "__main__":
    app.run(debug=True)
