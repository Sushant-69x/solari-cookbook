import asyncio, os, traceback
from solari_desktop import DesktopClient

async def check():
    desktops = DesktopClient(
        api_key=os.environ["SOLARI_API_KEY"],
        base_url="https://api.getsolari.com",
    )
    desktop = await desktops.create(template="default")
    try:
        await desktop.connect()
        print("connected")

        await desktop.mouse.click(314, 125, humanize=True)
        print("clicked")
        await asyncio.sleep(0.3)

        await desktop.keyboard.press("End")
        print("end pressed")
        for i in range(30):
            await desktop.keyboard.press("BackSpace")
        print("backspaced")
        await asyncio.sleep(0.3)

        await desktop.keyboard.type("http://localhost:5000")
        print("typed url")
        await asyncio.sleep(0.3)

        await desktop.keyboard.press("Return")
        print("return pressed")

        await asyncio.sleep(3)
        png = await desktop.screenshot(format="png")
        with open("check_typeurl.png", "wb") as f:
            f.write(png if isinstance(png, (bytes, bytearray)) else png.data)
        print("screenshot saved")
    except Exception:
        traceback.print_exc()
    finally:
        await desktop.close()
        await desktops.destroy(desktop.sessionId)
        print("cleaned up")

asyncio.run(check())