#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

def myNetwork():

	net = Mininet( topo=None,build=False,ipBase='10.0.0.0/8')

	info( '+Add controller+\n' )
	c0=net.addController(name='c0',controller=Controller,protocol='tcp',port=6633)

	info( '+Add switches+\n')
	s9 = net.addSwitch('s9', cls=OVSKernelSwitch)
	s3 = net.addSwitch('s3', cls=OVSKernelSwitch)
	s4 = net.addSwitch('s4', cls=OVSKernelSwitch)
	s10 = net.addSwitch('s10', cls=OVSKernelSwitch)
	s1 = net.addSwitch('s1', cls=OVSKernelSwitch)
	s7 = net.addSwitch('s7', cls=OVSKernelSwitch)
	s5 = net.addSwitch('s5', cls=OVSKernelSwitch)
	s6 = net.addSwitch('s6', cls=OVSKernelSwitch)
	s8 = net.addSwitch('s8', cls=OVSKernelSwitch)
	s2 = net.addSwitch('s2', cls=OVSKernelSwitch)

	info( '+Add hosts+\n')
	h7 = net.addHost('h7', cls=Host, ip='10.0.0.7', defaultRoute=None)
	h15 = net.addHost('h15', cls=Host, ip='10.0.0.15', defaultRoute=None)
	h3 = net.addHost('h3', cls=Host, ip='10.0.0.3', defaultRoute=None)
	h11 = net.addHost('h11', cls=Host, ip='10.0.0.11', defaultRoute=None)
	h9 = net.addHost('h9', cls=Host, ip='10.0.0.9', defaultRoute=None)
	h16 = net.addHost('h16', cls=Host, ip='10.0.0.16', defaultRoute=None)
	h13 = net.addHost('h13', cls=Host, ip='10.0.0.13', defaultRoute=None)
	h10 = net.addHost('h10', cls=Host, ip='10.0.0.10', defaultRoute=None)
	h14 = net.addHost('h14', cls=Host, ip='10.0.0.14', defaultRoute=None)
	h8 = net.addHost('h8', cls=Host, ip='10.0.0.8', defaultRoute=None)
	h2 = net.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute=None)
	h6 = net.addHost('h6', cls=Host, ip='10.0.0.6', defaultRoute=None)
	h4 = net.addHost('h4', cls=Host, ip='10.0.0.4', defaultRoute=None)
	h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)
	h5 = net.addHost('h5', cls=Host, ip='10.0.0.5', defaultRoute=None)
	h12 = net.addHost('h12', cls=Host, ip='10.0.0.12', defaultRoute=None)

	info( '+Add links+\n')
	net.addLink(s1, h3)
	net.addLink(h1, s1)
	net.addLink(h2, s1)
	net.addLink(s1, s2)
	net.addLink(s2, h4)
	net.addLink(s2, s3)
	net.addLink(s3, s4)
	net.addLink(s3, s5)
	net.addLink(s3, s6)
	net.addLink(s5, h5)
	net.addLink(s4, h7)
	net.addLink(s4, h6)
	net.addLink(s3, s7)
	net.addLink(s7, h8)
	net.addLink(s6, h10)
	net.addLink(s6, h9)
	net.addLink(s5, s8)
	net.addLink(s8, h11)
	net.addLink(s8, h12)
	net.addLink(s6, s9)
	net.addLink(s9, h13)
	net.addLink(s9, h14)
	net.addLink(s4, s10)
	net.addLink(s10, h15)
	net.addLink(s10, h16)

    
	info( '+Starting network+\n')
	net.addNAT().configDefault()
	net.build()
	
	info( '+Starting controllers+\n')
	for controller in net.controllers:controller.start()

	info( '+Starting switches+\n')
	net.get('s9').start([c0])
	net.get('s3').start([c0])
	net.get('s4').start([c0])
	net.get('s10').start([c0])
	net.get('s1').start([c0])
	net.get('s7').start([c0])
	net.get('s5').start([c0])
	net.get('s6').start([c0])
	net.get('s8').start([c0])
	net.get('s2').start([c0])

	info( '+Post configure switches and hosts+\n')
	print('+Starting WebServer+\n')
	h1.cmdPrint('python -m SimpleHTTPServer 80 &')
	h1.cmd('sleep 5')
	h2.cmdPrint('wget -O - 10.0.0.1')
	print('**h2 CONNECTED**')
	h1.cmd('sleep 5')
	h3.cmdPrint('wget -O - 10.0.0.1')
	print('**h3 CONNECTED**')
	h1.cmd('sleep 5')
	h4.cmdPrint('wget -O - 10.0.0.1')
	print('**h4 CONNECTED**')
	h1.cmd('sleep 5')
	h5.cmdPrint('wget -O - 10.0.0.1')
	print('**h5 CONNECTED**')
	h1.cmd('sleep 5')
	h6.cmdPrint('wget -O - 10.0.0.1')
	print('**h6 CONNECTED**')
	CLI(net)
	net.stop()
	
	
if __name__ == '__main__':
	setLogLevel( 'info' )
	myNetwork()
