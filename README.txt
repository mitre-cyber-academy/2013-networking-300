Name: Intruder Detected

Description: Alert! Our scans have detected that an intruder has come aboard. We need
you to go to sector <ip address here> and make contact! Determine if the intruder
is peaceful and whether they have anything to say for themselves.

How to Solve: Perform an nmap scan on the target. There should be a number of ports
open in the mid to high hundreds. Some of these correspond with 'known protocols,' 
but in fact aren't. By using ncat (or similar) to connect to these ports, a message
is relayed back to the user - a series of riddles that, when solved, give a numeric
sequence (1-12, missing a few). These numbers give an order of the ports. If converted
to ASCII, they give a sequence of characters, starting with MCA-. However, some
of them appear to be missing. If the scan is repeated, only with the udp flag, the
other two ports are revealed.

Notes: The program depends on Python 2.7 and the twisted framework. The program needs
to be run as root, but its privelegs will be shed (to the daemon user/group). This is
so that it can actually run on the correct ports. The firewall should be configured
to allow access on ports:

TCP:
45, 48, 49, 52, 53, 55, 65, 66, 67, 77

UDP:
49, 52

What to Distribute: Nothing, just replace the <ip address here> in the description
with the correct IP address of the server.

Flag: MCA-5411B047
