#!/usr/bin/env python

"this is a test module"
"gather program initialized by Crane Zhou on 03.24.2014"

import sys
import os

debug = True

topics = ['1:v-cloud computing: openstack, cloudstack, 3rd p-payment', 
	'2:linux automatic operation: puppet, saltstack tools',
	'3:python development: web framework development']

members = ['Crane Zhou-13812345678-3-male',
	'MorningSong-138-1-male',
	'KissPuppet-138-2-male',
	'itnihao-138-1-male',
	'Finger-138-2-male']

options = ['Tech Exchange',
	'Lunch or Dinner']

def gather():
	"gather the members and topics"
	i_members_count = len(members)
	print "\r\n"
	print "Total Members:%d" % i_members_count

	i_topic_1 = i_topic_2 = i_topic_3 = 0
	for member in members:
		s_m = member.split('-')
#		print "selected topic:%s" % s_m[2]
		if s_m[2] == '1':
			i_topic_1 += 1
		elif s_m[2] == '2':
			i_topic_2 += 1
		elif s_m[2] == '3':
			i_topic_3 += 1

	if i_topic_1 > i_topic_2:
		i_topic_max = i_topic_1
	else:
		i_topic_max = i_topic_2

	if i_topic_3 > i_topic_max:
		i_topic_max = i_topic_3
	
	gather_output(i_members_count, i_topic_max)
	
#	if debug:
#		print i_topic_max

def gather_output(members_count, topic_max):
	print "Topic most selected:%s" % topic_max
	if members_count <= 6:
		print "Party Action:%s" % options[0]
	elif members_count > 6 and member_count <= 10:
		print "Party Action:%s" % options[1]

def show_title():
	"show main title"
	print "\r\n"
	print "Tech. Exchange Party"
	print "  --- SH Linux Maintainence Group"
	print "=" * 33
	print "When: 03/28/2014 19:00 Friday"
	print "Where: TBD"
	print "\r\n"
	print "Topics:"
	for topic in topics:
		print topic

def main():
	show_title()
	gather()

if __name__=='__main__':
	main()


