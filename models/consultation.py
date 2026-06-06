from sqlalchemy import text
from sqlalchemy.ext.asyncio import result

from database import engine


def list_consultations():
    try:
        with engine.connect() as conn:
            result = conn.execute(
                text("""
                    SELECT * FROM consultation      
                """)
            )
        return result.fetchall()
    except Exception as e:
        print(f"Erreur : {e}")


def add_consultation(date, diagnostic, motant, num_veterinaire, num_animal):
    try:
        with engine.connect() as conn:
            conn.execute(
                text("""
                    INSERT INTO consultation
                    (date, diagnostic, montant, num_vet, num_animal)
                    VALUES (:date, :diagnostic, :montant, :num_vet, :num_animal)
                """),
                {
                    "date": date,
                    "diagnostic": diagnostic,
                    "montant": motant,
                    "num_vet": num_veterinaire,
                    "num_animal": num_animal
                }
            )
    except Exception as e:
        print(f"Erreur : {e}")


def delete_consultation(num_consultation):
    try:
        with engine.connect() as conn:
            conn.execute(
                text("""
                    DELETE FROM consultation
                    WHERE num_consultation = :num_consultation
                """),
                {
                    "num_consultation": num_consultation
                }
            )
    except Exception as e:
        print(f"Erreur : {e}")


def update_consultation(num_consultation, date, diagnostic, montant, num_vet, num_animal):
    try:
        with engine.connect() as conn:
            conn.execute(
                text("""
                    UPDATE consultation
                    SET num_consultation = :num_consultation,
                        date = :date,
                        diagnostic = :diagnostic,
                        montant = :montant,
                        num_vet = :num_vet,
                        num_animal = :num_animal
                    WHERE num_consultation = :num_consultation
                """),
                {
                    "num_consultation": num_consultation,
                    "date": date,
                    "diagnostic": diagnostic,
                    "montant": montant,
                    "num_vet": num_vet,
                    "num_animal": num_animal
                }
            )
    except Exception as e:
        print(f"Erreur : {e}")


def search_consultation_interval(start_date, end_date):
    try:
        with engine.connect() as conn:
            result = conn.execute(
                text("""
                    SELECT * FROM consultation
                    WHERE date BETWEEN :start_date AND :end_date
                """),
                {
                    "start_date": start_date,
                    "end_date": end_date
                }
            )
        return result.fetchall()
    except Exception as e:
        print(f"Erreur : {e}")


def consultation_exists(num_animal, date):
    try:
        with engine.connect() as conn:
            result = conn.execute(
                text("""
                    SELECT COUNT(*) FROM consultation
                    WHERE num_animal = :num_animal
                    AND DATE(date) = :date
                """),
                {
                    "num_animal": num_animal,
                    "date": date
                }
            )
        return result.scalar() > 0
    except Exception as e:
        print(f"Erreur : {e}")