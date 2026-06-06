import sys
import termios

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from rich import box

# ===========================================================================
# IMPORTS — les fichiers du dossier models/ (renommer zip/ en models/)
# ===========================================================================

from models.animal import (
    list_animal,
    add_animal,
    delete_animal,
    update_animal,
    search_animal_by_name,
    search_animal_by_species,
)

from models.proprietaire import (
    list_proprietaires,
    add_proprietaire,
    delete_proprietaire,
    update_proprietaire,
    search_proprietaire_by_name,
    search_proprietaire_by_surname,
    search_proprietaire_by_telephone,
)

from models.consultation import (
    list_consultations,
    add_consultation,
    delete_consultation,
    update_consultation,
    search_consultation_interval,
)

from models.medicament import (
    list_medicaments,
    add_medicament,
    delete_medicament,
    update_medicament,
    search_medicament_by_reference,
    search_medicament_by_nom,
)

from models.ordonnance import (
    list_ordonnances,
    add_ordonnance,
    delete_ordonnance,
    update_ordonnance,
    search_ordonnance,
)

from models.paiement import (
    list_paiements,
    add_paiement,
    delete_paiement,
    update_paiement,
    search_paiement_by_id,
    search_paiement_by_consultation,
)

from models.veterinaire import (
    list_veterinaires,
    add_veterinaire,
    delete_veterinaire,
    update_veterinaire,
    search_veterinaire_by_name,
    search_veterinaire_by_surname,
    search_veterinaire_by_speciality,
)

console = Console()


# ===========================================================================
# UTILITAIRES
# ===========================================================================

def flush_stdin():
    """Vide le buffer stdin pour éviter que les Entrées en trop cassent l'interface."""
    try:
        termios.tcflush(sys.stdin, termios.TCIFLUSH)
    except Exception:
        pass


def ask(label, default=None):
    """Prompt sécurisé : vide le buffer avant de lire."""
    flush_stdin()
    return Prompt.ask(label, default=default)


def pause():
    """Pause sécurisée : vide le buffer après lecture."""
    flush_stdin()
    input("\n  Appuie sur Entrée pour continuer...")
    flush_stdin()


def clear():
    console.clear()


def header(titre="CLINIQUE VÉTÉRINAIRE - SYSTÈME DE GESTION"):
    clear()
    console.print(
        Panel.fit(
            f"[bold cyan]{titre}[/bold cyan]\n"
            "[dim]Gestion des animaux, consultations, médicaments et paiements[/dim]",
            box=box.DOUBLE,
        )
    )


def exit_check(choice):
    return choice.strip().lower() in ["\\q", "\\exit", "q", "exit", "0"]


def show_table(rows):
    if not rows:
        console.print("\n  [yellow]⚠  Aucun résultat trouvé.[/yellow]")
        return

    table = Table(show_header=True, header_style="bold cyan", box=box.SIMPLE_HEAVY)
    columns = rows[0]._mapping.keys()
    for col in columns:
        table.add_column(str(col))
    for row in rows:
        table.add_row(*[str(v) if v is not None else "-" for v in row])

    console.print()
    console.print(table)


def confirm(msg="Confirmer ? (o/n)"):
    flush_stdin()
    rep = Prompt.ask(msg, choices=["o", "n"], default="n")
    flush_stdin()
    return rep == "o"


def ok(msg="Opération réussie"):
    console.print(f"\n  [bold green]✔  {msg}[/bold green]")


def err(msg="Une erreur est survenue"):
    console.print(f"\n  [bold red]✖  {msg}[/bold red]")


# ===========================================================================
# MENU PRINCIPAL
# ===========================================================================

def main_menu():
    while True:
        header()
        console.print()
        console.print("  [bold][1][/bold]  Propriétaires")
        console.print("  [bold][2][/bold]  Animaux")
        console.print("  [bold][3][/bold]  Consultations")
        console.print("  [bold][4][/bold]  Médicaments")
        console.print("  [bold][5][/bold]  Ordonnances")
        console.print("  [bold][6][/bold]  Paiements")
        console.print("  [bold][7][/bold]  Vétérinaires")
        console.print("  [bold][0][/bold]  Quitter")

        choice = ask("\nChoix").strip()

        if exit_check(choice):
            break
        elif choice == "1":
            proprietaire_menu()
        elif choice == "2":
            animal_menu()
        elif choice == "3":
            consultation_menu()
        elif choice == "4":
            medicament_menu()
        elif choice == "5":
            ordonnance_menu()
        elif choice == "6":
            paiement_menu()
        elif choice == "7":
            veterinaire_menu()


