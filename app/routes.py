from flask import Blueprint, render_template
import pandas as pd

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/view-csv')
def view_csv():
    df = pd.read_csv("global_covid.csv")
    df.columns = df.columns.str.strip()
    data = df.to_dict(orient="records")
    columns = df.columns.tolist()
    return render_template("view_csv.html", data=data, columns=columns)
