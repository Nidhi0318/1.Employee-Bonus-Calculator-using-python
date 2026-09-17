# Employee Bonus Calculator

## 📌 Project Description

The **Employee Bonus Calculator** is a simple Python program that calculates an employee's bonus based on their salary and performance rating.

The program takes the employee's name, salary, and rating as input and calculates the bonus according to predefined rating percentages. Employees earning less than ₹30,000 also receive an additional ₹2,000 bonus.

## 🎯 Objective

The main objective of this project is to practice:

* Python input and output
* Conditional statements (`if`, `elif`, `else`)
* Arithmetic calculations
* User input validation
* Basic program flow

## ⚙️ How It Works

The program calculates the bonus based on the employee rating:

| Rating | Bonus         |
| ------ | ------------- |
| 5      | 20% of salary |
| 4      | 15% of salary |
| 3      | 10% of salary |
| 2      | 5% of salary  |
| 1      | No bonus      |

### Additional Bonus

If the employee's salary is **below ₹30,000**, an additional **₹2,000** is added to the calculated bonus.

The final salary is calculated as:

```text
Final Salary = Original Salary + Bonus
```

## 🛠️ Technologies Used

* **Python 3**
* Conditional Statements
* User Input
* Arithmetic Operations

## ▶️ How to Run

1. Make sure Python is installed on your system.

2. Open the project folder in VS Code or Command Prompt.

3. Run the Python file:

```bash
python "1.Employee Bonus Calculator.py"
```

4. Enter the required details when prompted:

```text
Enter employee name: Rahul
Enter employee salary: ₹25000
Enter employee rating (1-5): 5
```

5. The program displays the employee's bonus details:

```text
--- Employee Bonus Details ---
Employee Name: Rahul
Original Salary: ₹ 25000
Bonus: ₹ 7000
Final Salary: ₹ 32000
```

## 📂 Project Structure

```text
Employee-Bonus-Calculator/
│
├── 1.Employee Bonus Calculator.py
└── README.md
```

## ✨ Features

* Accepts employee details from the user
* Calculates bonus based on performance rating
* Provides an additional bonus for employees earning below ₹30,000
* Validates employee ratings from 1 to 5
* Displays original salary, bonus, and final salary

## 📚 Learning Outcome

Through this project, I learned how to use Python conditional statements and mathematical operations to build a simple real-world salary calculation application.

## 👩‍💻 Author

**Nidhi M**

## 📄 License

This project is created for **educational and learning purposes**.
