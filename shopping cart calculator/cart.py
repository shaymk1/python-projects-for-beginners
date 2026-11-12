import os
import json

# import tkinter as tk
# from tkinter import messagebox

FILE_NAME = "items.json"


# load data
def load_data():
    if os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []


# save data
def save_items_to_file(items):
    with open(FILE_NAME, "w") as file:
        json.dump(items, file, indent=4)


# create items
def create_items(name, price):
    items = load_data()
    item_id = []
    for item in items:
        item_id.append(items["id"])

    if item_id:
        new_id = max(item_id) + 1
    else:
        new_id = 1
    items = {"id": new_id, "name": name, "price": price}
    items.append(item)
    save_items_to_file(items)


# read all items
def get_all_items():
    items = load_data()
    if not items:
        print("your item list is empty, please create items")
        return
    return items


# read one item
# def get_one_item():
#     items = load_data()
#     for item in items:
#         if item["id"] == item_id:
#             return item


# # saving items with tkinter
# def save_items():
#     name = name_entry.get().strip()
#     price = price_entry.get().strip()
#     new_id =
#     id_entry.get().strip()
#     if not name or not price:
#         messagebox.showwarning("missing information")
#         return
#     items = load_data()
#     items.append({"id": new_id, "name": name, "price": price})
#     save_items_to_file(items)
# Clear the input boxes after saving
#     name_entry.delete(0, tk.END)
#     age_entry.delete(0, tk.END)
#     phone_entry.delete(0, tk.END)
#     messagebox.showinfo("Saved", f"{name} has been saved!")


# # --- Build the Visual Window ---
# root = tk.Tk()
# root.title("My Contact Manager")
# root.geometry("300x250")

# # Name Slot
# tk.Label(root, text="Name:").pack(pady=(15, 0))
# name_entry = tk.Entry(root, width=30)
# name_entry.pack()

# # Age Slot
# tk.Label(root, text="Age:").pack(pady=(10, 0))
# age_entry = tk.Entry(root, width=30)
# age_entry.pack()

# # Phone Slot
# tk.Label(root, text="Phone:").pack(pady=(10, 0))
# phone_entry = tk.Entry(root, width=30)
# phone_entry.pack()

# # Save Button
# save_btn = tk.Button(
#     root, text="Save Contact", command=save_contact, bg="#4CAF50", fg="white"
# )
# save_btn.pack(pady=20)

# # Keep the window open
# root.mainloop()