# ===========================================================================
# PROPRIÉTAIRES
# ===========================================================================

def proprietaire_menu():
    while True:
        header("PROPRIÉTAIRES")
        console.print()
        console.print("  [bold][1][/bold]  Lister tous")
        console.print("  [bold][2][/bold]  Ajouter")
        console.print("  [bold][3][/bold]  Modifier")
        console.print("  [bold][4][/bold]  Supprimer")
        console.print("  [bold][5][/bold]  Rechercher par nom")
        console.print("  [bold][6][/bold]  Rechercher par prénom")
        console.print("  [bold][7][/bold]  Rechercher par téléphone")
        console.print("  [bold][0][/bold]  Retour")

        choice = ask("\nChoix").strip()
        if exit_check(choice):
            break

        if choice == "1":
            header("PROPRIÉTAIRES — Liste")
            show_table(list_proprietaires())
            pause()

        elif choice == "2":
            header("PROPRIÉTAIRES — Ajouter")
            nom      = ask("Nom")
            prenom   = ask("Prénom")
            tel      = ask("Téléphone")
            adresse  = ask("Adresse")
            add_proprietaire(nom, prenom, tel, adresse)
            ok("Propriétaire ajouté.")
            pause()

        elif choice == "3":
            header("PROPRIÉTAIRES — Modifier")
            num = ask("Numéro du propriétaire à modifier")
            console.print("\n  [dim]Laisse vide pour conserver la valeur actuelle.[/dim]")
            nom     = ask("Nouveau nom")
            prenom  = ask("Nouveau prénom")
            tel     = ask("Nouveau téléphone")
            adresse = ask("Nouvelle adresse")
            if confirm():
                update_proprietaire(num, nom, prenom, tel, adresse)
                ok("Propriétaire mis à jour.")
            else:
                console.print("  [yellow]Annulé.[/yellow]")
            pause()

        elif choice == "4":
            header("PROPRIÉTAIRES — Supprimer")
            num = ask("Numéro du propriétaire à supprimer")
            if confirm(f"Supprimer le propriétaire #{num} ? (o/n)"):
                delete_proprietaire(num)
                ok("Propriétaire supprimé.")
            else:
                console.print("  [yellow]Annulé.[/yellow]")
            pause()

        elif choice == "5":
            header("PROPRIÉTAIRES — Recherche par nom")
            nom = ask("Nom")
            show_table(search_proprietaire_by_name(nom))
            pause()

        elif choice == "6":
            header("PROPRIÉTAIRES — Recherche par prénom")
            prenom = ask("Prénom")
            show_table(search_proprietaire_by_surname(prenom))
            pause()

        elif choice == "7":
            header("PROPRIÉTAIRES — Recherche par téléphone")
            tel = ask("Téléphone")
            show_table(search_proprietaire_by_telephone(tel))
            pause()


# ===========================================================================
# ANIMAUX
# ===========================================================================

def animal_menu():
    while True:
        header("ANIMAUX")
        console.print()
        console.print("  [bold][1][/bold]  Lister tous")
        console.print("  [bold][2][/bold]  Ajouter")
        console.print("  [bold][3][/bold]  Modifier")
        console.print("  [bold][4][/bold]  Supprimer")
        console.print("  [bold][5][/bold]  Rechercher par nom")
        console.print("  [bold][6][/bold]  Rechercher par espèce")
        console.print("  [bold][0][/bold]  Retour")

        choice = ask("\nChoix").strip()
        if exit_check(choice):
            break

        if choice == "1":
            header("ANIMAUX — Liste")
            show_table(list_animal())
            pause()

        elif choice == "2":
            header("ANIMAUX — Ajouter")
            nom      = ask("Nom de l'animal")
            espece   = ask("Espèce")
            race     = ask("Race")
            date     = ask("Date de naissance (YYYY-MM-DD)")
            id_prop  = ask("ID propriétaire")
            add_animal(nom, espece, race, date, id_prop)
            ok("Animal ajouté.")
            pause()

        elif choice == "3":
            header("ANIMAUX — Modifier")
            num     = ask("Numéro de l'animal à modifier")
            nom     = ask("Nouveau nom")
            espece  = ask("Nouvelle espèce")
            race    = ask("Nouvelle race")
            date    = ask("Nouvelle date de naissance (YYYY-MM-DD)")
            id_prop = ask("Nouvel ID propriétaire")
            if confirm():
                update_animal(num, nom, espece, race, date, id_prop)
                ok("Animal mis à jour.")
            else:
                console.print("  [yellow]Annulé.[/yellow]")
            pause()

        elif choice == "4":
            header("ANIMAUX — Supprimer")
            num = ask("Numéro de l'animal à supprimer")
            if confirm(f"Supprimer l'animal #{num} ? (o/n)"):
                delete_animal(num)
                ok("Animal supprimé.")
            else:
                console.print("  [yellow]Annulé.[/yellow]")
            pause()

        elif choice == "5":
            header("ANIMAUX — Recherche par nom")
            nom = ask("Nom")
            show_table(search_animal_by_name(nom))
            pause()

        elif choice == "6":
            header("ANIMAUX — Recherche par espèce")
            espece = ask("Espèce")
            show_table(search_animal_by_species(espece))
            pause()


