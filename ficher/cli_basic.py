import argparse

parser = argparse.ArgumentParser(description="Traite les arguments.")
parser.add_argument("nom", type=str, help="C'est ton nom !")
parser.add_argument("--age", default=89, type=int, help="C'est ton age !")
parser.add_argument("--debug", action="store_true", help="Mode debug")
parser.add_argument("colors", choices=["red", "bleu"],  help="couleurs")
args = parser.parse_args()

print(args.age)
print(args.nom)
print(args.debug)
if args.debug:
    print("MODE DEBUG")
print(args.colors)