from sqlalchemy import text

from database import engine


def list_medicaments():
    try:
        with engine.connect() as conn:
            result = conn.execute(
                text("""
                     SELECT * FROM medicament
                 """)
            )
        return result.fetchall()
    except Exception as e:
        print(f"Erreur : {e}")


def add_medicament(reference, nom, dosage, prix_unitaire, stock):
    try:
        with engine.begin() as conn:
            conn.execute(
                text("""
                    INSERT INTO medicament
                    (reference, nom, dosage, prix_unitaire, stock)
                    VALUES (:reference, :nom, :dosage, :prix_unitaire, :stock)
                """),
                {
                    "reference": reference,
                    "nom": nom,
                    "dosage": dosage,
                    "prix_unitaire": prix_unitaire,
                    "stock": stock
                }
            )
    except Exception as e:
        print(f"Erreur : {e}")


def delete_medicament(reference):
    try:
        with engine.begin() as conn:
            conn.execute(
                text("""
                    DELETE FROM medicament
                    WHERE reference = :reference
                """),
                {
                    "reference": reference
                }
            )
    except Exception as e:
        print(f"Erreur : {e}")



def update_medicament(reference, nom, dosage, prix_unitaire, stock):
    try:
        with engine.begin() as conn:
            conn.execute(
                text("""
                    UPDATE medicament
                    SET nom = :nom,
                        dosage = :dosage,
                        prix_unitaire = :prix_unitaire,
                        stock = :stock
                    WHERE reference = :reference
                """),
                {
                    "reference": reference,
                    "nom": nom,
                    "dosage": dosage,
                    "prix_unitaire": prix_unitaire,
                    "stock": stock
                }
            )
    except Exception as e:
        print(f"Erreur : {e}")


def search_medicament_by_reference(reference):
    try:
        with engine.begin() as conn:
            result = conn.execute(
                text("""
                    SELECT * FROM medicament
                    WHERE reference LIKE :reference    
                """),
                {
                    "reference": f"%{reference}%"
                }
            )
        return result.fetchall()
    except Exception as e:
        print(f"Erreur : {e}")


def search_medicament_by_nom(nom):
    try:
        with engine.begin() as conn:
            result = conn.execute(
                text("""
                    SELECT * FROM medicament
                    WHERE nom LIKE :nom 
                """),
                {
                    "nom": f"%{nom}%"
                }
            )
        return result.fetchall()
    except Exception as e:
        print(f"Erreur : {e}")