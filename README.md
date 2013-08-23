# Postfix Queue Management

## Overview
Basic Postfix queue management for rapid deletion of emails. It consists of both a command line utility and a basic
class / library which can be integrated into other systems.

The code is GPL2 licensed, so please feel free to fork or contribute!

----
Tim Butler

## Required packages
- docopt
- blessings

## Installation

```bash
pip install -e git+https://github.com/timbutler/postmgt.git
```

## Usage
This help can be also found by calling postmgt --help

``` bash
Usage:
  postmgt count
  postmgt list
  postmgt deletefrom  <from>
  deleteto <to>
  postmgt deletesubject <subject>
  viewemail <messageid>
  viewheaders <messageid>

Arguments:
  count                        Display a count of the emails in the queue
  list                         Display a list of all emails in the queue
  viewemail <messageid>        View an email
  viewheaders <messageid>      View the headers of an email
  deleteto <to>                Delete email from the queue based on sender (from) address
  deletefrom <from>            Delete email from the queue based on sender (from) address
  deletesubject <subject>      Delete email from the queue based on subject

Examples:
  postmgt deletefrom spammer@domain.com
  postmgt deletesubject "Failure Notice"
  postmgt count
  postmgt viewheaders 1244E4206881
```

## TODO
Here's a list of future tasks, please feel free to contribute!
 - Publish to the Python Package Index (PyPi)
 - Full PEP8 audit
 - Add validation for message ID for deletion etc
 - Add validation of message deletion
 - Show how long the email has been in the queue
 - Delete emails older than `x` days in the queue