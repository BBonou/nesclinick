from sqlalchemy import text
from database import engine


def list_ordonnances():
    try:
        with engine.connect() as conn:
            result = conn.execute(
                text("""
                     SELECT * FROM ordonnance
                 """)
            )
        return result.fetchall()
    except Exception as e:
        print(f"Erreur : {e}")


def add_ordonnance(num_consultation, reference, posologie, duree):
    try:
        with engine.begin() as conn:
            conn.execute(
                text("""
                    INSERT INTO ordonnance
                    (num_consultation, reference, posologie, duree)
                    VALUES (:num_consultation, :reference, :posologie, :duree)
                """),
                {
                    "num_consultation": num_consultation,
                    "reference": reference,
                    "posologie": posologie,
                    "duree": duree
                }
            )
    except Exception as e:
        print(f"Erreur : {e}")


def delete_ordonnance(num_consultation, reference):
    try:
        with engine.begin() as conn:
            conn.execute(
                text("""
                    DELETE FROM ordonnance
                    WHERE num_consultation = :num_consultation
                    AND reference = :reference
                """),
                {
                    "num_consultation": num_consultation,
                    "reference": reference
                }
            )
    except Exception as e:
        print(f"Erreur : {e}")


def update_ordonnance(num_consultation, reference, posologie, duree):
    try:
        with engine.begin() as conn:
            conn.execute(
                text("""
                    UPDATE ordonnance
                    SET posologie = :posologie,
                        duree = :duree
                    WHERE num_consultation = :num_consultation
                    AND reference = :reference
                """),
                {
                    "num_consultation": num_consultation,
                    "reference": reference,
                    "posologie": posologie,
                    "duree": duree
                }
            )
    except Exception as e:
        print(f"Erreur : {e}")


def search_ordonnance(num_consultation, reference):
    try:
        with engine.begin() as conn:
            result = conn.execute(
                text("""
                    SELECT * FROM ordonnance
                    WHERE num_consultation = :num_consultation
                    AND reference = :reference
                """),
                {
                    "num_consultation": num_consultation,
                    "reference": reference
                }
            )
        return result.fetchall()
    except Exception as e:
        print(f"Erreur : {e}")


def ordonnance_exists(num_consultation, reference):
    try:
        with engine.begin() as conn:
            result = conn.execute(
                text("""
                    SELECT COUNT(*) FROM ordonnance
                    WHERE num_consultation = :num_consultation
                    AND reference = :reference
                """),
                {
                    "num_consultation": num_consultation,
                    "reference": reference
                }
            )
        return result.scalar() > 0
    except Exception as e:
        print(f"Erreur : {e}")