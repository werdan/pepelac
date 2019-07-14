import socket
import os
import atexit
import signal


HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)


class Server:

    child_pid = 0

    def start(self, config):
        self.child_pid = os.fork()
        if self.child_pid == 0:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                print("Starting Pepelac http server process on port {}".format(str(PORT)))
                s.bind((HOST, PORT))
                s.listen()
                while True:
                    conn, addr = s.accept()
                    data = conn.recv(1024)
                    print ("Incoming connection")
                    response = b'HTTP/1.1 200 OK\n\nDATA'
                    conn.sendall(response)
                    conn.close()
        else:
            print("Spawning 1 child process with PID {}".format(self.child_pid))

    def stop(self):
        os.kill(self.child_pid, signal.SIGKILL)


def close_child_processes():
    # Use Singleton
    # os.kill(child_pid, signal.SIGKILL)
    print("Closing server incorrectly. Child processes might be still running.")


atexit.register(close_child_processes)
