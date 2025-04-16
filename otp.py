import tkinter as tk
from tkinter import messagebox
from twilio.rest import Client
import random

# --- Twilio Credentials (Replace with your own) ---
account_sid = 'your_account_sid_here'
auth_token = 'your_auth_token_here'
twilio_number = '+1234567890'      # Your Twilio phone number
receiver_number = '+91xxxxxxxxxx'  # Your verified phone number

# --- Generate Initial OTP ---
generated_otp = random.randint(1000, 9999)

# --- Send OTP Function ---
def sendOTP():
    global generated_otp
    generated_otp = random.randint(1000, 9999)
    try:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=f"Your OTP is: {generated_otp}",
            from_=twilio_number,
            to=receiver_number
        )
        print("OTP Sent:", generated_otp)
        messagebox.showinfo("OTP Sent", f"OTP has been sent to {receiver_number}")
    except Exception as e:
        print("Error:", e)
        messagebox.showerror("Error", "Failed to send OTP")

# --- Verify OTP Function ---
def verifyOTP():
    try:
        user_input = int(otp_entry.get())
        if user_input == generated_otp:
            messagebox.showinfo("Success", "OTP Verified. Login Successful!")
        else:
            messagebox.showerror("Invalid", "Incorrect OTP. Try again.")
    except:
        messagebox.showerror("Error", "Please enter a valid 4-digit OTP")

# --- GUI Setup ---
root = tk.Tk()
root.title("OTP Verification - EduGenie")
root.geometry("400x400")
root.config(bg="white")

title = tk.Label(root, text="EduGenie OTP Verification", font=("Arial", 16, "bold"), bg="white")
title.pack(pady=20)

otp_entry = tk.Entry(root, width=25, font=("Arial", 14), show="*")  # Masked input
otp_entry.pack(pady=10)

send_button = tk.Button(root, text="Send OTP", command=sendOTP, font=("Arial", 12, "bold"), bg="#00bfff", fg="white")
send_button.pack(pady=10)

verify_button = tk.Button(root, text="Verify OTP", command=verifyOTP, font=("Arial", 12, "bold"), bg="green", fg="white")
verify_button.pack(pady=10)

# Automatically send OTP once GUI launches
sendOTP()

root.mainloop()
