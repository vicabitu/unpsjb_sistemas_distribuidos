import Pyro4
from datetime import datetime


@Pyro4.expose
class TimeServer(object):
    def get_time(self):
        time = datetime.now()
        string_time = time.strftime("%Y-%m-%d %H:%M:%S:%f")
        return string_time


daemon = Pyro4.Daemon()  # make a Pyro daemon
ns = Pyro4.locateNS()  # find the name server
uri = daemon.register(TimeServer)  # register the greeting maker as a Pyro object
ns.register("my.home", uri)  # register the object with a name in the name server

print("Ready.")
daemon.requestLoop()  # start the event loop of the server to wait for calls
