#!/usr/bin/env python

import subprocess
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", '--interface', dest='interface', help='Interface to change its Mac address')
    parser.add_option('-m', '--mac', dest='new_mac', help='New Mac address')
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error('[-] Please specify an interface, use -- help for more info.')
    elif not options.new_mac:
        parser.error('[-] Please specify a new mac, use --help for more info.')
        return options


def create_file(name):
    with open(name, 'w') as f:
        f.write('memasik')


def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + "to " + new_mac)
    subprocess.call(['ifconfig', interface, 'down'])
    subprocess.call(['ifconfig', interface, 'hr', new_mac])
    subprocess.call(['ifconfig', interface, 'up'])


def main():
    options = get_arguments()
    change_mac(options.interface, options.new_mac)


if __name__ == '__main__':
    main()
    # options = get_arguments()
    # change_mac(options.interface, options.new_mac)

    # ifconfig_result = subprocess.check_output(['ifconfig', options.interface])
    # print(ifconfig_result)
