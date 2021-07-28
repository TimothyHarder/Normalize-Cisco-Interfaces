import re


def convert_interface(interface_name):
    """
    Converts interface names to and from the abbreviated and non-abbreviated versions.
    If you pass in an abbreviated one, it will expand it, and if you pass in a non-abbreviated one, it will shorten it.

    :param interface_name: Whole name including the number of a Cisco Interface. (i.e. GigabitEthernet1/1)
    :return: Converted Interface Name
    """

    # Dictionary containing the conversions.
    interface_abbreviations = {
        'Ethernet': 'Eth',
        'FastEthernet': 'Fa',
        'GigabitEthernet': 'Gi',
        'TenGigabitEthernet': 'Te',
        'TwentyFiveGigE': 'Twe',
        'Port-channel': 'Po',
        'HundredGigE': 'Hu',
        'FortyGigabitEthernet': 'Fo',
        'Loopback': 'Lo',
        'Tunnel': 'Tu',
        'mgmt': 'mgmt',
        'Embedded-Service-Engine': 'Em',
        'Bundle-Ether': 'BE',
        'Null': 'Nu',
        'tunnel-ip': 'ti',
        'MgmtEth': 'Mg',
        'TenGigE': 'Te',
        'Vlan': 'Vl',
        'GMPLS': 'GM',
        'pseudowire': 'pw',
        'BDI': 'BD',
        'LISP': 'LI',
        'nve': 'nv',
    }

    if type(interface_name) != str:
        return interface_name

    if not interface_name:
        return interface_name

    interface_regex = r'^([^\d]+)(\d+.*)$'

    match = re.match(interface_regex, interface_name)
    if match:
        interface_type = match.group(1)
        interface_number = match.group(2)

        for long, short in interface_abbreviations.items():
            if long.lower() == interface_type.lower():
                return short + interface_number
            elif short.lower() == interface_type.lower():
                return long + interface_number

    return interface_name
