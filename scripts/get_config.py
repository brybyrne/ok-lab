from ncclient import manager
import sys
import xml.dom.minidom

# the variables below assume the user is leveraging the
# Vagrant image provided with the live delivery.  If running this
# as a self learning lab substitute your device details
# The IP address of your router/switch
HOST = 's2-r1.en-lab.local'
# use the NETCONF port for your CSR1000V device
PORT = 830
# use the user credentials for your CSR1000V device
USER = 'localadmin'
PASS = 'C1sco,123'

def main():
    """
    Main method that prints netconf capabilities of remote device.
    """
    # Create a NETCONF session to the router with ncclient
    with manager.connect(host=HOST, port=PORT, username=USER,
                         password=PASS, hostkey_verify=False,
                         device_params={'name': 'default'},
                         allow_agent=False, look_for_keys=False) as m:

        # Retrieve the configuraiton
        results = m.get_config('running')
        # Print the output in a readable format
        print(xml.dom.minidom.parseString(results.xml).toprettyxml())


if __name__ == '__main__':
    sys.exit(main())