# ===========================================================================
# CONSULTATIONS
# ===========================================================================

def consultation_menu():
    while True:
        header("CONSULTATIONS")
        console.print()
        console.print("  [bold][1][/bold]  Lister toutes")
        console.print("  [bold][2][/bold]  Ajouter")
        console.print("  [bold][3][/bold]  Modifier")
        console.print("  [bold][4][/bold]  Supprimer")
        console.print("  [bold][5][/bold]  Rechercher par intervalle de dates")
        console.print("  [bold][0][/bold]  Retour")

        choice = ask("\nChoix").strip()
        if exit_check(choice):
            break

        if choice == "1":
            header("CONSULTATIONS — Liste")
            show_table(list_consultations())
            pause()

        elif choice == "2":
            header("CONSULTATIONS — Ajouter")
            date      = ask("Date (YYYY-MM-DD)")
            diag      = ask("Diagnostic")
            montant   = ask("Montant")
            id_veto   = ask("ID vétérinaire")
            id_animal = ask("ID animal")
            add_consultation(date, diag, montant, id_veto, id_animal)
            ok("Consultation enregistrée.")
            pause()

        elif choice == "3":
            header("CONSULTATIONS — Modifier")
            num       = ask("Numéro de consultation à modifier")
            date      = ask("Nouvelle date (YYYY-MM-DD)")
            diag      = ask("Nouveau diagnostic")
            montant   = ask("Nouveau montant")
            id_veto   = ask("Nouvel ID vétérinaire")
            id_animal = ask("Nouvel ID animal")
            if confirm():
                update_consultation(num, date, diag, montant, id_veto, id_animal)
                ok("Consultation mise à jour.")
            else:
                console.print("  [yellow]Annulé.[/yellow]")
            pause()

        elif choice == "4":
            header("CONSULTATIONS — Supprimer")
            num = ask("Numéro de consultation à supprimer")
            if confirm(f"Supprimer la consultation #{num} ? (o/n)"):
                delete_consultation(num)
                ok("Consultation supprimée.")
            else:
                console.print("  [yellow]Annulé.[/yellow]")
            pause()

        elif choice == "5":
            header("CONSULTATIONS — Recherche par intervalle")
            debut = ask("Date de début (YYYY-MM-DD)")
            fin   = ask("Date de fin   (YYYY-MM-DD)")
            show_table(search_consultation_interval(debut, fin))
            pause()


# ===========================================================================
# MÉDICAMENTS
# ===========================================================================

