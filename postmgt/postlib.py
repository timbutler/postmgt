""" Postfix Queue Management - Base Library """

import re
import subprocess
from blessings import Terminal


class PostFixQueueMgt(object):

    def __init__(self, ):
        self.cmd_mailq = 'mailq'
        self.cmd_postqueue = 'postqueue'
        self.cmd_postcat = 'postcat'
        self.cmd_postsuper = 'postsuper'

    def _processoutput(self, cmd, splitlines=True):
        """ Execute a process and return the STDOUT """

        data = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT, close_fds=True).communicate()[0]
        if splitlines:
            return data.splitlines()
        else:
            return data

    def emaillist(self):
        """ Returns a list of dict's of emails """

        data = iter(self._processoutput(self.cmd_mailq))
        emaillist = []

        for line in data:
            email = {}

            # Find ID as the first line (postqueue output is a cluster of 3 lines)
            if re.match('^(\w{8,12})+', line):
                match = re.match('^(\w{8,12})\*?\s+(\d+)\s+(\w{3}\s\w{3}\s\d{1,2}\s\d{2}:\d{2}:\d{2})\s+(.*)', line)

                email['ID'] = match.group(1)
                email['Size'] = match.group(2)
                email['Date'] = match.group(3)
                email['From'] = match.group(4)
                email['Reason'] = next(data).strip()
                email['To'] = next(data).strip()
                email['Subject'] = ""

                # Find the subject
                for msgline in self._processoutput(self.cmd_postcat + " -h -q %s" % email['ID']):
                    if msgline.startswith('Subject: '):
                        email['Subject'] = msgline.replace('Subject: ', '')

                emaillist.append(email)

        return emaillist

    def _delete(self, item, search):
        """ Simple wrapper function for email deletion """

        t = Terminal()

        for email in self.emaillist():
            if re.match(search.strip(), email[item]):
                print ("Deleting Email {t.bold}[ID]{t.normal}: %s, {t.yellow}[Subject]:{t.normal}=%s" %
                       (email['ID'], email['Subject'])).format(t=t)
                delout = self._processoutput(self.cmd_postsuper + ' -d %s' % email['ID'], splitlines=False)

    def delete_subject(self, subject):
        """ Deletes emails from the PostFix Queue based on the Subject"""
        self._delete('Subject', subject)

    def delete_from(self, fromemail):
        """ Deletes emails from the PostFix Queue based on the FROM address """
        self._delete('From', fromemail)

    def delete_to(self, toemail):
        """ Deletes emails from the PostFix Queue based on the TO address """
        self._delete('To', toemail)

    def count(self):
        """ Returns the number of emails in the queue """
        output = self._processoutput(self.cmd_mailq)
        if output[0].find('Mail queue is empty') > -1:
            return 0
        else:
            match = re.match(r".* in (\d+) Requests.", output[len(output)-1])
            if match:
                return int(match.group(1))
            else:
                return 0

    def view(self, messageid, headersonly=False):
        """ Returns a copy of the email as a string, headersonly = only the headers of the email"""

        if headersonly:
            return self.self._processoutput(self.cmd_postcat + " -h -q %s" % messageid, splitlines=False)
        else:
            return self._processoutput(self.cmd_postcat + " -q %s" % messageid, splitlines=False)