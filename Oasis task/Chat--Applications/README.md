### Socket Chat Application
This Socket Chat Application is a simple client-server chat system built using Python's socket and threading libraries. It allows multiple clients to connect to a server and broadcast messages to all connected clients in real-time.

## Features
- Multi-Client Support: Multiple clients can connect to the server simultaneously.
- Real-Time Messaging: Messages are broadcasted to all connected clients in real-time.
- Threaded Server: The server handles multiple clients using threads, allowing for concurrent connections.
- Color-Coded Messages: Each client is assigned a random color for easy identification in the chat.


## Installation
### Prerequisites
- Python 3.x
- Required Python packages: colorama
You can install the required packages using pip:

```
pip install colorama
```

## Usage
### Running the Server
1. Navigate to the project directory.

2. Start the server:

```
python server.py
```
The server will start listening on 0.0.0.0:5002.

### Running the Client
1. Open a new terminal window.

2. Run the client:
```
python client.py
```
3. Enter your name when prompted.

4. Start sending messages! Type your message and press Enter to send it. Type 'q' to exit the chat.

## Example Workflow
- Start the server on your machine.
- Run multiple client instances from different terminals or different machines.
- Clients will connect to the server and start exchanging messages in real-time.


## Contributing
Contributions are welcome! Please fork this repository, make your changes, and submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
This project was inspired by the need for a simple, real-time communication system using Python's socket programming.