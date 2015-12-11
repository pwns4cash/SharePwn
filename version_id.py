import logging
import re

import requests
import url_processor

__author__ = '0rigen'
__email__ = "0rigen@0rigen.net"
__status__ = "Prototype"

red = "\033[31m"  # usually for errors, [X] items
cyan = "\033[36m"
yellow = "\033[33m"  # usually for information and requests, the [?] items
green = "\033[92m"  # Information and success, [!]
blue = "\033[94m"
endc = "\033[0m"
bold = "\033[1m"
underline = "\033[4m"


# SP Versions are identified in the response headers as 'MicrosoftSharePointTeamServices': 'X.X.X.X'
# Identify SP versions via initial GET request
# 2010 will start with 14, like 14.0.0.6010
# 2013 will start with 15.
# 2007 will start with 12.
# 2003 will start with 6.

# TODO Research what difference the version makes to interrogation functions.
# TODO Different service names and standards, etc.


####################################################
# identify                                         #
# Record a response from the target and examines   #
# the headers for SP version information           #
# @url - the target                                #
# @ port - the target port                         #
####################################################
def identify(url, port=None):
    # TODO: Use the servreg and aspreg to also identify server software and asp version information, if present

    # Regex to look for #.#.#.# format, where # is 1 or more numbers, dot separated
    spreg = re.compile("[\']([6,12,14,15]+\.)+(\d+\.)+(\d+\.)+(\d*)[\']")
    # Regex to identify Server in use
    servreg = re.compile("[\']Server[\']: [\'](.+?)\'")
    # Regex to identify ASP version, if any
    aspreg = re.compile("[\']X-AspNet-Version[\']: [\'](\d+\.)?(\d+\.)?(\d+\.)?(\d*)[\']")

    # Process the link, if port is specified
    if port is not None:
        link = url_processor.checkhttp(url, port)
    else:
        link = url

    # Request the page
    r = requests.get(link)

    # Check for a successful response
    status_code = str(r.status_code)
    success_code = re.match("(2)\w", status_code)  # Check for successful response code

    if success_code is None:  # Return 'Unknown' if request unsuccessful
        print(
            yellow + "[!] Unsuccessful request when attempting to identify SP version.  Version remains Unknown..." + endc)
        logging.info("Version ID failed; did not sp_match 2xx response regex")
        return "Unknown"

    # Search for version info in headers
    sp_match = re.search(spreg, str(r.headers))  # Otherwise, keep working
    asp_match = re.search(aspreg, str(r.headers))
    serv_match = re.search(servreg, str(r.headers))

    # Process SharePoint version
    if sp_match is None:  # No version info returned
        print(yellow + "[!] No SharePoint version information returned." + endc)
        logging.info("Version ID failed; successful request but no version information found.")
    else:
        ver = str(sp_match.group())  # Store the version info and return
        print(green + "\n[*] SharePoint version identified as " + bold + "%s" % ver + endc)
        logging.info("SP Version ID successful. Found %s" % ver)
        if ver.startswith("6"):
            print(green + bold + "SharePoint 2003" + endc)
        if ver.startswith("14"):
            print(green + "SharePoint 2010" + endc)

    # Process ASP version
    if asp_match is None:  # No version info returned
        print(yellow + "[!] ASP version not identified." + endc)
        logging.info("ASP version ID failed; successful request but no version information found.")
    else:
        ver = str(asp_match.group())  # Store the version info and return
        print(green + "\n[*] ASP version identified as " + bold + "%s" % ver + endc)
        logging.info("ASP Version ID successful. Found %s" % ver)

    # Process Server version
    if serv_match is None:  # No version info returned
        print(yellow + "[!] No Server version information returned." + endc)
        logging.info("Server version ID failed; successful request but no version information found.")
    else:
        ver = str(serv_match.group())  # Store the version info and return
        print(green + "\n[*] Server version identified as " + bold + "%s" % ver + endc)
        logging.info("Server version ID successful. Found %s" % ver)

    return ver
