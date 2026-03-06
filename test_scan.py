import pickle
import subprocess
import os

# Command injection vulnerability
def ping_host(user_input):
    os.system("ping " + user_input)  # Vulnerable

# Insecure deserialization
def load_data(file_path):
    with open(file_path, 'rb') as f:
        return pickle.load(f)  # Vulnerable

# Hardcoded credential
API_KEY = "sk_live_123456789"  # Vulnerable

# SQL injection vulnerability
def get_user(username):
    query = "SELECT * FROM users WHERE username = '" + username + "'"  # Vulnerable
    return query

# Eval usage
def calculate(expression):
    return eval(expression)  # Vulnerable
