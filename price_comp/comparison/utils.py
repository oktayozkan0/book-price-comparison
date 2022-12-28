import aiohttp
import asyncio
from aiohttp import web
@staticmethod
def sort_by_value(dct):
    n = {}
    data = []
    for i,d in enumerate(dct):
        n[i] = float(d["price"])
    last = dict(sorted(n.items(), key=lambda item: item[1]))
    for i in last:
        data.append(dct[i])
    return data

@staticmethod
def get_tasks(session, websites, q):
    tasks = []
    for website in websites:
        tasks.append(session.get("http://localhost:9080/crawl.json?spider_name=%s&start_requests=true&crawl_args={\"query\":\"%s\"}" % (website, q)))
    return tasks

@staticmethod
async def async_request(websites, q):
    results = []
    async with aiohttp.ClientSession() as session:
        tasks = get_tasks(session=session, websites=websites, q=q)
        responses = await asyncio.gather(*tasks)
        for response in responses:
            data = await response.json()
            w = web.json_response(data.get("items"))
            results.extend(w)
    return results

