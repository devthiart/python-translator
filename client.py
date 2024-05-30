import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # put your computers's IP address here:
    client.connect(('YOUR_IP_HERE', 12345))

    connected = True

    while connected:
        print("\n***** TRANSLATOR ENGLISH TO PORTUGUESE *****")
        operation = input("Type a sentence in English (ex.: 'how are you?') or 'exit' to close: ")

        if operation == "exit":
            connected = False
            break
        
        client.send(operation.encode('utf-8'))

        result = client.recv(4096).decode('utf-8')
        print(f"Translation: {result}")

    client.close()

if __name__ == "__main__":
    main()
