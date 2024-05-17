1. Introduction
This project involves the development of an Internet chatting application using Python. The application
utilizes socket programming to enable communication between two users, Alice and Bob, and
incorporates multi-threading for concurrent reading and writing operations. Additionally, the application
supports file transfer functionality between the users.

1.1 Project Components
chat_program.py:
● Writing Thread (Client Side):
● Initiates a new thread upon program launch.
● Accepts a port number from the user for establishing a connection.
● Reads user messages from the keyboard and sends them over the established
socket connection.
● Implements file transfer capability allowing users to send files by typing "transfer
filename".
● Reading Thread (Server Side):
● Creates a ServerSocket, listens for incoming connections, and prints received
messages.
● Manages file transfer requests by receiving and storing files locally.

1.2 Demo Sequence
● Execute chat_program.py for Alice to obtain port number X.
● Execute chat_program.py for Bob to obtain port number Y (distinct from X).
● Alice connects to Bob by entering Y in her console.
● Bob connects to Alice by entering X in his console.
● Messages sent by Alice should be displayed on Bob's console.
● Messages sent by Bob should be displayed on Alice's console.
● File transfer functionality tested by sending a file from Alice to Bob.

2. Programming Environment
● Programming Language: Python
● Operating System: Cross-platform (Windows, macOS, Linux)
● Tools: Any text editor or IDE that supports Python (Visual Studio Code)

3.Testing
The application was tested to ensure robustness and reliability in handling various scenarios:
● Message Communication: Verified that messages sent from one user are correctly received by the
other.
● File Transfer: Confirmed the successful transfer of files between the users.
● Error Handling: Ensured appropriate error messages are displayed for invalid inputs and
file-related issues.

Conclusion
The developed chat application offers a basic yet functional platform for real-time communication
between two users over the Internet. It leverages Python's socket programming capabilities and
multithreading features to provide seamless messaging and file transfer services
