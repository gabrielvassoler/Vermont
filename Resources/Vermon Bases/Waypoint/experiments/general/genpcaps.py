#!/usr/bin/env python3
import argparse
import sys
import socket
import random
import struct
import string
import math
import os
import json

from scapy.all import sendp, send, get_if_list, get_if_hwaddr
from scapy.utils import wrpcap
from scapy.all import Packet
from scapy.all import Ether, IP, UDP, UDP


def Yred(x):
    return 1

def Yblue(x):
    return 1

def Yteal(x):
    return 1

def Ygreen(x):
    return 1

def Yorange(x):
    return 1


def gen_pkts(src_addr, dst_addr, src_port, dst_port, yfunc, lorem, seconds, msglen, hdslen, add_noise=True):
    random.seed(42)
    x = 0
    i = 0
    pkts = []
    while (x < 1.0):
        # build packet
        beg = random.randint(0, 1e6 - msglen - 1)
        pkt = Ether() / IP(src=src_addr, dst=dst_addr) / \
            UDP(sport=src_port, dport=dst_port) / lorem[beg:beg+msglen]
        pkt.time = x
        pkts.append(pkt)

        # calculate arrival time for next packet
        delay = 1.0/((yfunc(x)*1e6)/(8*(hdslen + msglen)))
        if add_noise is True:
            noise = random.gauss(1, 0.1)
        else:
            noise = 1.0
        x = x + noise*delay
        # count pkts
        i = i + 1
        # if i%1000 == 0:
        #     print(i, end='', flush=True)
        # elif i%100 == 0:
        #     print(end='.', flush=True)
    print('done')
    return pkts

def main():
    print('Building random string')
    letters = string.ascii_letters + string.digits
    lorem = ''.join(random.choice(letters) for i in range(int(1e6)))
    print('done')

    seconds = 1.0
    maxframesize = 1518 - 4  # Frame Check Sequence
    hdslen = 14 + 20 + 8  # Eth + IPv4 + UDP
    tellen = 36  # IntSight + Vermon
    msglen = maxframesize - hdslen - tellen

    os.makedirs('../../resources/workloads/general')

    path = ''

    with open('../../path', 'r') as f:
        path = json.load(f)

    src = '10.0.' + path['src'] + '.'  + path['src']
    dst = '10.0.' + path['dst'] + '.'  + path['dst']

    print('Generating traffic for RED flow (h'+path['src']+'-h'+path['dst']+')')
    pkts = gen_pkts(src, dst, 1234, 1234, Yred, lorem, seconds, msglen, hdslen)
    #print('Writting traffic to pcap file', flush=True)
    wrpcap('../../resources/workloads/general/red.pcp', pkts)
    print('done')

    c = 1
    for pair in path['cflows']:
        src = pair[0]
        dst = pair[1]

        ipsrc = '10.0.' + str(src) + '.'  + str(src)
        ipdst = '10.0.' + str(dst) + '.'  + str(dst)

        print('Generating traffic for f{} flow (h'.format(c)+str(src)+'-h'+str(dst)+')')
        pkts = gen_pkts(ipsrc, ipdst, 1234+c, 1234+c, Yred, lorem, seconds, msglen, hdslen)
        wrpcap('../../resources/workloads/general/f{}.pcp'.format(c), pkts)
        print('done')

        with open('workload.json', 'r') as f:
            wl = json.load(f)


        new_flow = {}
        new_flow['sender'] = 'h' + str(src)
        new_flow['receiver'] = 'h' + str(dst)
        new_flow['receiver_opt'] = '10.0.'+str(dst) + '.' +str(dst) + ' ' + str(1234+c)
        new_flow['sender_opt'] = '--preload-pcap --stats=1 resources/workloads/general/f{}.pcp'.format(c)
        new_flow['sender_log'] = 'f{}-s.txt'.format(c)
        new_flow['receiver_log'] = 'f{}-r.txt'.format(c)
        new_flow['start_delay'] = 0
        new_flow['duration'] = 1

        wl['tcpreplay'].append(new_flow)


        with open('workload.json', 'w') as f:
            json.dump(wl, f)

        c += 1


if __name__ == '__main__':
    main()
