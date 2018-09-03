from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.util import custom
                                      
# Topology to be instantiated in Mininet
class MNTopo(Topo):
    "Mininet test topology"

    def __init__(self, cpu=.1, max_queue_size=None, **params):

        # Initialize topo
        Topo.__init__(self, **params)

        # Host and link configuration
        hostConfig = {'cpu': cpu}
        # change bw to 50mbits and delay to 10ms
        linkConfig = {'bw': 50, 'delay': '10ms', 'loss': 0,
                   'max_queue_size': max_queue_size }

        # Hosts and switches
        s1 = self.addSwitch('s1')
        
        # add more switches
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')

        sender = self.addHost('sender', **hostConfig)
        receiver = self.addHost('receiver', **hostConfig)

        # link to host and switch s1
        self.addLink(receiver, s1, port1=0, port2=1, **linkConfig)
        # link from s1 to s2
        self.addLink(s1, s2, port1=2, port2=1, **linkConfig)
        # link from s2 to s3
        self.addLink(s2, s3, port1=2, port2=1, **linkConfig)
        # link from s3 to sender
        self.addLink(sender, s3, port1=0, port2=2, **linkConfig)

if __name__ == '__main__':
  setLogLevel('debug')
