from sqlalchemy import text
from database import engine


def list_proprietaires():
    try:
        with engine.connect() as conn:
            result = conn.execute(
                text("""
                     SELECT * FROM proprietaire
                """)
            )
        return result.fetchall()
    except Exception as e:
        print(f"Erreur : {e}")


def add_proprietaire(nom, prenom, telephone, adresse):
    try:
        with engine.begin() as conn:
            conn.execute(
                text("""
                    INSERT INTO proprietaire
                    (nom, prenom, telephone, adresse)
                    VALUES (:nom, :prenom, :telephone, :adresse)
                """),
                {
                    "nom": nom,
                    "prenom": prenom,
                    "telephone": telephone,
                    "adresse": adresse
                }
            )
    except Exception as e:
        print(f"Erreur : {e}")


def delete_proprietaire(num_proprietaire):
    try:
        with engine.begin() as conn:
            conn.execute(
                text("""
                    DELETE FROM proprietaire
                    WHERE num_proprietaire = :num_proprietaire
                """),
                {
                    "num_proprietaire": num_proprietaire
                }
            )
    except Exception as e:
        print(f"Erreur : {e}")


def update_proprietaire(num_proprietaire, nom, prenom, telephone, adresse):
    try:
        with engine.begin() as conn:
            conn.execute(
                text("""
                    UPDATE proprietaire
                    SET nom = :nom,
                        prenom = :prenom,
                        telephone = :telephone,
                        adresse = :adresse
                    WHERE num_proprietaire = :num_proprietaire
                """),
                {
                    "num_proprietaire": num_proprietaire,
                    "nom": nom,
                    "prenom": prenom,
                    "telephone": telephone,
                    "adresse": adresse
                }
            )
    except Exception as e:
        print(f"Erreur : {e}")


def search_proprietaire_by_name(nom):
    try:
        with engine.begin() as conn:
            result = conn.execute(
                text("""
                    SELECT * FROM proprietaire
                    WHERE nom LIKE :nom
                """),
                {
                    "nom": f"%{nom}%"
                }
            )
        return result.fetchall()
    except Exception as e:
        print(f"Erreur : {e}")


def search_proprietaire_by_surname(prenom):
    try:
        with engine.begin() as conn:
            result = conn.execute(
                text("""
                    SELECT * FROM proprietaire
                    WHERE prenom LIKE :prenom
                """),
                {
                    "prenom": f"%{prenom}%"
                }
            )
        return result.fetchall()
    except Exception as e:
        print(f"Erreur : {e}")


def search_proprietaire_by_telephone(telephone):
    try:
        with engine.begin() as conn:
            result = conn.execute(
                text("""
                    SELECT * FROM proprietaire
                    WHERE telephone = :telephone
                """),
                {
                    "telephone": telephone
                }
            )
        return result.fetchall()
    except Exception as e:
        print(f"Erreur : {e}")


def search_proprietaire_by_address(adresse):
    try:
        with engine.begin() as conn:
            result = conn.execute(
                text("""
                    SELECT * FROM proprietaire
                    WHERE adress LIKE :adresse
                """),
                {
                    "adresse": f"%{adresse}%"
                }
            )
        return result.fetchall()
    except Exception as e:
        print(f"Erreur : {e}")


def proprietaire_exists(num_proprietaire):
    try:
        with engine.begin() as conn:
            result = conn.execute(
                text("""
                    SELECT COUNT(*) FROM proprietaire
                    WHERE num_proprietaire = :num_proprietaire
                """),
                {
                    "num_proprietaire": num_proprietaire
                }
            )
        return result.scalar() > 0
    except Exception as e:
        print(f"Erreur : {e}")