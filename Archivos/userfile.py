def main():
    print("This program creates a file of usernames from a file of names. ")

    # get the file names
    infileName = input("What file are the names in? ")
    outfileName = input("What file should the username go in? ")

    # open the files
    infile = open(infileName, "r")
    outfile = open(outfileName, "w")

    # process each line of the input file
    for line in infile:
        # get the first and the las names from line
        first, last = line.split()
        #create the username
        uname = (first+"."+last+"@colegiocoya.cl").lower()
        # write it to the output file
        print(uname, file=outfile)

    # close both files
    infile.close()
    outfile.close()

    print("Usernames have been written to", outfileName)
main()


