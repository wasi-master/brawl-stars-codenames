BRAWLERS = 58

with open("codenames.md", "w") as output:
    output.write("# Table of all characters and their codenames\n")
    output.write("| Codename | Character |\n")
    output.write("|----------|-----------|\n")
    with open("./characters.csv") as f:
        for character in f.readlines()[2:BRAWLERS-1]:
            codename, _, _, character = character.split(",")[:4]
            output.write(f"| {codename} | {character} |\n")