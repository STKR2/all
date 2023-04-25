
import asyncio
import importlib

from pytgcalls import idle
from rich.table import Table
from rich.console import Console
from Telugucoders.core.clientbot import  call_py, bot

console = Console()
loop = asyncio.get_event_loop()


async def eSport_boot():
    header = Table(show_header=True, header_style="bold yellow")
    header.add_column(
        "Amala MusicX : Best Ever Music Bot"
    )
    console.print(header)
    console.print("┌ [red]Starting Your Music Bot Client ...\n")
    await bot.start()
    console.print("└ [green]Started Music Bot Client")
    console.print("\n┌ [red]Booting Up The User Client...")
    await call_py.start()
    console.print("├ [yellow]Booted User Client")
    console.print("└ [green]Successfully Started Music Bot ...")
    await idle()
    print(f"ɢᴏᴏᴅʙʏᴇ!\nStopping @Telugucodersupdates")
    await bot.stop()

if __name__ == "__main__":
    loop.run_until_complete(eSport_boot())
