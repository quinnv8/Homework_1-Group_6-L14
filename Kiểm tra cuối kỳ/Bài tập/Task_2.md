# **Bài tập 2: Map Reduce**

## **1. Bản English**

**Task:**  Given two sets: $R = \{a, b, c\}$ and $S = \{b, e, f\}$. The task is to find the difference of $R \setminus S$, i.e., the set of elements that are present in $R$ but not in $S$. Design `Map`, `Group by Key` and `Reduce` functions to compute the difference, and write the answer in the form of $a, b, c, e, f, R, S$.

(a) What does the `Map` function produce for the sets $R, S$?

**Answer:** $\{(a, R), (b, R), (c, R), (b, S), (e, S), (f, S)\}$.

>>**Explanation:** The `Map` function produces a set of `(key, value)` pairs, where `key` is an element of the set, and `value` is the name of the set that contains the element.

(b) What does the `Group by Key` function produce?

**Answer:** $\{(a, [R]), (b, [R, S]), (c, [R]), (e, [S]), (f, [S])\}$.

>>**Explanation:** The `Group by Key` function groups together `(key, value)` pairs that have the same `key` into a single `(key, [value1, value2, ...])` pair.

(c) What does the `Reduce` function produce for the set $R \setminus S$?

**Answer:** $\{a, c\}$.

>>**Explanation:** The `Reduce` function removes `(key, value)` pairs that have `value` containing `S` and keeps only `(key, value)` pairs that have `value` containing only `R`. In this case, we only need to keep the `(a, [R])` and `(c, [R])` pairs.

## **2. Bản tiếng Việt**
**Bài tập:** Cho hai tập hợp $R = \{a, b, c\}$ và $S = \{b, e, f\}$. Yêu cầu tìm tập hợp $R \setminus S$, tức là tập hợp các phần tử chỉ có trong $R$ mà không có trong $S$. Thiết kế hàm `Map`, `Group by Key` và `Reduce` để tính toán tập hợp này, và viết kết quả dưới dạng $a, b, c, e, f, R, S$.

(a) Đối với tập hợp $R, S$ thì hàm `Map` sẽ tạo ra những gì?

**Đáp án:** $\{(a, R), (b, R), (c, R), (b, S), (e, S), (f, S)\}$.

>>**Giải thích:** Hàm `Map` sẽ tạo ra một tập hợp các cặp `(key, value)` với `key` là phần tử thuộc tập hợp, và `value` là tên tập hợp chứa phần tử đó. 

(b) Hàm `Group by Key` sẽ tạo ra gì?

**Đáp án:** $\{(a, [R]), (b, [R, S]), (c, [R]), (e, [S]), (f, [S])\}$.

>>**Giải thích:** Hàm `Group by Key` sẽ gom lại các cặp `(key, value)` có cùng `key` giống nhau thành một cặp `(key, [value1, value2, ...])`. 

(c) Hàm `Reduce` sẽ tạo ra gì cho tập hợp $R \setminus S$?

**Đáp án:** $\{a, c\}$.

>>**Giải thích:** Hàm `Reduce` sẽ loại bỏ các cặp `(key, value)` có `value` chứa `S` và chỉ giữ lại các cặp `(key, value)` có `value` chứa duy nhất `R`. Ở đây, ta chỉ cần giữ lại cặp `(a, [R])` và `(c, [R])`.