#Programa para separar email  - Program Email Slicer

# Get user email address
email = input("What is your email address?: ").strip()

# Slice out the user name
user_name = email.split('@')[0] #Another way is with -> email[:email.index("@")] 

# Slice the domain name
domain_name = email.split('@')[1] #Another way is with -> email[email.index("@")+1:]

# Format message
# Check if it's a popular domain
popular_domains = ['gmail.com', 'hotmail.com', 'yahoo.com', 'outlook.com', 'aol.com']
if domain_name in popular_domains:
    message = f"Hey {user_name}, puede ver que tu correo esta registrado con el dominio {domain_name}. ¡Eso es genial!"
# If it's not a popular domain, assume it's a custom domain
else:
    message = f"Hey {user_name}, parece que tines un dominio personalizado igual a  {domain_name}. ¡Impresionante!"

# Display output message
print(message)