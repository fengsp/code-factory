# -*- coding: utf-8 -*-
"""
    Scanner
    ~~~~~~~
"""

from socket import *


def scan_conn(host, port):
    try:
        conn = socket(AF_INET, SOCK_STREAM)
        conn.connect((host, port))
        print '[+]%d/tcp open' % port
        conn.close()
    except:
        print '[-]%d/tcp closed' % port


def scan_port(host, ports):
    try:
        ip_addr = gethostbyname(host)
    except:
        print "[-] Cannot resolve '%s': Unknown host" % ip_addr
        return
    try:
        host_name = gethostbyaddr(ip_addr)
        print '\n[+] Scan Results for: ' + host_name[0]
    except:
        print '\n[+] Scan Results for: ' + ip_addr
    setdefaulttimeout(1)
    for t_port in ports:
        print 'Scanning port ' + str(t_port)
        scan_conn(host, t_port)


if __name__ == "__main__":
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("-H", "--host", dest="t_host", help="target host")
    parser.add_option("-p", "--port", dest="t_port", help="target port")
    (options, args) = parser.parse_args()

    t_host = options.t_host
    t_port = options.t_port
    if t_host is None or t_port is None:
        print "Use -h for help"
        exit(0)
    scan_port('www.baidu.com', (23, 80, 443))
