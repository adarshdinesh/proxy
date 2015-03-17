"""
# Use iptables to deny Connections to the actual port from outside

CON = {
    <name_of_service> : {
            'virtual' : <to_port>,
            'actual' : <running_port>
        }
    }
"""

CON = {
    'mysql': {
        'virtual': 3306,
        'actual': 10009
        }
    }
