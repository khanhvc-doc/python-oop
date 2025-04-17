## Bài 1
1.	Lớp ConNguoi: Lớp cha
o	Thuộc tính: ho_ten, tuoi, gioi_tinh
o	Phương thức: __init__, __str__, hien_thi_thong_tin() (hiển thị thông tin cơ bản)

## Bài 2 – Lớp SinhVien kế thừa ConNguoi, và dùng Interface (Abstract Base Class)
Điểm cần lưu ý:
SinhVien là lớp trung gian kế thừa ConNguoi
SinhVien có thêm thuộc tính ma_sinh_vien
get_diem() và xep_loai() được định nghĩa là phương thức trừu tượng (abstract) — để các lớp con như SinhVienIT, SinhVienKD triển khai.