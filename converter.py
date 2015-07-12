#!/usr/bin/env python
# -*- coding=utf-8 -*-

import sys
from workflow import Workflow
from requests import get
from re import search

def main(wf):
    query = wf.args[0]

    try:
        url = "https://twitter.com/intent/user?user_id=%s" % int(query)
        pattern = '\"twitter://user\?screen_name=(\w+)\">'
    except:
        url = 'https://twitter.com/' + query
        pattern = 'data-user-id=\"([0-9]+)\"'

    html = get(url).text

    try:
        text = search(pattern, html).group(1)
    except:
        text = 'Not Found'

    wf.add_item(title = text, subtitle = query, icontype = 'icon', arg = text, valid = True)
    wf.send_feedback()

if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))
