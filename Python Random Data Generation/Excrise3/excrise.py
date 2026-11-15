# Exercise 3: Generate 6 digit Random Secure OTP
import secrets
s=secrets.SystemRandom()
otp=s.randrange(100000, 999999)
print(otp)