def medicament_menu():
    while True:
        header("MÉDICAMENTS")
        console.print()
        console.print("  [bold][1][/bold]  Lister tous")
        console.print("  [bold][2][/bold]  Ajouter")
        console.print("  [bold][3][/bold]  Modifier")
        console.print("  [bold][4][/bold]  Supprimer")
        console.print("  [bold][5][/bold]  Rechercher par référence")
        console.print("  [bold][6][/bold]  Rechercher par nom")
        console.print("  [bold][0][/bold]  Retour")

        choice = ask("\nChoix").strip()
        if exit_check(choice):
            break

        if choice == "1":
            header("MÉDICAMENTS — Liste")
            show_table(list_medicaments())
            pause()

        elif choice == "2":
            header("MÉDICAMENTS — Ajouter")
            ref    = ask("Référence")
            nom    = ask("Nom")
            dosage = ask("Dosage")
            prix   = ask("Prix unitaire")
            stock  = ask("Stock")
            add_medicament(ref, nom, dosage, prix, stock)
            ok("Médicament ajouté.")
            pause()

        elif choice == "3":
            header("MÉDICAMENTS — Modifier")
            ref    = ask("Référence du médicament à modifier")
            nom    = ask("Nouveau nom")
            dosage = ask("Nouveau dosage")
            prix   = ask("Nouveau prix unitaire")
            stock  = ask("Nouveau stock")
            if confirm():
                update_medicament(ref, nom, dosage, prix, stock)
                ok("Médicament mis à jour.")
            else:
                console.print("  [yellow]Annulé.[/yellow]")
            pause()

        elif choice == "4":
            header("MÉDICAMENTS — Supprimer")
            ref = ask("Référence du médicament à supprimer")
            if confirm(f"Supprimer le médicament '{ref}' ? (o/n)"):
                delete_medicament(ref)
                ok("Médicament supprimé.")
            else:
                console.print("  [yellow]Annulé.[/yellow]")
            pause()

        elif choice == "5":
            header("MÉDICAMENTS — Recherche par référence")
            ref = ask("Référence")
            show_table(search_medicament_by_reference(ref))
            pause()

        elif choice == "6":
            header("MÉDICAMENTS — Recherche par nom")
            nom = ask("Nom")
            show_table(search_medicament_by_nom(nom))
            pause()


# ===========================================================================
# ORDONNANCES
# ===========================================================================

def ordonnance_menu():
    while True:
        header("ORDONNANCES")
        console.print()
        console.print("  [bold][1][/bold]  Lister toutes")
        console.print("  [bold][2][/bold]  Ajouter")
        console.print("  [bold][3][/bold]  Modifier")
        console.print("  [bold][4][/bold]  Supprimer")
        console.print("  [bold][5][/bold]  Rechercher (par consultation + médicament)")
        console.print("  [bold][0][/bold]  Retour")

        choice = ask("\nChoix").strip()
        if exit_check(choice):
            break

        if choice == "1":
            header("ORDONNANCES — Liste")
            show_table(list_ordonnances())
            pause()

        elif choice == "2":
            header("ORDONNANCES — Ajouter")
            id_cons   = ask("ID consultation")
            ref       = ask("Référence médicament")
            posologie = ask("Posologie")
            duree     = ask("Durée (jours)")
            add_ordonnance(id_cons, ref, posologie, duree)
            ok("Ordonnance ajoutée.")
            pause()

        elif choice == "3":
            header("ORDONNANCES — Modifier")
            id_cons   = ask("ID consultation")
            ref       = ask("Référence médicament")
            posologie = ask("Nouvelle posologie")
            duree     = ask("Nouvelle durée (jours)")
            if confirm():
                update_ordonnance(id_cons, ref, posologie, duree)
                ok("Ordonnance mise à jour.")
            else:
                console.print("  [yellow]Annulé.[/yellow]")
            pause()

        elif choice == "4":
            header("ORDONNANCES — Supprimer")
            id_cons = ask("ID consultation")
            ref     = ask("Référence médicament")
            if confirm(f"Supprimer l'ordonnance (consultation #{id_cons}, méd. '{ref}') ? (o/n)"):
                delete_ordonnance(id_cons, ref)
                ok("Ordonnance supprimée.")
            else:
                console.print("  [yellow]Annulé.[/yellow]")
            pause()

        elif choice == "5":
            header("ORDONNANCES — Recherche")
            id_cons = ask("ID consultation")
            ref     = ask("Référence médicament")
            show_table(search_ordonnance(id_cons, ref))
            pause()


# ===========================================================================
# PAIEMENTS
# ===========================================================================

