# **Bài tập lớn - Homework 1 - CS246**

## **Thông tin lớp học phần:**

* **Tên lớp học phần:** Phân tích dữ liệu lớn
* **Mã lớp học phần:** DAT712_222_8_L14
* **Giảng viên:** Nguyễn Thanh Hiên

## **Thông tin nhóm 6:**
Gồm 3 thành viên:
| Họ và tên                     | MSSV          |
|-------------------------------|---------------|
| Trịnh Nguyễn Nhật An          | 050608200222  |
| Nguyễn Hữu Viết Ngọc          | 050608200489  |
| Võ Ngọc Khánh Vy              | 050608200791  |

## **Nội dung bài làm:**
Phần nộp báo cáo bao gồm 7 file chính sau:
* **README.md**: Giới thiệu bài làm
* **1_Spark.ipynb**: Bao gồm code và kết quả chạy code của *bài 1*
* **2_Asscociation Rules.ipynb**: Lời giải toán và kết quả chạy code của *bài 2*
* **3_Locality-Sensitive Hashing.ipynb**: Lời giải toán cho *bài 3*
* **4_LSH for Approximate Near Neighbor Search.ipynb**: Lời giải toán và kết quả chạy code của *bài 4*
* **lsh.py**: File chứa các hàm cần thiết để chạy code cho *bài 4*
* **Đề bài HW1.pdf**: Đề bài của bài tập này

## **Cấu trúc thư mục:**
```text
.
├── 1_Spark.ipynb
├── 2_Asscociation Rules.ipynb
├── 3_Locality-Sensitive Hashing.ipynb
├── 4_LSH for Approximate Near Neighbor Search.ipynb
├── README.md
├── lsh.py
└── Đề bài HW1.pdf
```

## **Cách chạy code:**
**Tất cả các file code đều được chạy trên Google Colab**

Một số lưu ý khi chạy code cho *bài 1* và *bài 4*:

### **Bài 1:**
Chạy cell đầu tiên để cài đặt thư viện pyspark, sau đó chạy các cell tiếp theo để chạy code
```python
# Setup
!pip install pyspark
!pip install -U -q PyDrive
!apt install openjdk-8-jdk-headless -qq

import os
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
```
**Lưu ý:** Về thời gian chạy thuật toán cho bài này có thể tùy thời điểm mà thời gian chạy sẽ khác nhau (từ 3-10 phút). Nếu thời gian chạy quá lâu, có thể restart lại runtime và chạy lại từ đầu.

### **Bài 4:**
Các đoạn code trong *bài 4* đa phần phần đều sử dụng các hàm trong file `lsh.py`. Do đó, khi chạy bài 4, cần sử dụng file `lsh.py` để có thể sử dụng được notebook này (tải file `lsh.py` về máy và upload lên Google Colab). Sau khi upload file lên Colab, chạy cell đầu tiên để import các thư viện cần thiết cho bài 4.
```python
from lsh import *
import time
from tabulate import tabulate
import matplotlib.pyplot as plt
```

**Lưu ý:** *Bài 4* sẽ sử dụng file `patches.csv` để chạy code. File này có kích thước khoảng 500MB, nên khi chạy bài 4, khuyến khích nên upload file `patches.csv` lên Google Drive và mount Google Drive vào Colab. Sau đó, chỉ cần chỉ định đường dẫn đến file `patches.csv` trong Google Drive là có thể chạy được bài 4.

**Nguồn đề bài và các tập dữ liệu được sử dụng trong bài làm:** [Homework 1 - CS246](http://web.stanford.edu/class/cs246/homework/hw1-bundle.zip )




