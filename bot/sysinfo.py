from dataclasses import dataclass

import psutil

from . import util


@dataclass
class Usage:
    capacity: str
    used: str
    free: str
    percent: str


def diskUsage(f: str) -> Usage:
    u = psutil.disk_usage(f)
    return Usage(
        used=util.humanReadable(u.used),
        capacity=util.humanReadable(u.total),
        free=util.humanReadable(u.total-u.used),
        percent=f"{u.percent:.0f}%"
    )
