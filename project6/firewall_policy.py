#!/usr/bin/python
# CS 6250 Fall 2018 - Project 6 - SDN Firewall

from pyretic.lib.corelib import *
from pyretic.lib.std import *
from pyretic.lib.query import packets
from pyretic.core import packet

def get_firewall_rule(entry):
	rule = match(ethtype=packet.IPV4)

	# data type EthAddr
	mcaddr_dst = entry['macaddr_dst']
	if (mcaddr_dst != '-'):
		rule = rule & match(dstmac=EthAddr(mcaddr_dst))
	
	# data type EthAddr
	mcaddr_src = entry['macaddr_src']
	if (mcaddr_src != '-'):
		rule = rule & match(srcmac=EthAddr(mcaddr_src))

	protocol = entry['protocol']
	if (protocol != '-'):
		protocolNamePyretic = None
		protocolNamePyretic2 = None
		if (protocol == 'T'):
			protocolNamePyretic = packet.TCP_PROTO
		if (protocol == 'U'):
			protocolNamePyretic = packet.UDP_PROTO
		if (protocol == 'I'):
			protocolNamePyretic = packet.ICMP_PROTO
		if (protocol == 'B'):
			protocolNamePyretic = packet.TCP_PROTO
			protocolNamePyretic2 = packet.UDP_PROTO
	if (protocolNamePyretic2 is None):
		rule = rule & match(protocol=protocolNamePyretic)
	else:
		rule = rule & (match(protocol=protocolNamePyretic) | match(protocol=protocolNamePyretic2))
	
	# data type int
	port_src = entry['port_src']
	if (port_src != '-'):
		rule = rule & match(srcport=int(port_src))
	
	# data type int
	port_dst = entry['port_dst']
	if (port_dst != '-'):
		rule = rule & match(dstport=int(port_dst))
	
	# data type IPAddr
	ipaddr_src = entry['ipaddr_src']
	if (ipaddr_src != '-'):
		rule = rule & match(srcip=IPAddr(ipaddr_src))
	
	# data type IPAddr
	ipaddr_dst = entry['ipaddr_dst']
	if (ipaddr_dst != '-'):
		rule = rule & match(dstip=IPAddr(ipaddr_dst))
	
	return rule

def make_firewall_policy(config):

	# You may place any user-defined functions in this space.
	# You are not required to use this space - it is available if needed.

	# feel free to remove the following "print config" line once you no longer need it
	print config # for demonstration purposes only, so you can see the format of the config

	# sample config
	# [{'macaddr_dst': '-', 'protocol': 'T', 'rulenum': '1', 'port_src': '-', 'ipaddr_dst': '-', 'macaddr_src': '-', 'port_dst': '1080', 'ipaddr_src': '-'}]
	print "hello"

	rules = []

	for entry in config:

		# TODO - This is where you build your firewall rules...
		# Note that you will need to delete the first rule line below when you create your own
		# firewall rules.  Refer to the Pyretic github documentation for instructions on how to
		# format these commands.
		# Example (but incomplete)
		# rule = match(srcport = int(entry['port_src']))
		# The line below is hardcoded to match TCP Port 1080.  You must remove this line
		# in your completed assignments.
		#rule = match(dstport=1080, ethtype=packet.IPV4, protocol=packet.TCP_PROTO)
		rule = get_firewall_rule(entry)
		rules.append(rule)
		pass


	allowed = ~(union(rules))

	return allowed
