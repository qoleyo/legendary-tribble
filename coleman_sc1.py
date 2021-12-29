from mininet.topo import Topo
from mininet.link import TCLink

class MyTopo( Topo ):

	def __init__( self ):
		"Create custom topo."
		
		Topo.__init__( self )

		s9 = self.addSwitch( 's9' )
		s10 = self.addSwitch( 's10' )
		s11 = self.addSwitch( 's11' )
		s12 = self.addSwitch( 's12' )
		s13 = self.addSwitch( 's13' )
		s14 = self.addSwitch( 's14' )
		s15 = self.addSwitch( 's15' )

		h1 = self.addHost ( 'h1' , ip= "10.0.1.10/24" )
		h2 = self.addHost ( 'h2' , ip= "10.0.1.11/24" )
		h3 = self.addHost ( 'h3' , ip= "10.0.1.12/24" )
		h4 = self.addHost ( 'h4' , ip= "10.0.1.13/24" )
		h5 = self.addHost ( 'h5' , ip= "10.0.2.10/24" )
		h6 = self.addHost ( 'h6' , ip= "10.0.2.11/24" )
		h7 = self.addHost ( 'h7' , ip= "10.0.2.12/24" )
		h8 = self.addHost ( 'h8' , ip= "10.0.2.13/24" )
		h9 = self.addHost ( 'h9' , ip= "10.0.1.1/24" )
		h10 = self.addHost ( 'h10' , ip= "10.0.2.1/24" )

		self.addLink ( h9, s9,cls=TCLink, bw = 10 )
		self.addLink ( h10, s9,cls=TCLink, bw = 10 )
		self.addLink ( s9, s10,cls=TCLink, bw = 10 )
		self.addLink ( s9, s13,cls=TCLink, bw = 10 )
		self.addLink ( s10, s11,cls=TCLink, bw = 15, delay='10ms' )
		self.addLink ( s10, s12,cls=TCLink, bw = 15, delay='10ms' )
		self.addLink ( s11, h1,cls=TCLink, bw = 15, delay='10ms' )
		self.addLink ( s11, h2,cls=TCLink, bw = 15, delay ='10ms' )
		self.addLink ( s12, h3,cls=TCLink, bw = 15, delay= '10ms' )
		self.addLink ( s12, h4,cls=TCLink, bw = 15, delay ='10ms')
		self.addLink ( s13, s14,cls=TCLink )
		self.addLink ( s13, s15,cls=TCLink )
		self.addLink ( s14, h5,cls=TCLink )
		self.addLink ( s14, h6,cls=TCLink )
		self.addLink ( s15, h7,cls=TCLink )
		self.addLink ( s15, h8,cls=TCLink )

topos = { 'mytopo' : (lambda: MyTopo() ) }

