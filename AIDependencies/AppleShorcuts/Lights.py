import aiohttp

async def turnOn():
    async with aiohttp.ClientSession() as session:
        await session.post("https://api.pushcut.io/6WHL06znhsDKYmfKbaed2/execute?shortcut=Strip%20on")

async def turnOff():
    async with aiohttp.ClientSession() as session:
        await session.post("https://api.pushcut.io/6WHL06znhsDKYmfKbaed2/execute?shortcut=Strip%20off")