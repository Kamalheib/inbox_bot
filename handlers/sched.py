#!/usr/bin/evn python

"""
Inbox bot Project
Copyright(c) 2017 Inbox bot.

This program is free software; you can redistribute it and/or modify it
under the terms and conditions of the GNU General Public License,
version 2, as published by the Free Software Foundation.

This program is distributed in the hope it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
more details.

You should have received a copy of the GNU General Public License along
with this program.  If not, see <http://www.gnu.org/licenses/>.

The full GNU General Public License is included in this distribution in
the file called "COPYING".

Contact Information:
Kamal Heib <kamalheib1@gmail.com>
"""

import sys

RAW_DATA = "/work/github/inbox_bot/scheds"


class Sched(object):
    def get_raw_data(self):
        try:
            f = open(RAW_DATA, 'r')
            return f.read()
        except IOError as e:
            print "ERROR: I/O error ({0}): {1}".format(e.errno, e.strerror)
        except:
            print "ERROR: Unexpected error while opening {0} file".format(RAW_DATA)
            print sys.exc_info()[0]
            raise

    def get_scheds(self):
        if not hasattr(self, 'sched'):
            self.scheds = eval(self.get_raw_data())
        return self.scheds

    def query(self, args):
        args = args.split()

        if len(args) == 2:
            if not self.Scheds.get(args[1]):
                return "Invalid Argument, Sorry :("

            return "\n".join(self.Scheds.get(args[1]))

    Scheds = property(get_scheds)

