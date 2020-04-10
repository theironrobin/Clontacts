import sys
import subprocess


def main(args):
    vcard_list =[]
    with open(args[1], "r") as contacts_file:
        for line in contacts_file:
            vcard_list.append(line)

    big_list = []
    longstring = "" 
    for line in vcard_list:
        longstring += line
        if line.strip() == "END:VCARD":
            big_list.append(longstring[:-1])
            longstring = ""

    subprocess.call(['mkdir', 'output'])
    i=1
    for vcard in big_list:
        f = open("output/"+str(i)+".vcf", "w")
        subprocess.call(['echo', vcard], stdout=f)
        f.close()
        i += 1

    x = 1
    while x < i:
        subprocess.call(["cat", "output/" + str(x) + ".vcf"])
        x += 1 


if __name__ == "__main__":
    sys.exit(main(sys.argv))
