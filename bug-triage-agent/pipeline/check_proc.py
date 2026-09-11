import asyncio, os, inspect
from solari_desktop import DesktopClient

async def check():
    desktops = DesktopClient(
        api_key=os.environ["SOLARI_API_KEY"],
        base_url="https://api.getsolari.com",
    )
    desktop = await desktops.create(template="default")
    await desktop.connect()

    procs = await desktop.process.list()
    print("running procs:", procs)

    print("process.start signature:", inspect.signature(desktop.process.start))

    result = await desktop.process.start(
        "google-chrome", args=["--new-window", "http://localhost:5000"]
    )
    print("process.start returned:", result)

    await asyncio.sleep(3)
    png = await desktop.screenshot(format="png")
    with open("check_proc.png", "wb") as f:
        f.write(png if isinstance(png, (bytes, bytearray)) else png.data)

    await desktop.close()
    await desktops.destroy(desktop.sessionId)

asyncio.run(check())