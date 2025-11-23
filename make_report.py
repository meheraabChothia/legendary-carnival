import json

sem = input("What sem do you want a report for: ")
file = f"sem{sem}.json"

with open(file, 'r') as fp:
    data = json.load(fp)

markdown = f"# Semester {sem} Results:\n\n"
markdown += "| Subject | Marks | Credits |\n"
markdown += "|---------|-------|---------|\n"

total_creds = 0
total_weightage = 0

for subject, values in data.items():
    marks = values.get('marks', '')
    credits = values.get('credits', '')
    markdown += f"| {subject} | {marks} | {credits} |\n"
    total_creds += credits
    total_weightage += (credits*marks)
sgpa = total_weightage/total_creds
markdown += f"\nSGPA: {sgpa}\n"

markdown_file = f"sem{sem}.md"
with open(markdown_file, 'w') as fp:
    fp.write(markdown)
    print(f"System: Report printed in markdown format in file {
          markdown_file} ")

print(markdown)
