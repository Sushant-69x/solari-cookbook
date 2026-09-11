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
        print("clicked address bar")
        await asyncio.sleep(0.3)

        await desktop.keyboard.press("End")
        for i in range(30):
            await desktop.keyboard.press("BackSpace")
        await asyncio.sleep(0.3)

        await desktop.keyboard.type("https://knapsack-map-caramel.ngrok-free.dev")
        await asyncio.sleep(0.3)
        await desktop.keyboard.press("Return")
        print("navigated")

        await asyncio.sleep(3)
        png = await desktop.screenshot(format="png")
        with open("check_warning.png", "wb") as f:
            f.write(png if isinstance(png, (bytes, bytearray)) else png.data)
        print("warning-page screenshot saved")

        await desktop.mouse.click(224, 555, humanize=True)
        await asyncio.sleep(2)

        png2 = await desktop.screenshot(format="png")
        with open("check_after_click.png", "wb") as f:
            f.write(png2 if isinstance(png2, (bytes, bytearray)) else png2.data)
        print("after-click screenshot saved")
    except Exception:
        traceback.print_exc()
    finally:
        await desktop.close()
        await desktops.destroy(desktop.sessionId)
        print("cleaned up")

asyncio.run(check())