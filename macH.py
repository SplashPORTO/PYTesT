#!/usr/bin/env python3

import subprocess
import optparse


parse = optparse.OptionParser()


interface = input('Qual o interfece: ')
new_mac = input('Qual o NovoMac: ')

print('[+] Changing MAC address for ' + interface + ' to ' + new_mac)



subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig",interface, "hw ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])
                # subprocess.call("ifconfig", + interface + "down", Shell=True)
                # subprocess.call("ifconfig" + interface + "hw ether" + new_mac +, Shell=True)
                # subprocess.call("ifconfig" + interface + "up", Shell=True)
