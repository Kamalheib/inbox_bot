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
from handlers.sched import Sched
from argparse import ArgumentParser
from slackclient import SlackClient


class Bot(object):

    def get_parser(self):
        if not hasattr(self, "parser"):
            self.parser = ArgumentParser(self.__class__.__name__)
        return self.parser

    def parse_args(self, args):
        self.Parser.add_argument('-t', '--token_file', help='path to token file')
        self.Parser.parse_args(namespace=self, args=args)

    def get_token(self):
        if not hasattr(self, 'token'):
            try:
                f = open(self.token_file, 'r')
                self.token = f.read().strip()
            except IOError as e:
                print "ERROR: I/O error ({0}): {1}".format(e.errno, e.strerror)
            except:
                print "ERROR: Unexpected error while opening {0} file".format(token_file)
                print sys.exc_info()[0]
                raise
        return self.token

    def get_client(self):
        if not hasattr(self, 'client'):
            try:
                self.client = SlackClient(self.Token)
            except:
                print "ERROR: Failed to create slack client"
                print sys.exc_info()[0]
                raise
        return self.client

    def handle_message(self, channel, text):
        print text
        if 'sched' in text:
            self.Client.rtm_send_message(channel, str(Sched().query(text)))

    def start(self, args):
        self.parse_args(args)
        if not self.Client.rtm_connect():
            print "ERROR: Failed to connect to slack service."
            return 1

        while True:
            for slack_msg in self.Client.rtm_read():
                text = slack_msg.get("text")
                channel = slack_msg.get("channel")
                if not text or not channel:
                    continue
                self.handle_message(channel, text)

        return 0

    Token = property(get_token)
    Client = property(get_client)
    Parser = property(get_parser)

if __name__ == '__main__':
    sys.exit(Bot().start(sys.argv[1:]))
