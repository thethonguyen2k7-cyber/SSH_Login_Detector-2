
import re
import csv
from collections import Counter
import matplotlib.pyplot as plt

LOG_FILE = "auth_log.txt"
CSV_FILE = "result.csv"
IMAGE_FILE = "bieu_do_output.png"

# -------------------------
# Đọc file log và lấy IP đăng nhập thất bại
# -------------------------
def doc_log():
    failed_ips = []

    regex = r"Failed password.*from ([0-9.]+)"

    with open(LOG_FILE, "r", encoding="utf-8") as file:
        for line in file:
            match = re.search(regex, line)
            if match:
                failed_ips.append(match.group(1))

    return failed_ips


# -------------------------
# Phân tích dữ liệu
# -------------------------
def phan_tich(ip_list):

    counter = Counter(ip_list)

    print("\n========== KẾT QUẢ ==========\n")

    for ip, count in counter.items():

        if count >= 3:
            print(f"{ip} : {count} lần -> CẢNH BÁO")
        else:
            print(f"{ip} : {count} lần -> Bình thường")

    return counter


# -------------------------
# Xuất CSV
# -------------------------
def xuat_csv(counter):

    with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow(["IP Address", "Failed Login"])

        for ip, count in counter.items():
            writer.writerow([ip, count])

    print("\nĐã tạo file result.csv")


# -------------------------
# Vẽ biểu đồ
# -------------------------
def ve_bieu_do(counter):

    ips = list(counter.keys())
    values = list(counter.values())

    plt.figure(figsize=(9,5))

    bars = plt.bar(
        ips,
        values,
        color="orange",
        edgecolor="black",
        label="Failed Login"
    )

    plt.axhline(
        y=3,
        color="red",
        linestyle="--",
        linewidth=2,
        label="Warning Threshold (>=3)"
    )

    plt.title(
        "AI Based SSH Login Attack Detector",
        fontsize=15,
        fontweight="bold"
    )

    plt.xlabel("Source IP Address")
    plt.ylabel("Number of Failed Login")

    plt.grid(axis="y", linestyle=":")

    plt.legend()

    for bar in bars:
        y = bar.get_height()
        plt.text(
            bar.get_x()+bar.get_width()/2,
            y+0.05,
            str(int(y)),
            ha="center",
            fontsize=11,
            fontweight="bold"
        )

    plt.savefig(IMAGE_FILE, dpi=300)

    print("Đã tạo biểu đồ:", IMAGE_FILE)

    plt.show()
    # -------------------------
# Main
# -------------------------

def main():

    print("AI based SSH Login Attack Detector")

    ip_list = doc_log()

    counter = phan_tich(ip_list)

    xuat_csv(counter)

    ve_bieu_do(counter)


if __name__ == "__main__":
    main()