from sqlalchemy import text
from database import engine


def list_animal():
    try:
        with engine.connect() as conn:
            result = conn.execute(
                text("""
                    SELECT * FROM animal
                """)
            )
        return result.fetchall()
    except Exception as e:
        print(f"Erreur : {e}")


def add_animal(nom_animal, espece_animal, race_animal, date_naissance_animal, num_proprietaire_animal):
    try:
        with engine.begin() as conn:
            conn.execute(
                text("""
                    INSERT INTO animal
                    (nom_animal, espece, race, date_naissance, num_proprietaire)
                    VALUES (:nom, :espece, :race, :date_naissance, :num_proprietaire)
                """),
                {
                    "nom": nom_animal,
                    "espece": espece_animal,
                    "race": race_animal,
                    "date_naissance": date_naissance_animal,
                    "num_proprietaire": num_proprietaire_animal
                }
            )
    except Exception as e:
        print(f"Erreur : {e}")


def delete_animal(num_animal):
    try:
        with engine.begin() as conn:
            conn.execute(
                text("""
                    DELETE FROM animal
                    WHERE num_animal = :numAnimal
                """),
                {
                    "numAnimal": num_animal
                }
            )
    except Exception as e:
        print(f"Erreur : {e}")


def update_animal(num_animal, nom_animal, espece_animal, race_animal, date_naissance_animal, num_proprietaire_animal):
    try:
        with engine.begin() as conn:
            conn.execute(
                text("""
                    UPDATE animal
                    SET nom_animal = :nom_animal,
                        espece = :espece,
                        race = :race,
                        date_naissance = :date_naissance,
                        num_proprietaire = :num_proprietaire
                    WHERE num_animal = :numAnimal
                """),
                {
                    "numAnimal": num_animal,
                    "nom_animal": nom_animal,
                    "espece": espece_animal,
                    "race": race_animal,
                    "date_naissance": date_naissance_animal,
                    "num_proprietaire": num_proprietaire_animal
                }
            )
    except Exception as e:
        print(f"Erreur : {e}")

def search_animal_by_name(nom_animal):
    try:
        with engine.begin() as conn:
            result = conn.execute(
                text("""
                    SELECT * FROM animal
                    WHERE nom_animal LIKE :nom_animal
                """),
                {
                    "nom_animal": f"%{nom_animal}%"
                }
            )
        return result.fetchall()
    except Exception as e:
        print(f"Erreur : {e}")

def search_animal_by_species(espece_animal):
    try:
        with engine.begin() as conn:
            result = conn.execute(
                text("""
                    SELECT * FROM animal
                    WHERE espece LIKE :espece_animal
                """),
                {
                    "espece_animal": f"%{espece_animal}%"
                }
            )
        return result.fetchall()
    except Exception as e:
        print(f"Erreur : {e}")


def animal_exists(num_animal, num_proprietaire):
    try:
        with engine.begin() as conn:
            result = conn.execute(
                text("""
                    SELECT COUNT(*) FROM animal
                    WHERE num_animal = :num_animal
                    AND num_proprietaire = :num_proprietaire
                """),
                {
                    "num_animal": num_animal,
                    "num_proprietaire": num_proprietaire
                }
            )
        return result.scalar() > 0
    except Exception as e:
        print(f"Erreur : {e}")