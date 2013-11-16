# -*- coding: utf-8 -*-
"""
    RQ Demos
    ~~~~~~~~

    RQ(Redis Queue)

    The life-cycle of a worker:
    1. Boot. Loading the Python environment.
    2. Birth registration. The worker register itself to the system
    3. Start listening.
    4. Fork a child process. A child process do the actual job.
    5. Process work.
    6. Loop back to step 3.

"""
import requests
from redis import Redis
from rq import Queue

from testmodule import count_words_at_url


q = Queue('fsp', connection=Redis(db=1))


result = q.enqueue(count_words_at_url, 'http://www.baidu.com')
print type(result)
