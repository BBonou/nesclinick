from sqlalchemy import text
from database import engine


def list_paiements():
    try:
        with engine.connect() as conn:
            result = conn.execute(
                text("""
                     SELECT * FROM paiement
                """)
            )
        return result.fetchall()
    except Exception as e:
        print(f"Erreur : {e}")


def add_paiement(montant, date_pay, mode_pay, num_consultation):
    try:
        with engine.begin() as conn:
            conn.execute(
                text("""
                    INSERT INTO paiement
                    (montant, date_pay, mode_pay, num_consultation)
                    VALUES (:montant, :date_pay, :mode_pay, :num_consultation)
                """),
            {
                "montant": montant,
                "date_pay": date_pay,
                "mode_pay": mode_pay,
                "num_consultation": num_consultation
            }
        )
    except Exception as e:
        print(f"Erreur : {e}")


def delete_paiement(num_paiement):
    try:
        with engine.begin() as conn:
            conn.execute(
                text("""
                    DELETE FROM paiement
                    WHERE num_pay = :num_paiement
                """),
                {
                    "num_paiement": num_paiement
                }
            )
    except Exception as e:
        print(f"Erreur : {e}")


def update_paiement(num_paiement, montant, date_pay, mode_pay, num_consultation):
    try:
        with engine.begin() as conn:
            conn.execute(
                text("""
                    UPDATE paiement
                    SET montant = :montant,
                        date_pay = :date_pay,
                        mode_pay = :mode_pay,
                        num_consultation = :num_consultation
                    WHERE num_pay = :num_paiement
                """),
                {
                    "num_paiement": num_paiement,
                    "montant": montant,
                    "date_pay": date_pay,
                    "mode_pay": mode_pay,
                    "num_consultation": num_consultation
                }
            )
    except Exception as e:
        print(f"Erreur : {e}")


def search_paiement_by_id(num_paiement):
    try:
        with engine.begin() as conn:
            result = conn.execute(
                text("""
                    SELECT * FROM paiement
                    WHERE num_pay = :num_paiement
                """),
                {
                    "num_paiement": num_paiement
                }
            )
        return result.fetchall()
    except Exception as e:
        print(f"Erreur : {e}")


def search_paiement_by_consultation(num_consultation):
    try:
        with engine.begin() as conn:
            result = conn.execute(
                text("""
                        SELECT * FROM paiement
                        WHERE num_consultation = :num_consultation
                    """),
                {
                    "num_consultation": num_consultation
                }
            )
        return result.fetchall()
    except Exception as e:
        print(f"Erreur : {e}")