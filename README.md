# 📋 Moodle Users CSV Generator

This project provides a Python script to generate a Moodle-compatible CSV file containing user information from a simple CSV list of student names and IDs. It is designed to help educators quickly prepare user upload files for Moodle, especially when starting from a basic spreadsheet or exported list.

---

## ✨ Features

- Reads a CSV file with student IDs and full names.
- Splits full names into first and last names.
- Automatically generates email addresses and default passwords.
- Outputs a CSV file ready for Moodle user import.

---

## 🗂️ Input Format

The input CSV file (e.g., `Student's Names.csv`) should have at least two columns:

| ID      | Full Name         |
|---------|-------------------|
| 123456  | John Doe          |
| 234567  | Jane Smith        |
| ...     | ...               |

*The script skips the header row automatically.*

---

## 📝 Output Format

The output CSV file (`students_processed.csv`) will have the following columns:

| username | firstname | lastname | email             | password  |
|----------|-----------|----------|-------------------|-----------|
| 123456   | John      | Doe      | 123456@gmail.com  | Mm00000#  |
| 234567   | Jane      | Smith    | 234567@gmail.com  | Mm00000#  |
| ...      | ...       | ...      | ...               | ...       |

---

## 🚀 Usage

1. **Prepare your input CSV file**  
   - Ensure it is named `Student's Names.csv` and placed in the same directory as the script.
   - The first column should be the student ID, the second column the full name.

2. **Run the script**  
   - Open a terminal in the script directory.
   - Run:
     ```bash
     python "Moodle Users CSV Genertator.py"
     ```
   - The script will generate `students_processed.csv` in the same directory.

3. **Upload to Moodle**  
   - Use the generated CSV file for bulk user upload in your Moodle site.

---

## ⚠️ Notes

- The script uses a default password (`Mm00000#`) for all users. You may wish to change this for security.
- Email addresses are generated as `<student_id>@gmail.com`. Adjust this in the script if your institution uses a different domain.
- The script assumes the first and last words in the full name are the first and last names, respectively.

---

## 🛠️ Customization

- **Change password or email domain:**  
  Edit the lines in the script that set `password` and `email`.
- **Input/output file names:**  
  Change `input_filename` and `output_filename` variables at the top of the script.

---

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## 👤 Author

Majd Alsurihi

---

## 🤝 Contributing

Pull requests and suggestions are welcome!
