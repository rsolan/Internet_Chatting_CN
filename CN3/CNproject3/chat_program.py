import threading
import socket
import os

# Function for writing thread
def writing_thread(name):
    port = int(input("Enter port number to connect: "))
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect(('localhost', port))
    
    while True:
        message = input(f"")
        if message == "":  # Skip sending empty messages
            continue
        
        full_message = f"{name}: {message}"
        server.send(full_message.encode())
        
        if message == "transfer filename":
            filename = input("Enter filename to transfer: ")
            
            if os.path.exists(filename):
                server.send("transfer filename".encode())
                server.send(filename.encode())
                
                with open(filename, "rb") as f:
                    while True:
                        file_data = f.read(1024)
                        if not file_data:
                            break
                        server.send(file_data)
                        
                print("File transferred successfully.")
            else:
                print("File does not exist.")

# Function for reading thread
def reading_thread(name):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 0))
    port = server.getsockname()[1]
    print("Server started on port", port)
    server.listen(1)
    conn, addr = server.accept()
    
    receiving_file = False
    received_filename = ""
    
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            
            if receiving_file:
                with open(f"new_{received_filename}", "ab") as f:
                    f.write(data)
                    
                if len(data) < 1024:
                    print(f"File received and saved as 'new_{received_filename}'.")
                    receiving_file = False
                    received_filename = ""
            else:
                message = data.decode()
                if message == "transfer filename":
                    received_filename = conn.recv(1024).decode()
                    receiving_file = True
                else:
                    print(message)
        except ConnectionResetError:
            print("Connection closed by the remote host.")
            break


# Main function
def main():
    name = input("Enter your name (e.g., Alice or Bob): ")

    # Create reading thread
    reading = threading.Thread(target=reading_thread, args=(name,))
    reading.start()

    # Wait for reading thread to start
    input("Press Enter to continue...")

    # Create writing thread
    writing_thread(name)

if __name__ == "__main__":
    main()
