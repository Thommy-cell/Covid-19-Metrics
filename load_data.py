import pandas as pd
from datetime import datetime
from app import create_app, db
from app.models import Country, CovidStat

app = create_app()

def load_data():
    df = pd.read_csv("global_covid.csv")

    # Clean column names
    df.columns = df.columns.str.strip()

    for _, row in df.iterrows():
        country_name = row['Country']
        population = row.get('Population', None)
        income = row.get('Income', None)

        # Create or get country
        country = Country.query.filter_by(name=country_name).first()
        if not country:
            country = Country(
                name=country_name,
                population=int(population) if pd.notna(population) else None,
                income=income,
                life_expectancy=None  # CSV has no such column
            )
            db.session.add(country)
            db.session.flush()

        # Parse date
        try:
            date = datetime.strptime(row['Date'], "%d/%m/%Y")
        except ValueError:
            print(f"Invalid date format: {row['Date']}")
            continue

        covid_stat = CovidStat(
            country_id=country.id,
            date=date,
            cases=int(row['Confirmed Cases']) if pd.notna(row['Confirmed Cases']) else None,
            deaths=int(row['Confirmed Deaths']) if pd.notna(row['Confirmed Deaths']) else None,
            recoveries=None  # Not in your CSV
        )

        db.session.add(covid_stat)

    db.session.commit()
    print("Data loaded successfully.")

if __name__ == "__main__":
    with app.app_context():
        load_data()
