from tkinter.filedialog import askopenfilename, asksaveasfilename


def main():
    # Preguntar los nombres de los archivos de forma tradicional
    # infileName = input("Archivo de entrada: ")
    # outfileName = input("Archivo de salida: ")
    # Preguntar los nombres de los archivos usando tkinter
    infileName = askopenfilename()
    outfileName = asksaveasfilename()

    with open(infileName, "r") as infile, open(outfileName, "w") as outfile:
        for line in infile:
            name, last_name = line.split()
            uname = uname = (name + "." + last_name + "@colegiocoya.cl").lower()
            print(uname, file=outfile)

    print("Los nombre de usuarios se han escrito en el archivo", outfileName)


main()
