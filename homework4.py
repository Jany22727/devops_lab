from config import interval
from config import output
from config import output_file_name
from datetime import datetime
import json
from prettytable import PrettyTable
import psutil
from time import sleep


class Metrics(object):
    snapshot_number = 0

    def __init__(self):
        self.snapshot_number = Metrics.snapshot_number
        self.time = datetime.strftime(datetime.now(), "%H:%M:%S")
        self.date = datetime.strftime(datetime.now(), "%d.%m.%Y")
        self.cpu = psutil.cpu_percent(interval=1)
        self.memory = psutil.virtual_memory().total / (1024 * 1024)
        self.v_memory = psutil.virtual_memory().percent
        self.io_read = psutil.disk_io_counters()[2] / (1024 * 1024)
        self.io_write = psutil.disk_io_counters()[3] / (1024 * 1024)
        self.net_ip = (psutil.net_connections()[1]).laddr[0]
        self.net_port = (psutil.net_connections()[1]).laddr[1]
        self.net_status = (psutil.net_connections()[1]).status
        Metrics.snapshot_number += 1

    @staticmethod
    def get_snapshot_number():
        return Metrics.snapshot_number

    def get_time(self):
        return self.time

    def get_date(self):
        return self.date

    def get_cpu(self):
        return self.cpu

    def get_memory(self):
        return self.memory

    def get_v_memory(self):
        return self.v_memory

    def get_io_read(self):
        return self.io_read

    def get_io_write(self):
        return self.io_write

    def get_net_ip(self):
        return self.net_ip

    def get_net_port(self):
        return self.net_port

    def get_net_status(self):
        return self.net_status

    def system_state(self):
        return [count, self.time, self.date, self.cpu, self.memory,
                self.v_memory, self.io_read, self.io_write,
                self.net_ip, self.net_port, self.net_status]


test = Metrics()


def pt(x):
    """Create pretty table"""
    mpt = PrettyTable()
    mpt.field_names = [
        "Snpsh#", "Time", "Date", "CPU",
        "Memory MB", "Memory %", "IO read MB",
        "IO write MB", "local IP", "PORT", "Status"
    ]
    mpt.add_row(x)
    return mpt.get_string()


def write_txt(z):
    """Write information in txt file"""
    out_file = open(output_file_name, "a")
    out_file.write(z + '\n')
    out_file.close()


def write_json(y):
    """Write  information in json file"""
    out_file = open(output_file_name, "a", newline='\r\n')
    out_file.write(json.dumps(y + '\n'))
    out_file.close()


count = 0

if output == "txt":
    while True:
        write_txt(pt(test.system_state()))
        count += 1
        sleep(interval)

if output == "json":
    while True:
        write_json(pt(test.system_state()))
        count += 1
        sleep(interval)
