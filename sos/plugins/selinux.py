### This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.

## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.

## You should have received a copy of the GNU General Public License
## along with this program; if not, write to the Free Software
## Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

from sos.plugins import Plugin, RedHatPlugin

class selinux(Plugin, RedHatPlugin):
    """selinux related information
    """

    option_list = [("fixfiles", 'Print incorrect file context labels', 'slow', False)]
    packages = ('libselinux',)

    def setup(self):
        # sestatus is always collected in check_enabled()
        self.add_copy_spec("/etc/selinux")
        if self.get_option('fixfiles'):
            self.add_cmd_output("fixfiles -v check")
        self.add_cmd_output("sestatus -b")
        self.add_cmd_output("selinuxdefcon root")
        self.add_cmd_output("selinuxconlist root")
        self.add_cmd_output("selinuxexeccon /bin/passwd")

