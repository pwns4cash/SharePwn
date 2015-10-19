import argparse
import logging
import sys
import brute_browse

__author__ = '0rigen'
__email__ = "0rigen@0rigen.net"
__status__ = "Prototype"


def banner():
    print("""
      ___   _                         ___
     / __| | |_    __ _   _ _   ___  | _ \ __ __ __  _ _
     \__ \ | ' \  / _` | | '_| / -_) |  _/ \ V  V / | ' \\
     |___/ |_||_| \__,_| |_|   \___| |_|    \_/\_/  |_||_|  V.01

    SharePoint Security Auditing by @_0rigen / 0rigen.net""")

# TODO:
# Create argument parsing to call features on-demand rather than monolithic and such
#
#  Output structure: ! - info, X - error, * - finding/positive
#########################################
# Command Line Arguments #
# -u URL of target
# -L file-based list of brute browsing targets
# -O specify output file rather than stdout
#########################################

try:
    # Parse argument
    parser = argparse.ArgumentParser()
    parser.add_argument("-target", type=str, help="URL of the target SP site")
    parser.add_argument("-browse", help="Perform Brute-Force Browsing")
    parser.add_argument("-pick", help="Perform Enumeration via Picker Service")
    parser.add_argument("-uid", help="Perform Brute-Force User ID Search")
    args = parser.parse_args()
    target = args.target

    # Error if no target specified
    if target is None:
        print("No target specified.  Use -t to specify the target URL")
        sys.exit(1)

    else:
        # Welcome to SharePwn
        banner()

        # Set Logging level (based on command line arg in the future
        logging.basicConfig(stream=sys.stdout, level=logging.ERROR)

        ans = raw_input("Perform brute force browsing? (y/n): ")
        if ans == 'y':
            finds = brute_browse.geturlcode(target, None, "service_list.txt")
            print ("\n")
            print ("I found"),
            print finds

except KeyboardInterrupt:
    print("\n\nYour keys interrupted meh! Quitting...")
    sys.exit(0)
except:
    print("Unknown error; iunno d00d...")
    sys.exit(1)


