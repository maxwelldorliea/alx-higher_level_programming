#!/usr/bin/python3

"""Statistic Module."""
import fileinput


def print_stats(filesize: int, status_dict: dict) -> None:
    """Print Statistic."""
    print(f"File size: {filesize}")
    for k in sorted(list(status_dict.keys())):
        print(f"{k}: {status_dict[k]}")


def main():
    """Parse Arguments."""
    valid_status = [200, 301, 400, 401, 403, 404, 405, 500]
    i = 0
    status_dict = {}
    total_file_size = 0
    try:
        for line in fileinput.input():
            host = line.split()

            try:
                filesize = host[-1]
                total_file_size += int(filesize)
            except Exception:
                pass

            try:
                status = host[-2]
                if int(status) in valid_status:
                    status_dict[status] = 1 + status_dict.get(status, 0)
            except Exception:
                pass
            i += 1

            if i == 10:
                print_stats(total_file_size, status_dict)
                i = 0
        print_stats(total_file_size, status_dict)
    except KeyboardInterrupt:
        print_stats(total_file_size, status_dict)
        raise


main()
