# **Bài tập 9: Collaborative Filtering** ✅

## **1. Bản tiếng Anh**

**Task:** Consider the table of ratings below, which shows the ratings for three different books by five different readers. In this question, you want to figure out the rating of `Reader1` for `Book1` using item-item
and user-user collaborative filtering methods. Notice that some of the ratings are unknown.

| | Book1 | Book2 | Book3 |
|---|---|---|---|
| Reader1 | ? | 2.0 | 1.0 |
| Reader2 | 3.0 | 1.0 | |
| Reader3 | 1.0 | | |
| Reader4 | 2.0 | 1.0 | |
| Reader5 | 0.0 | | 3.0 |


**(a) Use the `user-user` collaborative filtering method and the cosine similarity measure to calculate the rating of `Reader1` for `Book1` based on the two most similar readers to `Reader1`. Show your steps and highlight your final rating. You do not need to subtract row mean to normalize the table.**

**(b) Use the `item-item` collaborative filtering method and the cosine similarity measure to calculate the rating of `Reader1` for `Book1` based on the most similar book to `Book1`. Show your steps and highlight your final rating. You do not need to subtract row mean to normalize the table.**

## **2. Bản tiếng Việt**

**Bài tập:** Xét bảng đánh giá dưới đây, bảng đánh giá bao gồm các đánh giá cho ba cuốn sách khác nhau bởi năm người đọc khác nhau. Trong câu hỏi này, bạn hãy xác định đánh giá của `Reader1` cho `Book1` bằng cách sử dụng phương pháp `user-user` và `item-item`. Lưu ý rằng có một số đánh giá không được xác định trong bảng (tức là những ô bị trống).

| | Book1 | Book2 | Book3 |
|---|---|---|---|
| Reader1 | ? | 2.0 | 1.0 |
| Reader2 | 3.0 | 1.0 | |
| Reader3 | 1.0 | | |
| Reader4 | 2.0 | 1.0 | |
| Reader5 | 0.0 | | 3.0 |

**Ngoài lề ✅: Nếu người ta có dặn trừ trung bình của mỗi hàng để chuẩn hóa bảng trước khi tính toán thì ta sẽ làm như sau:**

Công thức trung bình của một hàng là: $$ \bar{r_i} = \frac{r_{i1} + r_{i2} + ... + r_{in}}{n} $$

**Lưu ý:** Trong đó $r_{ij}$ là đánh giá của người đọc thứ $i$ cho cuốn sách thứ $j$. Và $n$ là số lượng cuốn sách `đã được đánh giá` (bỏ qua những ô bị trống).

Với hàng 1 ta có: $$ \bar{r_1} = \frac{2 + 1}{2} = 1.5 $$

Vậy hàng 1 sẽ được biến đổi thành: $$ r_1 = \{?, 2 - 1.5, 1 - 1.5\} = \{?, 0.5, -0.5\} $$

Tương tự với các hàng còn lại, ta có bảng đã được chuẩn hóa như sau:

| | Book1 | Book2 | Book3 |
|---|---|---|---|
| Reader1 | ? | 0.5 | -0.5 |
| Reader2 | 1.0 | -1.0 | |
| Reader3 | 1.0 | | |
| Reader4 | 0.5 | -0.5 | |
| Reader5 | -1.5 | | 1.5 |

**Ngoài lề ❌:** Nếu đề bài bắt tình độ tương đồng bằng công thức `Pearson` thì ta sẽ tính toán như sau:

Đầu tiên ta cần tính trung bình đánh giá của mỗi người đọc. Công thức trung bình đánh giá của một người đọc là:

$$ \bar{r_x} = \frac{r_{x1} + r_{x2} + ... + r_{xn}}{n} $$

$$ hoặc $$

$$ \bar{r_y} = \frac{r_{y1} + r_{y2} + ... + r_{yn}}{n} $$

Ta có công thức tính độ tương đồng `Pearson` giữa hai người đọc $x$ và $y$ như sau:

$$ sim(x, y) = \frac{\sum_{s \in S_{xy}} (r_{xs} - \bar{r}_x) \cdot (r_{ys} - \bar{r}_y)}{\sqrt{\sum_{s \in S_{xy}} (r_{xs} - \bar{r}_x)^2} \sqrt{\sum_{s \in S_{xy}} (r_{ys} - \bar{r}_y)^2}} $$

*Trong đó:*

- $S_{xy}$ là tập hợp các cuốn sách mà cả $x$ và $y$ đều đã đánh giá.
- $r_{xs}$ là đánh giá của người đọc $x$ cho cuốn sách $s$.
- $r_{ys}$ là đánh giá của người đọc $y$ cho cuốn sách $s$.
- $\bar{r}_x$ là trung bình đánh giá của người đọc $x$ trên các cuốn sách mà $x$ đã đánh giá.
- $\bar{r}_y$ là trung bình đánh giá của người đọc $y$ trên các cuốn sách mà $y$ đã đánh giá.

