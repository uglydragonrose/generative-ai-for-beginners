from dotenv import load_dotenv
import os

# Φόρτωση μεταβλητών περιβάλλοντος από το αρχείο .env
load_dotenv()

# Πρόσβαση στην μεταβλητή GITHUB_TOKEN
github_token = os.getenv("GITHUB_TOKEN")

print(github_token)
