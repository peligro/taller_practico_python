import argparse

parser = argparse.ArgumentParser(description="Ejemplo ARG Parse")
parser.add_argument('-s', '--server', help="Servidor")
args = parser.parse_args()


if args.server:
    print(type(args.server))
    #print(f"el valor del server es {args.server}")
else:
    print("no se recibió el nombre del server, por favor vuelve a intentarlo")