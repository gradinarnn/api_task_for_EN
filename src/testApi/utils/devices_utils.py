from random import choice

from randmac import RandMac


def get_dev_type():
    return choice(('emeter', 'zigbee', 'lora', 'gsm'))

def generate_mac_addr():
    return str(RandMac())