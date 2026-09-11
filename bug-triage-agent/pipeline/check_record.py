import asyncio, os
from solari_desktop import DesktopClient

async def check():
    desktops = DesktopClient(
        api_key=os.environ["SOLARI_API_KEY"],
        base_url="https://api.getsolari.com",
    )
    desktop = await desktops.create(template="default", record=True)
    await desktop.connect()

    print("record methods:", [m for m in dir(desktop.record) if not m.startswith("_")])

    await desktop.close()
    await desktops.destroy(desktop.sessionId)

asyncio.run(check())