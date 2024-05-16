import matplotlib.pyplot as plt

with open("text.txt", "r") as my_file:
    lines = my_file.readlines()[1:] 

subjects = []
grades = []

for line in lines:
    subject, grade = line.strip().split(',')
    subjects.append(subject)
    grades.append(int(grade))

plt.plot(subjects, grades, marker='o', linestyle='-')
plt.xlabel('Предмет')
plt.ylabel('Оцінка')
plt.title('Графік оцінок')
plt.xticks(rotation=45) 
plt.grid(True) 
plt.tight_layout() 
plt.show()
