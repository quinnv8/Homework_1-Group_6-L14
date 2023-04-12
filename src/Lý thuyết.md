# **Lý thuyết môn Big Data**
## **1. Map Reduce**
### **1.1. Map Reduce là gì?** ✅
`MapReduce` là một mô hình lập trình phân tán được phát triển bởi Google để xử lý và phân tích các tập dữ liệu lớn. Mô hình này bao gồm hai pha chính: `Map` và `Reduce`.

* **Map:** trong pha này, dữ liệu được chia thành các cặp (key, value) và được xử lý bởi các `mapper` trên các `node` khác nhau trong mạng phân tán. Các `mapper` sẽ trích xuất thông tin từ các cặp `(key, value)` và tạo ra các cặp mới `(key, value)` để gửi đến pha `Reduce`.

* **Reduce:** trong pha này, các cặp `(key, value)` được tổng hợp và xử lý bởi các `reducer` trên các `node` khác nhau trong mạng phân tán. Các `reducer` sẽ nhận các cặp `(key, value)` từ pha `Map` và tập hợp chúng lại thành các cặp mới `(key, value)` với các giá trị được tính toán dựa trên nhiều cặp dữ liệu đầu vào.

Mô hình `MapReduce` có nhiều ứng dụng thực tế, như ứng dụng vào tính toán phân tán và song song.

## **2. Itemsets Mining - Association Rule**
### **2.1. Itemsets Mining là gì?** ✅
`Itemsets mining` là quá trình khai thác dữ liệu để tìm kiếm tập các mặt hàng hay mẫu xuất hiện cùng nhau trong tập dữ liệu. Nó là một phần quan trọng của khai thác luật kết hợp trong dữ liệu và được sử dụng rộng rãi trong các ứng dụng thương mại điện tử, marketing và phân tích dữ liệu để tìm kiếm các kết hợp sản phẩm hay dịch vụ phổ biến và kết hợp đó để đưa ra các quyết định kinh doanh hiệu quả.

### **2.2. Association Rule là gì?** ✅
`Association rule` là luật kết hợp được sử dụng để mô tả sự tương quan giữa các mặt hàng trong một tập dữ liệu. Các luật kết hợp được tạo ra từ các itemsets phổ biến.

### **2.3. Các thuật toán phổ biến trong Itemsets Mining** ✅
Có nhiều thuật toán được sử dụng để khai thác các luật kết hợp trong dữ liệu như `Apriori`, `FP-Growth`.

### **2.5. Một số chỉ số đo lường** ✅

* **Support ✅: (được ký hiệu là S(A))** Support được định nghĩa là xác suất xuất hiện của A trong giỏ hàng:

$$ S(A) = Support(A) = Pr(A) $$

* **Confidence ✅: (được ký hiệu là conf(A → B))** Confidence được định nghĩa là xác suất xuất hiện của B trong giỏ hàng nếu giỏ hàng đã chứa A:

$$ conf(A → B) = Pr(B|A) = \frac{Support(A \cup B)}{Support(A)} $$

## **3. Locality Sensitive Hashing**
### **3.1. LSH là gì?** ✅
`Local Sensitive Hashing (LSH)` là một kỹ thuật được sử dụng trong khai thác dữ liệu để tìm kiếm các đối tượng tương tự trong các tập dữ liệu lớn.

Tuy nhiên, `LSH` cũng có một số hạn chế, bao gồm độ chính xác thấp và khó khăn trong việc tìm ra tham số phù hợp cho hàm băm.

## **4. K-Means Clustering**
### **4.1. Clustering là gì?** ✅
`Clustering` là một kỹ thuật trong khai thác dữ liệu được sử dụng để phân loại các đối tượng vào các nhóm tương đồng dựa trên các đặc trưng của chúng. 

Mục đích của `Clustering` là tìm ra cấu trúc ẩn của các tập dữ liệu, giúp phát hiện ra các mẫu, nhóm tương đồng và xu hướng tồn tại trong dữ liệu.

### **4.3. Ứng dụng của Clustering** ✅
Thuật toán này có thể được sử dụng để phân loại các đối tượng vào các nhóm tương đồng trong nhiều ứng dụng như xử lý hình ảnh, phân tích văn bản, phân loại khách hàng và phát hiện gian lận.

## **5. Dimensionality Reduction**
### **5.1. Dimensionality Reduction là gì?** ✅
`Dimensionality Reduction` là một kỹ thuật trong khai thác dữ liệu, được sử dụng để giảm số chiều của dữ liệu trong khi giữ nguyên các thông tin quan trọng. Nó giúp giảm kích thước của tập dữ liệu để giảm chi phí tính toán và lưu trữ, cải thiện khả năng phân loại và giảm thiểu các vấn đề như overfitting.

### **5.2. Ý nghĩa của trị riêng và vector riêng** ✅
`Trị riêng` là một số vô hướng đại diện cho mức độ thay đổi của một ma trận khi được áp dụng trên một vector. Nó được tính bằng cách giải phương trình $det(A-λI) = 0$, trong đó $A$ là ma trận vuông, $λ$ là trị riêng và $I$ là ma trận đơn vị. Trị riêng được sử dụng để phân tích cấu trúc của một ma trận và có thể được sử dụng để giảm số chiều của dữ liệu.

