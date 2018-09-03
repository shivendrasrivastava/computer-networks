from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.util import custom

# Topology to be instantiated in Mininet
class ComplexTopo(Topo):
    "Mininet Complex Topology"

    def __init__(self, cpu=.1, max_queue_size=None, **params):

        # Initialize topo
        Topo.__init__(self, **params)

        #TODO: Create your Mininet Topology here!

        # host config
        hostConfig = {'cpu': cpu}
        # link config
        ethernetLinkConfig = {'bw': 25, 'delay': '2ms', 'loss': 0, 'max_queue_size': max_queue_size}
        wifiLinkConfig = {'bw': 10, 'delay': '6ms', 'loss': 3, 'max_queue_size': max_queue_size}
        threeGLinkConfig = {'bw': 3, 'delay': '10ms', 'loss': 8, 'max_queue_size': max_queue_size}

        # create hosts
        h1 = self.addHost('h1', **hostConfig)
        h2 = self.addHost('h2', **hostConfig)
        h3 = self.addHost('h3', **hostConfig)

        # create switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')

        # link b/w h1 and s1
        self.addLink(h1, s1, **ethernetLinkConfig)

        # link b/w s1 and s2
        self.addLink(s1, s2, **ethernetLinkConfig)

        # link b/w s2 and s3
        self.addLink(s2, s3, **ethernetLinkConfig)

        # link b/w s3 and h2
        self.addLink(s3, h2, **wifiLinkConfig)

        # link b/w s2 and s4
        self.addLink(s2, s4, **ethernetLinkConfig)

        # link b/w s4 and h3
        self.addLink(s4, h3, **threeGLinkConfig)


