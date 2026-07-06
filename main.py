import time
import os

# Starting grid coordinates for the rover
x, y = 0, 0

print("Rover engine started. Waiting for commands...")

while True:
    # Check if the file exists and has a command in it
    if os.path.exists("command.txt") and os.path.getsize("command.txt") > 0:
        with open("command.txt", "r") as file:
            command = file.read().strip()

        # Clear the file immediately so we don't read it twice
        open("command.txt", "w").close()

        # Move the rover on the grid
        if command == "W": y += 1
        elif command == "S": y -= 1
        elif command == "D": x += 1
        elif command == "A": x -= 1

        print(f"🚀 Rover executed [{command}]. Current Mars Position: X = {x}, Y = {y}")

    time.sleep(0.5) # Sleep for half a second to save CPU