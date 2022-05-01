with open("text-notes/zettel.txt", encoding='utf-8') as f:
    content = f.readlines()

new_content = [line.replace("\n\n", "\n") for line in content]

with open("zettel-notes/zettel_50.md", "w+", encoding='utf-8') as f:
    counter = 1
    for line_num, line in enumerate(new_content, start=1):
        if line_num % 50 == 0 or line_num == 1:
            f.write(f"# {counter}\n")
            counter += 1
        f.write(line)

    




