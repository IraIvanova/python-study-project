students = {
    "Іван Петров": {
        "Пошта": "Ivan@gmail.com",
        "Вік": 14,
        "Номер телефону": "+380987771221",
        "Середній бал": 95.8,
    },
    "Женя Курич": {
        "Пошта": "Geka@gmail.com",
        "Вік": 16,
        "Номер телефону": None,
        "Середній бал": 64.5,
    },
    "Маша Кера": {
        "Пошта": "Masha@gmail.com",
        "Вік": 18,
        "Номер телефону": "+380986671221",
        "Середній бал": 80,
    },
}

new_student_name = "Іван Франко"
new_student_info = {
    "Пошта": "i.franko@gmail.com",
    "Вік": 28,
    "Номер телефону": "+380635471203",
    "Середній бал": 59.2,
}

students[new_student_name] = new_student_info

total_score = 0

for student, student_info in students.items():
    total_score += student_info["Середній бал"]

average_score = total_score / len(students)

students["Іван Петров"]["bank_account_number"] = None

second_student_salary = students["Женя Курич"].get("salary") or 0.0