**(a) Sử dụng phương pháp `user-user` và phương pháp đo độ tương đồng `Cosine` để tính toán đánh giá của `Reader1` cho `Book1` dựa trên hai người đọc tương tự nhất với `Reader1`. Hãy cho biết các bước tính toán và đánh dấu đánh giá cuối cùng của bạn.** ✅

**Đáp án:**

Cho $r_x$ là một vector đánh giá của người đọc $x$ với $r_x = \{r_{x1}, r_{x2}, r_{x3}\}$. Trong đó $r_{xi}$ là đánh giá của người đọc $x$ cho cuốn sách thứ $i$. Vậy với từng người đọc $x$ ta có vector đánh giá $r_x$ như sau:

$$ r_1 = \{0, 2, 1\}; r_2 = \{3, 1, 0\}; r_3 = \{1, 0, 0\}; r_4 = \{2, 1, 0\}; r_5 = \{0, 0, 3\} $$

>>**Giải thích**: Với những đánh giá không xác định, ta có thể coi như là đánh giá bằng 0.

Ta có công thức tính độ tương đồng `Cosine` giữa hai nguời đọc $x$ và $y$ như sau:

$$ sim(x, y) = \cos(r_x, r_y) = \frac{r_x \cdot r_y}{\|r_x\| \|r_y\|} $$

*Trong đó:*

- $\cos(r_x, r_y)$ là độ tương đồng `Cosine` giữa hai vector đánh giá $r_x$ và $r_y$.
- $r_x \cdot r_y$ là tích vô hướng của hai vector đánh giá $r_x$ và $r_y$.
- $\|r_x\|$ là độ dài của vector đánh giá $r_x$.
- $\|r_y\|$ là độ dài của vector đánh giá $r_y$.

Với bài toán này, ta có thể tính độ tương đồng `Cosine` giữa `Reader1` và các người đọc khác như sau:

**✅ `Phương pháp Cosine`:** 

Với `Reader1` và `Reader2`: $$ sim(1, 2) = \cos(r_1, r_2) = \frac{r_1 \cdot r_2}{\|r_1\| \|r_2\|} = \frac{0 \times 3 + 2 \times 1 + 1 \times 0}{\sqrt{0^2 + 2^2 + 1^2} \sqrt{3^2 + 1^2 + 0^2}} = \frac{2}{\sqrt{5} \sqrt{10}} \approx 0.283 $$

*Tương tự với các cặp người đọc `Reader1` và `Reader3`, `Reader1` và `Reader4`, `Reader1` và `Reader5` ta có bảng tính toán độ tương đồng `Cosine` giữa `Reader1` và các người đọc khác như sau:*

| | Reader2 | Reader3 | Reader4 | Reader5 |
|---|---|---|---|---|
| $cos(r_1, r_i)$ | $0.283$ | $0$ | $0.4$ | $0.447$ |

---

**❌ `Phương pháp Pearson`:**

Trung bình đánh giá của các người đọc như sau:

$$ \bar{r}_1 = \frac{0 + 2 + 1}{3} = 1; \bar{r}_2 = \frac{3 + 1 + 0}{3} = 1.33; \bar{r}_3 = \frac{1 + 0 + 0}{3} = 0.33$$ 
$$ \bar{r}_4 = \frac{2 + 1 + 0}{3} = 1; \bar{r}_5 = \frac{0 + 0 + 3}{3} = 1 $$

Với `Reader1` và `Reader2`: 
$$ sim(1, 2) = \frac{\sum_{s \in S_{12}} (r_{1s} - \bar{r}_1) \cdot (r_{2s} - \bar{r}_2)}{\sqrt{\sum_{s \in S_{12}} (r_{1s} - \bar{r}_1)^2} \sqrt{\sum_{s \in S_{12}} (r_{2s} - \bar{r}_2)^2}} $$

$$ = \frac{(0 - 1) \cdot (3 - 1.33) + (2 - 1) \cdot (1 - 1.33) + (1 - 1) \cdot (0 - 1.33)}{\sqrt{(0 - 1)^2 + (2 - 1)^2 + (1 - 1)^2} \sqrt{(3 - 1.33)^2 + (1 - 1.33)^2 + (0 - 1.33)^2}} $$

$$ = \frac{-2}{\sqrt{2} \sqrt{4.67}} \approx -0.654 $$

*Tương tự với các cặp người đọc `Reader1` và `Reader3`, `Reader1` và `Reader4`, `Reader1` và `Reader5` ta có bảng tính toán độ tương đồng `Cosine` giữa `Reader1` và các người đọc khác như sau:*

| | Reader2 | Reader3 | Reader4 | Reader5 |
|---|---|---|---|---|
| $sim(1, i)$ | $-0.654$ | | | |

💭 **An nghĩ thầy sẽ không cho tính Pearson nếu ra bài này vì công thức quá nặng 🥀**

---

