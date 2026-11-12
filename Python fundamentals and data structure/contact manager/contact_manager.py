import tkinter as tk
from tkinter import messagebox
import os
import json

file_name = "contacts.json"
# contacts = []


# load existing contacts if the file exist
def load_contacts():
    if os.path.exists(file_name):
        try:
            with open(file_name, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    return []


# Save the list of dictionaries to a JSON file
def save_to_file(contacts):
    with open(file_name, "w") as file:
        json.dump(contacts, file, indent=4)


def save_contact():
    name = name_entry.get().strip()
    age = age_entry.get().strip()
    phone = phone_entry.get().strip()

    if not name or not age or not phone:
        messagebox.showwarning("missing information, name required")
        return
    contacts = load_contacts()
    contacts.append({"name": name, "age": age, "phone": phone})
    save_to_file(contacts)

    # Clear the input boxes after saving
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    messagebox.showinfo("Saved", f"{name} has been saved!")


# --- Build the Visual Window ---
root = tk.Tk()
root.title("My Contact Manager")
root.geometry("300x250")

# Name Slot
tk.Label(root, text="Name:").pack(pady=(15, 0))
name_entry = tk.Entry(root, width=30)
name_entry.pack()

# Age Slot
tk.Label(root, text="Age:").pack(pady=(10, 0))
age_entry = tk.Entry(root, width=30)
age_entry.pack()

# Phone Slot
tk.Label(root, text="Phone:").pack(pady=(10, 0))
phone_entry = tk.Entry(root, width=30)
phone_entry.pack()

# Save Button
save_btn = tk.Button(
    root, text="Save Contact", command=save_contact, bg="#4CAF50", fg="white"
)
save_btn.pack(pady=20)

# Keep the window open
root.mainloop()


# #console only app
# # add contacts if they dont exist yet
# def add_contact(name, age, phone):
#     contact = {"name": name, "age": age, "phone": phone}
#     contacts.append(contact)
#     print(f" the new {contact} has been added to a list of contacts")

# # view contacts
# def view_contacts():
#     if not contacts:
#         print("your contact list is empty")
#         return
#     print("\n--- your contacts")
#     for contact in contacts:
#         print(
#             f"name : {contact:['name']} | age :{contact:['age']} | phone: {contact:['phone']}"
#         )

# # Button click action
# def save_with_button_click()
# add_contact("angie", 30, 12345)
# # save_to_file(contact)
