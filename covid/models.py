from covid.extensions import db

class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    population = db.Column(db.Integer)
    income = db.Column(db.String(50))  # <-- FIXED
    life_expectancy = db.Column(db.Float)  # CSV doesn't have it, can remove or keep as optional
    covid_stats = db.relationship('CovidStat', backref='country', lazy=True)

class CovidStat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    cases = db.Column(db.Integer)
    deaths = db.Column(db.Integer)
    recoveries = db.Column(db.Integer)
