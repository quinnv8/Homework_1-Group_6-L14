# **Bài tập 6: Clustering** ✅

## **1. Bản tiếng Anh**

**Task:** 

**(a) In this question, you will perform a simple `K-means` calculation.**

|Points| x | y |
|---|---|---|
|1|1.0|1.0|
|2|1.5|2.0|
|3|3.0|4.0|
|4|5.0|7.0|
|5|3.5|5.0|
|6|4.5|5.0|
|7|3.5|4.5|

If we set $k = 2$, the initial centroids be $P_1$ and $P_4$, and we are using `Euclidean distance`, what are the final outputs of `K-means`?

|Centroids| coordinates members |
|---|---|
|? | ? |

**(b) True/False question about `K-means`. If we use `Euclidean distance`, the cost over iterations always decreases:__________**

**(c) Explain two different types of 2-dimensional data distributions where `K-means` might fail to produce accurate clusters. Provide sketches of the data in the 2D `Euclidean` space, and briefly explain.**

## **2. Bản tiếng Việt**

**Bài tập:**

**(a) Trong câu hỏi này, bạn sẽ thực hiện một phép tính `K-means` đơn giản.** ✅

|Points| x | y |
|---|---|---|
|1|1.0|1.0|
|2|1.5|2.0|
|3|3.0|4.0|
|4|5.0|7.0|
|5|3.5|5.0|
|6|4.5|5.0|
|7|3.5|4.5|

Nếu chúng ta đặt $k = 2$, các điểm trung tâm ban đầu là $P_1$ và $P_4$, và chúng ta đang sử dụng khoảng cách `Euclidean`, thì kết quả cuối cùng của `K-means` là gì?

|Centroids| coordinates members |
|---|---|
|? | ? |

**Đáp án:**

Ta có công thức tính khoảng cách `Euclidean` giữa hai điểm $P_i(x_i, y_i)$ và $P_j(x_j, y_j)$ như sau:

$$d(P_i, P_j) = \sqrt{(x_i - x_j)^2 + (y_i - y_j)^2}$$

***Vòng lặp đầu tiên:***

Với điểm trung tâm $P_1=(1.0, 1.0)$ và $P_4=(5.0, 7.0)$, ta có khoảng cách giữa các điểm còn lại với các điểm trung tâm như sau:

|Points| $d(P_1, P_i)$ | $d(P_4, P_i)$ |
|---|---|---|
|2|1.118|6.103|
|3|3.606|3.606|
|5|4.717|2.5|
|6|5.315|2.062|
|7|4.301|2.915|

Ta thấy rằng, điểm $P_2$ có khoảng cách nhỏ nhất với $P_1$, và các điểm $P_5$, $P_6$ và $P_7$ có khoảng cách nhỏ nhất với $P_4$; và điểm $P_3$ có khoảng cách bằng nhau với cả hai điểm trung tâm, nên ta sẽ gán điểm $P_3$ vào cụm thứ 2.

|Centroids| coordinates members |
|---|---|
|$C_1$ | $P_1$, $P_2$|
|$C_2$ | $P_3$, $P_4$, $P_5$, $P_6$, $P_7$|

*Tính lại các điểm trung tâm:*

Ta tính lại các điểm trung tâm của các cụm như sau:

$$X_{C_1} = \frac{1.0 + 1.5}{2} = 1.25$$

$$Y_{C_1} = \frac{1.0 + 2.0}{2} = 1.5$$

$$X_{C_2} = \frac{3.0 + 5.0 + 3.5 + 4.5 + 3.5}{5} = 3.9$$

$$Y_{C_2} = \frac{4.0 + 7.0 + 5.0 + 5.0 + 4.5}{5} = 5.3$$

Vậy, các điểm trung tâm mới là:

$$C_1 = (1.25, 1.5)$$

$$C_2 = (3.9, 5.3)$$

***Vòng lặp thứ hai:***

Với các điểm trung tâm mới, ta có khoảng cách giữa các điểm còn lại với các điểm trung tâm như sau:

|Points| $d(C_1, P_i)$ | $d(C_2, P_i)$ |
|---|---|---|
|1|0.559|5.187|
|2|0.559|4.080|
|3|3.052|1.581|
|4|6.657|2.025|
|5|4.161|0.500|
|6|4.776|0.671|
|7|3.750|0.894|

Ta thấy rằng, điểm $P_1$, $P_2$ có khoảng cách nhỏ nhất với $Centroid_1$, và các điểm $P_3$, $P_4$, $P_5$, $P_6$ và $P_7$ có khoảng cách nhỏ nhất với $C_2$. Vậy, ta sẽ gán các điểm này vào các cụm tương ứng.

|Centroids| coordinates members |
|---|---|
|$C_1$ | $P_1$, $P_2$|
|$C_2$ | $P_3$, $P_4$, $P_5$, $P_6$, $P_7$|

Ta nhận thấy rằng, các điểm trung tâm mới không thay đổi so với các điểm trung tâm cũ, nên thuật toán `K-means` đã kết thúc.

$ \rightarrow $ Kết quả cuối cùng của `K-means` là:

|Centroids| coordinates members |
|---|---|
|$C_1$ | $P_1$, $P_2$|
|$C_2$ | $P_3$, $P_4$, $P_5$, $P_6$, $P_7$|

**(b) Câu hỏi đúng/sai về `K-means`. Nếu chúng ta sử dụng khoảng cách `Euclidean`, chi phí qua các lần lặp luôn giảm dần:__________** ✅

**Đáp án:** Đúng

**Giải thích:** Ta có hàm chi phí của `K-means` như sau:

$$J = \sum_{i=1}^{n} ||x_i - \mu_{c_i}||^2$$

Trong đó, $x_i$ là điểm dữ liệu thứ $i$, $\mu_{c_i}$ là điểm trung tâm của cụm $c_i$, và $n$ là tổng số điểm dữ liệu.

Mục tiêu của `K-means` là tối thiểu hóa hàm chi phí $J$. Với mỗi lần lặp, ta sẽ tìm được các điểm trung tâm mới, và hàm chi phí sẽ giảm dần. Vì vậy, chi phí qua các lần lặp luôn giảm dần.

~~**(c) Giải thích hai loại phân bố dữ liệu hai chiều khác nhau mà `K-means` có thể không thể tạo ra các cụm chính xác. Cung cấp một số minh họa của dữ liệu trong không gian hai chiều `Euclidean`, và giải thích ngắn gọn.**~~ ❌

**Đáp án:** `K-means` không thể tạo ra các cụm chính xác khi dữ liệu có 2 dạng như sau:

![](https://s3-ap-south-1.amazonaws.com/av-blog-media/wp-content/uploads/2017/02/05114142/q16sol.png)

**1. Dạng hình xoắn:**

Trong ví dụ như trên, `K-means` sẽ không thể tạo ra các cụm chính xác vì không có sự phân chia rõ ràng giữa các cụm và mật độ thấp giữa các cụm sẽ khiến cho việc phân loại các điểm dữ liệu trở nên khó khăn.

**2. Dạng dữ liệu có nhiều cụm với mật độ khác nhau:**

Trong ví dụ trên, mặc dù cụm dữ liệu lớn màu đỏ khi nhìn chung có vẻ sẽ được phân loại tốt, nhưng nếu xét kĩ hơn thì cụm dữ liệu lớn này lại bao gồm 2 cụm nhỏ với mỗi cụm có mật độ dày đặc khiến cho cụm dữ liệu lớn này lại bị thuật toán `K-means` phân loại không chính xác thành 2 cụm nhỏ.



