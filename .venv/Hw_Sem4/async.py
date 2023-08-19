import asyncio
import aiohttp
import time
from sys import argv

urls = ['https://w.forfun.com/fetch/3e/3e6d5f96bb0a293b7eb3866e91f2fd32.jpeg',
'https://w.forfun.com/fetch/ca/ca3c70c3111dde977a73ebf659a9ccc2.jpeg',
'https://mobimg.b-cdn.net/v3/fetch/32/32270e41db5c3c8763937d843a9d1fc8.jpeg',
'https://i.pinimg.com/originals/21/25/ee/2125ee74769913bb6793f249d4a8cded.jpg',
'https://i.pinimg.com/originals/8a/a7/83/8aa7831e22f8d5c74aecfe0c0e6953e3.jpg',
'https://klike.net/uploads/posts/2023-01/1674543731_3-86.jpg',
]


async def download(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as responce:
            img = await responce.read()
            filename = url.split('/')[-1]
        with open(filename, "wb") as f:
            f.write(img)
        
        print(f"Downloaded {url} in {time.time()-start_time:.2f} seconds")
    

async def main(urls):
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(download(url))
        tasks.append(task)
    await asyncio.gather(*tasks)
    
    
start_time = time.time()

if __name__ == '__main__':
    urls = argv[1:]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(urls))
    
    