`Vector riêng` là một vector đại diện cho một hướng không thay đổi khi ma trận được áp dụng lên nó. Nó là một vector khác không của ma trận $A$, thỏa mãn phương trình $Av = λv$, trong đó $v$ là vector riêng và $λ$ là trị riêng tương ứng. 

`Trị riêng` và `vector riêng` có thể được sử dụng để phân tích cấu trúc của một ma trận và giảm số chiều của dữ liệu.

### **5.3. Phương pháp SVD (Singular Value Decomposition)** ✅
`Phương pháp SVD` phân tích một ma trận thành các thành phần riêng biệt để giảm số chiều của dữ liệu. Kết quả phân tích `SVD` là ba ma trận $U$, $S$, và $V$, trong đó ma trận $S$ là một ma trận đường chéo với các giá trị đường chéo gọi là `singular values`. Các giá trị này đại diện cho sự quan trọng của các thành phần trong dữ liệu và cho phép chọn một số lượng dữ liệu quan trọng nhất để giảm số chiều.

### **5.4. Phương pháp PCA (Principal Component Analysis)** ✅
`PCA` là một phương pháp giảm chiều dữ liệu, được sử dụng để giảm số chiều của dữ liệu bằng cách chọn các thành phần chính quan trọng nhất. `PCA` xác định các thành phần chính bằng cách phân tích các `trị riêng` và `vector riêng` của `ma trận hiệp phương sai` của dữ liệu. Các thành phần chính này được sắp xếp theo thứ tự ưu tiên của sự giải thích phương sai của dữ liệu. PCA thường được sử dụng trong các ứng dụng như phân tích dữ liệu và trực quan hóa dữ liệu.

## **6. Recommender System**
### **6.1. Recommender System là gì?** ✅
`Recommender System (Hệ thống gợi ý)` là một công nghệ được sử dụng rộng rãi trong lĩnh vực khai thác dữ liệu để giúp người dùng tìm kiếm và lựa chọn các sản phẩm, dịch vụ hoặc nội dung phù hợp với sở thích và nhu cầu của họ.

### **6.2. Các loại Recommender System** ✅
`Recommender System` có thể được phân loại thành 3 loại chính:

- `Content-based Recommender System`: phương pháp này đánh giá nội dung của sản phẩm và đưa ra các gợi ý sản phẩm tương tự. Phương pháp này phụ thuộc vào việc xây dựng các đặc trưng của sản phẩm.

- `Collaborative Filtering`: phương pháp này dựa trên lịch sử sử dụng của người dùng và tính tương đồng giữa các người dùng để đưa ra các gợi ý sản phẩm. Phương pháp này có thể được chia thành hai loại: `user-based collaborative filtering` và `item-based collaborative filtering`.

- `Hybrid Methods`: phương pháp này kết hợp cả `Content-based Recommender System` và `Collaborative Filtering Recommender System` để tạo ra các gợi ý sản phẩm.

## **7. Mining Data Streams**
### **7.1. Mining Data Streams là gì?** ✅
`Mining DataStreams (Khai thác dữ liệu luồng)` là một kỹ thuật trong khai thác dữ liệu được sử dụng để xử lý các luồng dữ liệu đến liên tục. Khác với khai thác dữ liệu thông thường, trong đó dữ liệu được lưu trữ trong cơ sở dữ liệu hoặc tập tin, dữ liệu trong `Mining DataStreams` được xử lý ngay khi chúng đang truyền qua.

`Mining DataStreams` đòi hỏi các giải thuật phải có tính tương tác với dữ liệu đầu vào để thích nghi với các thay đổi liên tục của dữ liệu. Vì vậy, các giải thuật phải đáp ứng các yêu cầu về thời gian và bộ nhớ.

### **7.2. Ứng dụng của Mining Data Streams** ✅
`Mining DataStreams` được sử dụng rộng rãi trong các lĩnh vực như theo dõi máy móc, quản lý mạng, tài chính và bảo mật. Các ứng dụng của nó là đa dạng và có thể cải thiện đáng kể hiệu quả của các hệ thống quản lý dữ liệu thời gian thực.

## **8. Computational Advertising**
### **8.1. Computational Advertising là gì?** ✅
`Computational Advertising (Quảng cáo tính toán)` là một lĩnh vực trong khoa học máy tính và quảng cáo kỹ thuật số, trong đó các giải thuật và công nghệ được sử dụng để tối ưu hóa hiệu quả của các chiến dịch quảng cáo trực tuyến.

Trong `Computational Advertising`, dữ liệu được sử dụng để xác định nhóm khách hàng tiềm năng và cách tương tác của họ với quảng cáo. Các giải thuật như `Machine Learning` và `Data Mining` được sử dụng để phân tích dữ liệu và tạo ra các mô hình dự đoán.

`Computational Advertising` giúp cải thiện hiệu quả quảng cáo, tăng khả năng tương tác của người dùng và cải thiện doanh số bán hàng của doanh nghiệp. Tuy nhiên, nó cũng đặt ra một số thách thức như đảm bảo tính riêng tư và bảo mật của người dùng và đảm bảo tính công bằng và độ tin cậy của quảng cáo.

