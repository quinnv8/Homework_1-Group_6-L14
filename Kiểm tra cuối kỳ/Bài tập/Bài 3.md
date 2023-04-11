# **Bài tập 3: Frequent Item Set Mining**

## **1. Bản tiếng Anh**

**Task:** In this problem we focus on the frequent item set mining part. As a toy example, assume the whole item set is $\{banana, apple, basket, friend, atmosphere, learning\}$. The transaction database is as follows:

|Sentence index|words in the sentence and S|
|:-:|:-:|
|1|banana, apple, basket|
|2|basket, learning|
|3|apple, friend, learning|
|4|basket, friend, atmosphere|
|5|banana, friend, atmosphere, learning|
|6|basket, friend, atmosphere|

**Consider support threshold $s = 3$ in this case. Apply the `A-priori` algorithm to find the frequent item sets.**

**(a) Find the frequent items: $L_1 = $ $\{$ __________ $\}$**

**(b) Then, construct the candidate pairs using items in L1. The set of candidate pairs is: $C_2 = $ $\{$ __________ $\}$**

**(c) Filter on C2 to obtain frequent item tuples: $L_2 = $ $\{$ __________ $\}$**

**(d) Now suppose instead of `A-priori`, you are using the `PCY` algorithm to further optimize the process. During the first pass, you also hash each pair of items into a bucket, and maintain the count of pairs for each bucket. For $a$ bucket $b$ with count $c$, what can you say about the pairs that hash to $b$ if $c ≥ s$? (Possible answers: They must be frequent, they cannot be frequent, or not sure.)**

## **2. Bản tiếng Việt**

**Bài tập:** Trong bài tập này, chúng ta sẽ tập trung vào phần tìm kiếm tập mục phổ biến. Ví dụ, giả sử cho một tập các mặt hàng là $\{banana, apple, basket, friend, atmosphere, learning\}$. Chúng ta có các giao dịch như sau:

|Số thứ tự|Các vật phẩm trong từng giao dịch|
|:-:|:-:|
|1|banana, apple, basket|
|2|basket, learning|
|3|apple, friend, learning|
|4|basket, friend, atmosphere|
|5|banana, friend, atmosphere, learning|
|6|basket, friend, atmosphere|

**Giả sử ngưỡng hỗ trợ là $s = 3$. Áp dụng thuật toán `A-priori` để tìm các tập mục phổ biến.**

**(a) Tìm các mục phổ biến: $L_1 = $ $\{$ __________ $\}$** ✅

**Đáp án:**

Với ngưỡng hỗ trợ là 3, ta có bảng đếm số lần xuất hiện $C_1$ như sau:

|Item|Count|
|:-:|:-:|
|$banana$|2|
|$apple$|2|
|$basket$|4|
|$friend$|4|
|$atmosphere$|3|
|$learning$|3|

>> $\rightarrow L_1 = \{basket, friend, atmosphere, learning\}$


**(b) Sau đó, xây dựng các cặp ứng viên từ các mục trong L1. Tập các cặp ứng viên là: $C_2 = $ $\{$ __________ $\}$** ✅

**Đáp án:**

Ta có bảng đếm số lần xuất hiện $C_2$ như sau:

|Item|Count|
|:-:|:-:|
|$\{basket, friend\}$|2|
|$\{basket, atmosphere\}$|1|
|$\{basket, learning\}$|1|
|$\{friend, atmosphere\}$|3|
|$\{friend, learning\}$|2|
|$\{atmosphere, learning\}$|1|

>> $\rightarrow C_2 = \{\{basket, friend\}, \{basket, atmosphere\}, \{basket, learning\}, \{friend, atmosphere\}, \{friend, learning\}, \{atmosphere, learning\}\}$

**(c) Lọc trên C2 để tìm các tập mục phổ biến: $L_2 = $ $\{$ __________ $\}$** ✅

**Đáp án:**

>> $\rightarrow L_2 = \{\{friend, atmosphere\}\}$

~~**(d) Giả sử thay vì `A-priori`, chúng ta sử dụng thuật toán `PCY` để tối ưu hóa quá trình. Trong lần duyệt đầu tiên, chúng ta cũng băm mỗi tập mục vào một bucket, và duy trì số lần xuất hiện của các tập mục trong mỗi bucket. Với một bucket $b$ với số lần xuất hiện là $c$, chúng ta có thể nói gì về các tập mục băm vào $b$ nếu $c ≥ s$? (Các câu trả lời có thể là: Chúng phải là các tập mục phổ biến, chúng không thể là các tập mục phổ biến, hoặc không chắc chắn.)**~~ ❌

**Đáp án:** Không chắc chắn.

>>**Giải thích:** Với thuật toán `PCY`, chúng ta sẽ không đếm số lần xuất hiện của từng mục đơn lẻ, mà chúng ta sẽ đếm số lần xuất hiện của các cặp mục. Mỗi cặp mục sẽ được băm vào một bucket tương ứng. Mỗi lần một cặp mục được băm vào một bucket $b$ tương ứng, thì chúng ta sẽ tăng mức độ phổ biến (frequent count) của bucket $b$ đó lên `1` đơn vị. Sau khi kết thúc lần duyệt đầu tiên, chúng ta sẽ có một số bucket $b$ có mức độ phổ biến lớn hơn hoặc bằng ngưỡng hỗ trợ $s$. Tuy nhiên, chúng ta không thể nói rằng các cặp mục băm vào bucket $b$ đó phải là các tập mục phổ biến. Ví dụ, giả sử chúng ta có một bucket $b$ có mức độ phổ biến $s=3$. Chúng ta có thể có các cặp mục băm vào bucket $b$ như sau: 

>>$\{banana, apple\}$, $\{banana, apple\}$, $\{apple, basket\}$

>>Với các cặp mục trên, chúng ta không thể nói rằng chúng là các tập mục phổ biến vì chúng không đủ số lần xuất hiện để đạt ngưỡng hỗ trợ $s = 3$. Tuy nhiên, với các bucket $b$ không thỏa mãn điều kiện $c ≥ s$, chúng ta có thể kết luận rằng các cặp mục băm vào bucket $b$ không phải là các tập mục phổ biến.





