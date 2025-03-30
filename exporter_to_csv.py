filenames = [
    "chapter_1.rpy"
]

knownSpeakers = [
    "fox",
    "lastar",
    "\"\"",
    "\"???\"",
]

if __name__ == "__main__":
    with open("out.csv", "wt", encoding='utf-8') as output:
        for filename in filenames:
            with open(filename, "r", encoding='utf-8', errors='ignore') as f:
                for line in f.readlines():
                    line = line.strip()
                    splitLine = line.split(" ")
                    if splitLine[0] in knownSpeakers:
                        speaker, text = splitLine[0], " ".join(splitLine[1:]).strip("\"")
                    elif line.startswith("\""):
                        speaker, text = "option", line.split("\"")[1]
                    elif line.startswith("$ currentSituation = "):
                        speaker, text = "[currentSituation]", line.split("\"")[1]
                    else:
                        continue
                    if len(text) > 140:
                        print(f"{text}")
                    output.write(f"{speaker}|{text}|{len(text)}\n")