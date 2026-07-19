
#!/bin/bash

# Thu thập các dòng đăng nhập SSH thất bại
grep "Failed password" auth_log.txt > failed_log.txt

echo "Đã tạo file failed_log.txt"
