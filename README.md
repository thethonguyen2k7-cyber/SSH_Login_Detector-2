
# AI Based SSH Login Attack Detector

## Project Overview

This project detects suspicious SSH login attacks by analyzing Linux authentication logs. It counts failed login attempts from each IP address and identifies potential brute-force attacks.

---

## Features

- Read Linux SSH authentication log
- Extract failed login attempts
- Count failed logins by IP address
- Detect suspicious IPs
- Export results to CSV
- Generate visualization chart

---

## Project Structure

```
SSH_Login_Detector
│
├── auth_log.txt          # Sample SSH log
├── collect_log.sh        # Shell script
├── main.py               # Main Python program
├── result.csv            # Analysis result
├── bieu_do_output.png    # Chart
├── requirements.txt
└── README.md
```

---

## Requirements

- Python 3.x
- matplotlib

Install dependency:

```bash
pip install -r requirements.txt
```

---

## Run Project

```bash
python main.py
```

---

## Output

The program will:

- Detect suspicious IP addresses
- Generate result.csv
- Generate bieu_do_output.png

---

## Sample Detection

| IP Address | Failed Login | Status |
|------------|-------------:|--------|
|203.0.113.5|4|Warning|
|198.51.100.12|1|Normal|

---

## Authors

Group 9

- Nguyễn Thế Thọ
- Lã Ngọc Ninh
- Vũ Hoàng Yến

Course: OSG203