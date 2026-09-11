import asyncio, os, inspect
from solari_desktop import DesktopClient

async def check():
    desktops = DesktopClient(
        api_key=os.environ["SOLARI_API_KEY"],
        base_url="https://api.getsolari.com",
    )
    desktop = await desktops.create(template="default")
    try:
        await desktop.connect()
        print("keyboard methods:", [m for m in dir(desktop.keyboard) if not m.startswith("_")])
        print("press signature:", inspect.signature(desktop.keyboard.press))
        print("type signature:", inspect.signature(desktop.keyboard.type))
    finally:
        await desktop.close()
        await desktops.destroy(desktop.sessionId)

asyncio.run(check())