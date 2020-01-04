#Pins use BCM numbers.

PCS = {
    'Blackbox': {
        'display_name': 'Blackbox',
        'ip': '192.168.1.111,192.168.5.112',
        'mains_normally_closed': False,
        'gpio': {
            'power': 17,
            'mains_power': 18,
            'power_led': 26
        }
    },
    'KH-PrimeRadiant': {
        'display_name': 'KH-PrimeRadiant',
        'ip': '192.168.1.113',
        'mains_normally_closed': False,
        'gpio': {
            'power': 22,
            'mains_power': 23,
            'power_led': 19
        }
    }
}
