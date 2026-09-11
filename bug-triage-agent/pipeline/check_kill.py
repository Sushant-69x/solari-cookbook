import asyncio, os
from solari_desktop import DesktopClient

async def check():
    desktops = DesktopClient(
        api_key=os.environ["SOLARI_API_KEY"],
        base_url="https://api.getsolari.com",
    )
    desktop = await desktops.create(template="default")
    try:
        await desktop.connect()

        result = await desktop.process.start("google-chrome", args=["http://localhost:5000"])
        print("started pid:", result)

        await asyncio.sleep(5)
        png = await desktop.screenshot(format="png")
        with open("check_kill.png", "wb") as f:
            f.write(png if isinstance(png, (bytes, bytearray)) else png.data)
    finally:
        await desktop.close()
        await desktops.destroy(desktop.sessionId)

asyncio.run(check())