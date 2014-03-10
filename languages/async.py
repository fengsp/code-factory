# -*- coding: utf-8 -*-
"""
    http://compiletoi.net/fast-scraping-in-python-with-asyncio.html
"""
import asyncio
import aiohttp


@asyncio.coroutine
def print_page(url):
    response = yield from aiohttp.request('GET', url)
    body = yield from response.read_and_close(decode=True)
    print(len(body))


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(print_page('http://www.apple.com'))
