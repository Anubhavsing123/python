# Exercise 8: Generate Random Token and URL
import secrets
print(secrets.token_hex(16))
print(secrets.token_urlsafe(64))