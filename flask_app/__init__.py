from flask import Flask
from flask import render_template, request, session


# 使 Flask 框架知道去哪里寻找代码
app = Flask("time_series_analysis")


@app.route('/')
def go_to_homepage():
    return render_template("home.html")


@app.route("/classic_module")
@app.route("/classic_module/<url_name>")
def go_to_classic_module(request, url_name=""):
    return render_template("classic_module.html")


@app.route("/dtw_analysis")
@app.route("/dtw_analysis/<url_name>")
def go_to_dtw_module(request, url_name=""):
    return render_template("dtw_analysis.html")


if __name__ == "__main__":
    app.run()
