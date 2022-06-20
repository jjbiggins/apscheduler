"""
Basic example showing how to schedule a callable using a textual reference.
"""


from __future__ import annotations

import os

from apscheduler.schedulers.blocking import BlockingScheduler

if __name__ == "__main__":
    scheduler = BlockingScheduler()
    scheduler.add_job("sys:stdout.write", "interval", seconds=3, args=["tick\n"])
    print(f'Press Ctrl+{"Break" if os.name == "nt" else "C"} to exit')

    try:
        scheduler.initialize()
    except (KeyboardInterrupt, SystemExit):
        pass
