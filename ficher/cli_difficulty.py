import argparse

parser = argparse.ArgumentParser(description="Système de gestion des utilisateurs")
subparsers = parser.add_subparsers(dest='command', help='Commandes utilisateur')
add_parser = subparsers.add_parser('add', help='Ajouter un nouvel utilisateur')
add_parser.add_argument('name', help='Nom de lutilisateur')
delete_parser = subparsers.add_parser('delete', help='Supprimer un utilisateur existant')
delete_parser.add_argument('id', help='ID de lutilisateur')

args = parser.parse_args()

print(args.command)
