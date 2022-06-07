with open("text-notes/zettel.txt", encoding='utf-8') as f:
    content = f.readlines()

new_content = [line for line in content if line.strip() != '']

total_num_lines = len(new_content)
num_lines_per_heading = 50
number_headings = total_num_lines // num_lines_per_heading

with open("zettel-notes/zettel_50.md", "w+", encoding='utf-8') as f:
    counter = number_headings
    for line_num, line in enumerate(new_content, start=1):
        if line_num % num_lines_per_heading == 0:
            f.write(f"# {counter}\n")
            counter -= 1
        f.write(f"{line}")

    




