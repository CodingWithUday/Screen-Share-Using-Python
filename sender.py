from vidstream import ScreenShareClient
import threading

sender = ScreenShareClient("192.168.1.105", 7831)

t = threading.Thread(target=sender.start_stream)
t.start()