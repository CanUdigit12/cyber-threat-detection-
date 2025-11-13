import csv
import random

geo_locations = ["UK", "US", "RU", "CN", "DE", "IN", "POL", "FR"]
login_methods = ["Web", "Ssh", "api", "Vpn", "Rdp"]
ip_prefixes = ["192.168", "10.0", "172.16", "203.0", "8.8"]

def random_time():
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    return f"{hour:02d}:{minute:02d}"

def generate_rows(n=1000):
    rows = []
    for _ in range(n):
        failed_attempts = random.randint(0, 20)
        ip = f"{random.choice(ip_prefixes)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
        login_time = random_time()
        geo = random.choice(geo_locations)
        method = random.choice(login_methods)

        hour = int(login_time.split(":")[0])
        is_threat = int(
            failed_attempts > 10 or
            geo in ["RU", "CN"] or
            hour < 6 or hour > 22
        )

        rows.append([failed_attempts, ip, login_time, geo, method, is_threat])
    return rows

with open("data/login_logs.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["failed_attempts", "ip_address", "login_time", "geo", "login_method", "is_threat"])
    writer.writerows(generate_rows())