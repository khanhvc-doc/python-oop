Python OOP Project - Quản lý Sinh viên & Nhân viên

📌 Mục tiêu

Xây dựng hệ thống Python áp dụng Lập trình Hướng Đối Tượng (OOP) từ cơ bản đến nâng cao, thông qua việc quản lý Sinh viên và Nhân viên.

Hệ thống chia thành 8 bài, mỗi bài phát triển theo mô hình kế thừa, trừu tượng, nạp chồng phương thức, CRUD và dễ mở rộng sau này.

📚 Danh sách các bài học

🔹 Bài 1 – ConNguoi

Lớp cha gốc cho toàn hệ thống.

Thuộc tính: ho_ten, tuoi, gioi_tinh

Phương thức:

__init__(): Phương thức khởi tạo để tạo một đối tượng của lớp.

__str__(): Phương thức trả về chuỗi biểu diễn của đối tượng.

hien_thi_thong_tin(): Hiển thị thông tin cơ bản về đối tượng.

🔹 Bài 2 – SinhVien (Lớp trừu tượng)

Kế thừa ConNguoi

Thuộc tính: ma_sinh_vien

Phương thức trừu tượng: get_diem(), xep_loai()

🔹 Bài 3 – SinhVienIT

Kế thừa SinhVien

Thuộc tính: diem_A, diem_B, diem_C

Tính điểm: 40%A + 35%B + 25%C

Xếp loại: Giỏi ≥ 8.0, Khá ≥ 7.0, TB ≥ 5.0, Yếu < 5.0

🔹 Bài 4 – SinhVienKD

Kế thừa SinhVien

Thuộc tính: diem_X, diem_Y, diem_Z

Tính điểm: 20%X + 30%Y + 50%Z

Xếp loại: Giỏi ≥ 8.5, Khá ≥ 7.5, TB ≥ 6.0, Yếu < 6.0

🔹 Bài 5 – NhanVien (Lớp trừu tượng)

Kế thừa ConNguoi

Thuộc tính: ma_nhan_vien, luong_co_ban

Phương thức trừu tượng:

get_thu_nhap()

get_thue()

get_bao_hiem()

get_phuc_loi()

get_thuc_lanh()  ➔ Thực lãnh = thu nhập - thuế - bảo hiểm + phúc lợi

⚠️ Việc triển khai interface giúp đảm bảo mỗi loại nhân viên phải định nghĩa cụ thể cách tính toán thu nhập, thuế, bảo hiểm và phúc lợi, từ đó giúp hệ thống dễ mở rộng, đảm bảo tính đóng gói và rõ ràng trong thiết kế.

🔹 Bài 6 – NhanVienHR

Thu nhập: = lương cơ bản

Thuế: 10%, Bảo hiểm: 8%, Phúc lợi: 500k

Thực lãnh: theo công thức chung

🔹 Bài 7 – NhanVienSales

Thuộc tính: doanh_so, hoa_hong

Thu nhập = lương cơ bản + doanh số * hoa hồng (%)

Thực lãnh: theo công thức chung

🔹 Bài 8 – TruongPhong

Thuộc tính: phu_cap_trach_nhiem, he_so_chuc_vu, so_nam_cong_tac

Thu nhập = lương cơ bản * hệ số + phụ cấp

Phúc lợi = 1 triệu + 100k * năm công tác

Thực lãnh: theo công thức chung


**NHẬN XÉT**:
Việc dùng thuộc tính `tuoi` là đơn giản để bắt đầu, nhưng không bền vững theo thời gian, vì:
- Tuổi thay đổi theo năm.
- Phải cập nhật thủ công mỗi năm.
- Không rõ thời điểm tuổi được cập nhật (mất tính chính xác nếu dùng trong báo cáo).

Giải pháp OOP tốt hơn: Dùng ngay_sinh hoặc nam_sinh
- Thuộc tính gốc: ngay_sinh (datetime.date) hoặc nam_sinh (int)
- Khi cần tính tuổi, dùng một phương thức: get_tuoi()

Gợi ý tinh chỉnh: 
- Tinh chỉnh class ConNguoi bai01_connguoi.py
- Xem lại các class có import class ConNguoi theo file mới cập nhật (hoặc ghi đè class cũ)
- Thay dữ liệu vào là tuổi bằng ngày sinh