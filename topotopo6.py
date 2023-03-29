from mininet.link import TCLink
from mininet.net import Mininet
from mininet.topo import Topo


class MyTopom(Topo):
    def __init__(self):
        Topo.__init__(self)
        h1 = self.addHost("warszawa",ip='10.1/8')
        h2 = self.addHost("bialystok",ip='10.2/8')
        h3 = self.addHost("gdansk",ip='10.3/8')
        h4 = self.addHost("szczecin",ip='10.4/8')
        h5 = self.addHost("poznan",ip='10.5/8')
        h6 = self.addHost("bydgoszcz",ip='10.6/8')
        h7 = self.addHost("lodz",ip='10.7/8')
        h8 = self.addHost("krakow",ip='10.8/8')
        h9 = self.addHost("wroclaw",ip='10.9/8')
        h10 = self.addHost("rzeszow",ip='10.10/8')

        s1 = self.addSwitch("s1")
        s2 = self.addSwitch("s2")
        s3 = self.addSwitch("s3")
        s4 = self.addSwitch("s4")
        s5 = self.addSwitch("s5")
        s6 = self.addSwitch("s6")
        s7 = self.addSwitch("s7")
        s8 = self.addSwitch("s8")
        s9 = self.addSwitch("s9")
        s10 = self.addSwitch("s10")

        self.addLink(h1, s1)
        self.addLink(h2, s2)
        self.addLink(h3, s3)
        self.addLink(h4, s4)
        self.addLink(h5, s5)
        self.addLink(h6, s6)
        self.addLink(h7, s7)
        self.addLink(h8, s8)
        self.addLink(h9, s9)
        self.addLink(h10, s10)

        links0s1 = self.addLink(s1, s2, bw=9.5, loss=0.35, delay="1.41ms", max_queue_size=950)  # Warszawa-Bialystok
        links0s2 = self.addLink(s1, s3, bw=9.8, loss=0.55, delay="2.40ms", max_queue_size=980)  # Warszawa-Gdansk
        links0s9 = self.addLink(s3, s4, bw=10, loss=0.6, delay="2.55ms", max_queue_size=1000)  # Gdansk-Szczecin

        links1s6 = self.addLink(s1, s5, bw=9.8, loss=0.5, delay="2.20ms", max_queue_size=980)  # Warszawa-Poznan
        links1s7 = self.addLink(s5, s6, bw=8.5, loss=0.1, delay="0.98ms", max_queue_size=920)  # Poznan-Bydgoszcz
        links1s4 = self.addLink(s1, s7, bw=10, loss=0.1, delay="0.96ms", max_queue_size=1000)  # Warszawa-Lodz

        links4s6 = self.addLink(s1, s8, bw=10, loss=0.45, delay="2.05ms", max_queue_size=1000)  # Warszawa-Krakow
        links4s7 = self.addLink(s8, s9, bw=9.7, loss=0.4, delay="1.91ms", max_queue_size=970)  # Krakow-Wroclaw
        links4s5 = self.addLink(s8, s10, bw=8, loss=0.2, delay="1.18ms", max_queue_size=870)  # Krakow-Rzeszow

        self.addLink(s1, s10, bw=7.5, loss=0.55, delay="2.33ms", max_queue_size=800)  # Warszawa-Rzeszow 330km
        self.addLink(s1, s6, bw=8.6, loss=0.5, delay="2.13ms", max_queue_size=900)  # Warszawa-Bydgoszcz 302km
        self.addLink(s7, s8, bw=10, loss=0.45, delay="1.97ms", max_queue_size=1000)  # Lodz-Krakow 280 km
        self.addLink(s7, s9, bw=10, loss=0.37, delay="1.56ms", max_queue_size=1000)  # Lodz-Wroclaw 221km
        self.addLink(s7, s5, bw=10, loss=0.35, delay="1.50ms", max_queue_size=1000)  # Lodz-Poznan 212km
        self.addLink(s5, s9, bw=9.8, loss=0.3, delay="1.29ms", max_queue_size=980)  # Poznan-Wroclaw 183km
        self.addLink(s5, s4, bw=9.5, loss=0.4, delay="1.88ms", max_queue_size=950)  # Poznan-Szczecin 266km
        self.addLink(s4, s9, bw=9.7, loss=0.8, delay="2.94ms", max_queue_size=970)  # Szczecin-Wroclaw 416km
        self.addLink(s4, s6, bw=9, loss=0.4, delay="1.83ms", max_queue_size=940)  # Szczecin-Bydgoszcz 259km
        self.addLink(s2, s10, bw=7, loss=1.3, delay="3.41ms", max_queue_size=770)  # Bialystok-Rzeszow 482km
        self.addLink(s3, s2, bw=8, loss=0.75, delay="2.76ms", max_queue_size=870)  # Gdansk-Bialystok 391km
        self.addLink(s3, s6, bw=8.5, loss=0.2, delay="1.18ms", max_queue_size=920)  # Gdansk-Bydgoszcz 167km


topos = {'MyTopo': lambda: MyTopom()}
