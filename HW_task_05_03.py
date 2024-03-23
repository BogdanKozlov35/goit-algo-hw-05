import re
from pathlib import Path
from collections import defaultdict
import sys

#filter_logs_by_level(logs: list, level: str) -> list


def parse_log_line(line: str) -> dict:
    pattern = r'^(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (\w+) (.+)$'
    match = re.match(pattern, line)
    if match:
        return {"data": match.group(1), "time": match.group(2), "level": match.group(3), "message": match.group(4)}
    else:
        return None

def load_logs(path):
    logs = []
    with open(path, "r", encoding="UTF-8") as fh:
        for line in fh:
            log_info = parse_log_line(line)
            if log_info:
                logs.append(log_info)
    return logs

def count_logs_by_level(logs) -> dict:

    counts = defaultdict(int)
    for log in logs:
        counts[log["level"]] += 1
    return counts

def display_log_counts(counts: dict):
    line = "|{:^17}|{:^10}|".format("Рівень логування", "Кількість")
    separator = "_" * len(line)
    body = ""
    for key, val in counts.items():
        body += ("|{:<17}|{:<10}|\n".format(key, val))
    table = "\n".join([line, separator, body,])

    return table

def filter_logs_by_level(logs: list, level: str):
    return [f"{log ["data"]} {log["time"]} - {log["message"]}" for log in logs if log['level'] == level]

def main():

    #user_input = input("Enter path log file [example log.txt or log.txt ERROR] :")
    path = "log.txt" #sys.argv[1]
    logs = load_logs(path)
    counts = count_logs_by_level(logs)
    print(display_log_counts(counts))

    if len(sys.argv) > 0:
        level = "ERROR" #sys.argv[2]
        filtered_logs = filter_logs_by_level(logs, level)
        print("Filtered Logs for level:", level)
        for log in filtered_logs:
            print(log)

if __name__ == "__main__":
    main()