Vậy ta có thể thấy `Reader1` với `Reader4` và `Reader5` có độ tương đồng `Cosine` cao nhất. Vậy ta sẽ dự đoán đánh giá của `Reader1` cho `Book1` dựa trên đánh giá của `Reader4` và `Reader5`.

Ta có công thức tính đánh giá dự đoán của người đọc $x$ cho một cuốn sách $i$ như sau:

$$ r_{xi} = \frac{\sum_{y \in N} sim(x, y) \cdot r_{yi}}{\sum_{y \in N} sim(x, y)} $$

*Trong đó:*

- $N$ là tập hợp các người đọc tương tự với người đọc $x$. Ở ví dụ này, $N = \{4, 5\}$.
- $r_{yi}$ là đánh giá của người đọc $y$ cho cuốn sách thứ $i$. Ở ví dụ này, $r_{41} = 2$ và $r_{51} = 0$.
- $sim(x, y)$ là độ tương đồng Cosine giữa hai người đọc $x$ và $y$.

Với bài toán này, ta có thể tính đánh giá dự đoán của `Reader1` cho `Book1` như sau:

$$ r_{11} = \frac{\sum_{y \in N} sim(1, y) \cdot r_{yi}}{\sum_{y \in N} sim(1, y)} = \frac{sim(1, 4) \cdot r_{41} + sim(1, 5) \cdot r_{51}}{sim(1, 4) + sim(1, 5)} = \frac{0.4 \cdot 2 + 0.447 \cdot 0}{0.4 + 0.447} \approx 4.47 $$

**Kết luận**: Vậy ta có thể dự đoán đánh giá của `Reader1` cho `Book1` là $4.47$.

**(b) Sử dụng phương pháp `item-item` và phương pháp đo độ tương đồng `Cosine` để tính toán đánh giá của `Reader1` cho `Book1` dựa trên cuốn sách tương tự nhất với `Book1`. Hãy cho biết các bước tính toán và đánh dấu đánh giá cuối cùng của bạn.** ✅

**Đáp án:**

Cho $r_i$ là một vector đánh giá của cuốn sách $i$ với $r_i = \{r_{i1}, r_{i2}, r_{i3}, r_{i4}, r_{i5}\}$. Trong đó $r_{ij}$ là đánh giá của cuốn sách $i$ cho người đọc thứ $j$. Vậy với từng cuốn sách $i$ ta có vector đánh giá $r_i$ như sau:

$$ r_1 = \{0, 3, 1, 2, 0\}; r_2 = \{2, 1, 0, 1, 0\}; r_3 = \{1, 0, 0, 0, 3\} $$

Với bài toán này, ta tính độ tương đồng `Cosine` giữa `Book1` và các cuốn sách khác như sau:

Với `Book1` và `Book2`: $$ sim(1, 2) = \cos(r_1, r_2) = \frac{r_1 \cdot r_2}{\|r_1\| \|r_2\|} = \frac{0 \times 2 + 3 \times 1 + 1 \times 0 + 2 \times 1 + 0 \times 0}{\sqrt{0^2 + 3^2 + 1^2 + 2^2 + 0^2} \sqrt{2^2 + 1^2 + 0^2 + 1^2 + 0^2}} = \frac{5}{\sqrt{14} \sqrt{6}} \approx 0.546 $$

*Tương tự với cặp cuốn sách `Book1` và `Book3`, ta có $sim(1, 3) = 0$.*

Vậy ta có thể thấy `Book1` với `Book2` có độ tương đồng Cosine cao nhất. Vậy ta sẽ dự đoán đánh giá của `Reader1` cho `Book1` dựa trên đánh giá của tất cả các người đọc cho `Book2`.

Ta có công thức tính đánh giá dự đoán của người đọc $x$ cho một cuốn sách $i$ với phương pháp `item-item` như sau:

$$ r_{xi} = \frac{\sum_{j \in N(i;x)} sim(i, j) \cdot r_{xj}}{\sum_{j \in N(i;x)} sim(i, j)} $$

*Trong đó:*

- $N(i;x)$ là tập hợp các cuốn sách tương tự với cuốn sách $i$ mà người đọc $x$ đã đánh giá. Ở ví dụ này, người đọc `Reader1` đã đánh giá `Book2` nên $N(1;1) = \{2\}$.
- $r_{xj}$ là đánh giá của người đọc $x$ cho cuốn sách thứ $j$. Ở ví dụ này, $r_{21} = 1$.
- $sim(i, j)$ là độ tương đồng Cosine giữa hai cuốn sách $i$ và $j$.

Với bài toán này, ta có thể tính đánh giá dự đoán của `Reader1` cho `Book1` như sau:

$$ r_{11} = \frac{\sum_{j \in N(1;1)} sim(1, j) \cdot r_{xj}}{\sum_{j \in N(1;1)} sim(1, j)} = \frac{sim(1, 2) \cdot r_{21}}{sim(1, 2)} = \frac{0.546 \cdot 2.0}{0.546} = 2 $$
