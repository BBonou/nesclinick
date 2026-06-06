from sqlalchemy import text
from database import engine


def list_veterinaires():
    try:
        with engine.connect() as conn:
            results = conn.execute(
                text("""
                    SELECT * FROM veterinaire
                """)
            )
        return results.fetchall()
    except Exception as e:
        print(f"Erreur : {e}")


def add_veterinaire(nom_veterinaire, prenom_veterinaire, specialite):
    try:
        with engine.connect() as conn:
            conn.execute(
                text("""
                    INSERT INTO veterinaire
                    (nom_vet, prenom_vet, specilite)
                    VALUES (:nom_vet, :prenom_vet, :specialite)
                """),
                {
                    "nom_vet": nom_veterinaire,
                    "prenom_vet": prenom_veterinaire,
                    "specilite": specialite
                }
            )
    except Exception as e:
        print(f"Erreur : {e}")


def delete_veterinaire(num_veterinaire):
    try:
        with engine.connect() as conn:
            conn.execute(
                text("""
                    DELETE FROM veterinaire
                    WHERE num_vet = :num_vet
                """),
                {
                    "num_vet": num_veterinaire
                }
            )
    except Exception as e:
        print(f"Erreur : {e}")


def update_veterinaire(num_veterinaire, nom_veterinaire, prenom_veterinaire, specialite):
    try:
        with engine.connect() as conn:
            conn.execute(
                text("""
                    UPDATE veterinaire
                    SET nom_vet = :nom_veterinaire,
                        prenom_vet = :prenom_veterinaire,
                        specialite = :specialite,
                    WHERE num_vet = :num_veterinaire
                """),
                {
                    "num_vet": num_veterinaire,
                    "nom_vet": nom_veterinaire,
                    "prenom_vet": prenom_veterinaire,
                    "specialite": specialite,
                }
            )
    except Exception as e:
        print(f"Erreur : {e}")


def search_veterinaire_by_name(nom_veterinaire):
    try:
        with engine.connect() as conn:
            result = conn.execute(
                text("""
                    SELECT * FROM veterinaire
                    WHERE nom_vet LIKE :nom_veterinaire
                """),
                {
                    "nom": f"%{nom_veterinaire}%"
                }
            )
        return result.fetchall()
    except Exception as e:
        print(f"Erreur : {e}")


def search_veterinaire_by_surname(prenom_veterinaire):
    try:
        with engine.connect() as conn:
            result = conn.execute(
                text("""
                    SELECT * FROM veterinaire
                    WHERE prenom_vet LIKE :prenom_veterinaire
                """),
                {
                    "prenom_vet": f"%{prenom_veterinaire}%"
                }
            )
        return result.fetchall()
    except Exception as e:
        print(f"Erreur : {e}")


def search_veterinaire_by_speciality(specialite):
    try:
        with engine.connect() as conn:
            result = conn.execute(
                text("""
                    SELECT * FROM veterinaire
                    WHERE specialite = :specialite
                """),
                {
                    "specialite": specialite
                }
            )
        return result.fetchall()
    except Exception as e:
        print(f"Erreur : {e}")


def veterinaire_exists(num_veterinaire):
    try:
        with engine.connect() as conn:
            result = conn.execute(
                text("""
                    SELECT COUNT(*) FROM veterinaire
                    WHERE num_veterinaire = :num_veterinaire
                """),
                {
                    "num_vetrinaire": num_veterinaire
                }
            )
        return result.scalar() > 0
    except Exception as e:
        print(f"Erreur : {e}")