import csv

# Read input from CSV file (converted from Excel)
input_filename = "Student's Names.csv"
output_filename = 'students_processed.csv'

with open(input_filename, 'r', encoding='utf-8') as infile, \
        open(output_filename, 'w', newline='', encoding='utf-8') as outfile:

    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    # Write header for output file
    writer.writerow(['username', 'firstname', 'lastname', 'email', 'password'])
    
    # Skip header row
    next(reader)
    
    for row in reader:
        # Ensure row has enough columns
        if len(row) < 2:
            continue
            
        uid = row[0].strip()
        full_name = row[1].strip()
        
        # Split full name into parts
        name_parts = full_name.split()
        
        if name_parts:
            first_name = name_parts[0]  # First word
            last_name = name_parts[-1]  # Last word
        else:
            first_name = ''
            last_name = ''
        
        # Generate email and password
        email = f"{uid}@gmail.com"
        password = "Mm00000#"
        
        # Write processed data
        writer.writerow([uid, first_name, last_name, email, password])