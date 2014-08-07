# Copyright (C) 2014  Andrea De Pasquale <andrea@de-pasquale.name>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import logging


logger = logging.getLogger(__name__)


class CommandResponder(object):
    def __init__(self, template):
        self.command_not_found = (
            "\r\n"
            "? Command not found.\r\n"
            "Send 'H' for help.\r\n"
        )

        self.service_menu = (
            "==============================================================================\r\n"
            "Service Menu\r\n"
            "==============================================================================\r\n"
            "H:   Help [cmd].\r\n"
            "Q:   Close connection.\r\n"
            "!AC: Access control.\r\n"
            "!AS: Alarm Server.\r\n"
            "!GC: Get Config.\r\n"
            "!GV: Software version.\r\n"
            "!SA: Set KAP Server IP and port (*1).\r\n"
            "!SB: Set 2nd KAP Server IP and port.\r\n"
            "!SC: Set Config (*1).\r\n"
            "!SD: Set device name (*1).\r\n"
            "!SH: Set KAP Server lookup (DNS or DHCP)\r\n"
            "!SI: Set IP (enter either valid IP or 0 to force DHCP)(*1).\r\n"
            "!SK: Set KAP watchdog timeout(WDT).\r\n"
            "!SN: Set IP for DNS Name servers to use.\r\n"
            "!SP: Set IP Ports\r\n"
            "!SS: Set Serial Settings.\r\n"
            "!RC: Request connect\r\n"
            "!RR: Request restart (*1).\r\n"
            "!WM: Wink module.\r\n"
            "==============================================================================\r\n"
            "(*1) Forces system restart\r\n"
            "==============================================================================\r\n"
            "Kamstrup (R)\r\n"
        )

        self.invalid_parameter = (
            "\r\n"
            "? Invalid parameter.\r\n"
            "Try 'H cmd' for specific help.\r\n"
            " Ie: H !SC\r\n"
        )

        self.help_GC = (
            "!GC: Get Config.\r\n"
            "     Returns the module configuration.\r\n"
        )

        self.command_GC = (
            "Device Name         : {}\r\n"
            "Use DHCP            : {}\r\n"
            "IP addr.            : {}\r\n"
            "IP Subnet           : {}\r\n"
            "Gateway addr.       : {}\r\n"
            "Service server addr.: {}\r\n"
            "Service server hostname.: {}\r\n"
            "DNS Server No. 1: {}\r\n"
            "DNS Server No. 2: {}\r\n"
            "DNS Server No. 3: {}\r\n"
            "MAC addr. (HEX)     : {}\r\n"
            "Channel A device meterno.: {}\r\n"
            "Channel B device meterno.: {}\r\n"
            "Keep alive timer (flash setting): {} {}\r\n"
            "Keep alive timer (current setting): {} {}\r\n"
            "Has the module received acknowledge from the server: {}\r\n"
            "KAP Server port: {}\r\n"
            "KAP Local port: {}\r\n"
            "Software watchdog: {} {}\r\n"
        )

        self.help_GV = (
            "!GV: Software version.\r\n"
            "     Returns the software revision of the module.\r\n"
        )

        self.command_GV = (
            "\r\n"
            "Software Version: {}\r\n"
        )

    def respond(self, request):
        stripped_request = request.strip()
        split_request = stripped_request.split(" ", 1)
        command = split_request[0].upper()

        if len(command) > 3:
            return self.command_not_found

        if command.startswith("Q"):
            return  # quit

        if command.startswith("H"):
            if len(split_request) > 1:
                return self.show_help(split_request[1])
            return self.service_menu

        if command.startswith("!"):
            return self.run_command(command)

        return ""  # default: idle

    def show_help(self, command):
        if command == "!GC":
            return self.help_GC
        if command == "!GV":
            return self.help_GV

        # TODO implement help
        return self.invalid_parameter

    def run_command(self, command, params=None):
        if command == "!GC":
            return self.command_GC  # TODO format
        if command == "!GV":
            return self.command_GV  # TODO format

        # TODO implement commands
        return self.command_not_found
