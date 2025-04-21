1. Ghi đè (`Override`)
- Là gì?
Ghi đè là khi lớp con định nghĩa lại một phương thức đã có ở lớp cha.

- Dùng khi nào?
Khi bạn muốn thay đổi hành vi của phương thức kế thừa từ lớp cha.

**@abstractmethod** là trường hợp đặc biệt của ghi đè:
➜ Khi lớp cha khai báo phương thức trừu tượng (@abstractmethod), thì lớp con `bắt buộc phải override` (ghi đè) phương thức đó để triển khai.


2. Nạp chồng (`Overload`)
- Là gì?
Nạp chồng là khi nhiều phương thức cùng tên nhưng khác tham số được định nghĩa trong cùng một lớp.

- Trong Python:
Không hỗ trợ overload kiểu truyền thống như Java hay C++, nhưng bạn có thể giả lập bằng:

- - Gán giá trị mặc định cho tham số
- - Dùng *args, **kwargs