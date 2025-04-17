## Bài 1
1.	Lớp ConNguoi: Lớp cha
o	Thuộc tính: ho_ten, tuoi, gioi_tinh
o	Phương thức: __init__, __str__, hien_thi_thong_tin() (hiển thị thông tin cơ bản)

## Bài 2 – Lớp SinhVien kế thừa ConNguoi, và dùng Interface (Abstract Base Class)
Điểm cần lưu ý:
SinhVien là lớp trung gian kế thừa ConNguoi
SinhVien có thêm thuộc tính ma_sinh_vien
get_diem() và xep_loai() được định nghĩa là phương thức trừu tượng (abstract) — để các lớp con như SinhVienIT, SinhVienKD triển khai.

## Bài 3:
- Kế thừa lớp SinhVien
- Bổ sung 3 thuộc tính: diem_A, diem_B, diem_C
- Cài đặt get_diem() theo công thức:
  diem = diem_A * 0.4 + diem_B * 0.35 + diem_C * 0.25
- Cài đặt xep_loai() theo điểm:
    ≥ 8.5: Giỏi
    ≥ 7.0: Khá
    ≥ 5.5: Trung bình
    < 5.5: Yếu

## Bài 4:
* SinhVienKD (Sinh viên khối Kinh Doanh) kế thừa từ SinhVien, tương tự như SinhVienIT, nhưng sử dụng công thức tính điểm khác.
- Kế thừa từ lớp SinhVien
- Bổ sung thuộc tính: diem_X, diem_Y, diem_Z
- Cài đặt:
- get_diem() = diem_X * 0.2 + diem_Y * 0.3 + diem_Z * 0.5
- xep_loai():
    ≥ 8.5: Giỏi
    ≥ 7.0: Khá
    ≥ 6.0: Trung bình
    < 6.0: Yếu