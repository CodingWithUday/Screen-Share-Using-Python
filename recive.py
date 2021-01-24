from vidstream import StreamingServer #pip install vidstream
import threading

reviver = StreamingServer("192.168.1.105", 7831)

t = threading.Thread(target=reviver.start_server)
t.start()