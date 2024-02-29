#!/usr/bin/python3
"""
Log parsing 0-stats.py
"""
import sys


def print_metrics(file_size, status_codes):
    """
    Print metrics
    """
    print("File size: {}".format(file_size))
    codes_sorted = sorted(status_codes.keys())
    for code in codes_sorted:
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


codes_count = {'200': 0, '301': 0, '400': 0, '401': 0,
               '403': 0, '404': 0, '405': 0, '500': 0}
file_size_total = 0
count = 0

if __name__ == "__main__":
    try:
        for line in sys.stdin:
            try:
                parts = line.split()
                if len(parts) >= 9:
                    status_code = parts[-2]
                    if status_code in codes_count:
                        codes_count[status_code] += 1
                    file_size = int(parts[-1])
                    file_size_total += file_size
            except ValueError:
                pass

            count += 1
            if count == 10:
                print_metrics(file_size_total, codes_count)
                count = 0
    except KeyboardInterrupt:
        print_metrics(file_size_total, codes_count)
        raise
    print_metrics(file_size_total, codes_count)
