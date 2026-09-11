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
        print("display methods:", [m for m in dir(desktop.display) if not m.startswith("_")])
        print("screenshot signature:", inspect.signature(desktop.screenshot))

        await desktop.process.start("google-chrome", args=["http://localhost:5000"])
        await asyncio.sleep(5)

        png = await desktop.screenshot(format="png")
        with open("check_display.png", "wb") as f:
            f.write(png if isinstance(png, (bytes, bytearray)) else png.data)
    finally:
        await desktop.close()
        await desktops.destroy(desktop.sessionId)

asyncio.run(check())