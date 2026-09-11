import asyncio, os, inspect
from solari_desktop import DesktopClient

async def check():
    desktops = DesktopClient(
        api_key=os.environ["SOLARI_API_KEY"],
        base_url="https://api.getsolari.com",
    )
    desktop = await desktops.create(template="default")
    await desktop.connect()

    print("open() signature:", inspect.signature(desktop.open))
    print("process methods:", [m for m in dir(desktop.process) if not m.startswith("_")])

    result = await desktop.open("google-chrome", ["http://localhost:5000"])
    print("open() returned:", result)

    await asyncio.sleep(3)
    png = await desktop.screenshot(format="png")
    with open("check_open.png", "wb") as f:
        f.write(png if isinstance(png, (bytes, bytearray)) else png.data)

    await desktop.close()
    await desktops.destroy(desktop.sessionId)

asyncio.run(check())