def paiement_menu():
    while True:
        header("PAIEMENTS")
        console.print()
        console.print("  [bold][1][/bold]  Lister tous")
        console.print("  [bold][2][/bold]  Ajouter")
        console.print("  [bold][3][/bold]  Modifier")
        console.print("  [bold][4][/bold]  Supprimer")
        console.print("  [bold][5][/bold]  Rechercher par ID paiement")
        console.print("  [bold][6][/bold]  Rechercher par ID consultation")
        console.print("  [bold][0][/bold]  Retour")

        choice = ask("\nChoix").strip()
        if exit_check(choice):
            break

        if choice == "1":
            header("PAIEMENTS — Liste")
            show_table(list_paiements())
            pause()

        elif choice == "2":
            header("PAIEMENTS — Ajouter")
            montant = ask("Montant")
            date    = ask("Date (YYYY-MM-DD)")
            mode    = ask("Mode de paiement (espèces / carte / chèque…)")
            id_cons = ask("ID consultation")
            add_paiement(montant, date, mode, id_cons)
            ok("Paiement enregistré.")
            pause()

        elif choice == "3":
            header("PAIEMENTS — Modifier")
            num     = ask("Numéro du paiement à modifier")
            montant = ask("Nouveau montant")
            date    = ask("Nouvelle date (YYYY-MM-DD)")
            mode    = ask("Nouveau mode de paiement")
            id_cons = ask("Nouvel ID consultation")
            if confirm():
                update_paiement(num, montant, date, mode, id_cons)
                ok("Paiement mis à jour.")
            else:
                console.print("  [yellow]Annulé.[/yellow]")
            pause()

        elif choice == "4":
            header("PAIEMENTS — Supprimer")
            num = ask("Numéro du paiement à supprimer")
            if confirm(f"Supprimer le paiement #{num} ? (o/n)"):
                delete_paiement(num)
                ok("Paiement supprimé.")
            else:
                console.print("  [yellow]Annulé.[/yellow]")
            pause()

        elif choice == "5":
            header("PAIEMENTS — Recherche par ID")
            num = ask("Numéro du paiement")
            show_table(search_paiement_by_id(num))
            pause()

        elif choice == "6":
            header("PAIEMENTS — Recherche par consultation")
            id_cons = ask("ID consultation")
            show_table(search_paiement_by_consultation(id_cons))
            pause()


# ===========================================================================
# VÉTÉRINAIRES
# ===========================================================================

def veterinaire_menu():
    while True:
        header("VÉTÉRINAIRES")
        console.print()
        console.print("  [bold][1][/bold]  Lister tous")
        console.print("  [bold][2][/bold]  Ajouter")
        console.print("  [bold][3][/bold]  Modifier")
        console.print("  [bold][4][/bold]  Supprimer")
        console.print("  [bold][5][/bold]  Rechercher par nom")
        console.print("  [bold][6][/bold]  Rechercher par prénom")
        console.print("  [bold][7][/bold]  Rechercher par spécialité")
        console.print("  [bold][0][/bold]  Retour")

        choice = ask("\nChoix").strip()
        if exit_check(choice):
            break

        if choice == "1":
            header("VÉTÉRINAIRES — Liste")
            show_table(list_veterinaires())
            pause()

        elif choice == "2":
            header("VÉTÉRINAIRES — Ajouter")
            nom        = ask("Nom")
            prenom     = ask("Prénom")
            specialite = ask("Spécialité")
            add_veterinaire(nom, prenom, specialite)
            ok("Vétérinaire ajouté.")
            pause()

        elif choice == "3":
            header("VÉTÉRINAIRES — Modifier")
            num        = ask("Numéro du vétérinaire à modifier")
            nom        = ask("Nouveau nom")
            prenom     = ask("Nouveau prénom")
            specialite = ask("Nouvelle spécialité")
            if confirm():
                update_veterinaire(num, nom, prenom, specialite)
                ok("Vétérinaire mis à jour.")
            else:
                console.print("  [yellow]Annulé.[/yellow]")
            pause()

        elif choice == "4":
            header("VÉTÉRINAIRES — Supprimer")
            num = ask("Numéro du vétérinaire à supprimer")
            if confirm(f"Supprimer le vétérinaire #{num} ? (o/n)"):
                delete_veterinaire(num)
                ok("Vétérinaire supprimé.")
            else:
                console.print("  [yellow]Annulé.[/yellow]")
            pause()

        elif choice == "5":
            header("VÉTÉRINAIRES — Recherche par nom")
            nom = ask("Nom")
            show_table(search_veterinaire_by_name(nom))
            pause()

        elif choice == "6":
            header("VÉTÉRINAIRES — Recherche par prénom")
            prenom = ask("Prénom")
            show_table(search_veterinaire_by_surname(prenom))
            pause()

        elif choice == "7":
            header("VÉTÉRINAIRES — Recherche par spécialité")
            specialite = ask("Spécialité")
            show_table(search_veterinaire_by_speciality(specialite))
            pause()


# ===========================================================================
# ENTRY POINT
# ===========================================================================

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        pass
    finally:
        console.print("\n[bold red]Fermeture du système...[/bold red]")