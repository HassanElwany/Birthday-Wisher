# Generate_modified_message Func
This function takes a name and a template path as input,
reads a template file, replaces a placeholder with the provided name, 
and returns the modified message.

# Send_birthday_email Func
This function sends a birthday email using the SMTP protocol with Gmail. It requires sender and recipient information, subject, and body.

# main Function
The main function is the main entry point of the program. It reads birthday data from a CSV file,
checks if it's someone's birthday today, 
generates a modified message, and sends a birthday email if conditions are met.
