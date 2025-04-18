## Bài 1
1.	Lớp ConNguoi: Lớp cha
o	Thuộc tính: ho_ten, tuoi, gioi_tinh
o	Phương thức: __init__, __str__, hien_thi_thong_tin() (hiển thị thông tin cơ bản)

## Bài 2
- Lớp SinhVien kế thừa ConNguoi, và dùng Interface (Abstract Base Class)
* Điểm cần lưu ý:
- - SinhVien là lớp trung gian kế thừa ConNguoi
- - SinhVien có thêm thuộc tính ma_sinh_vien
- - get_diem() và xep_loai() được định nghĩa là phương thức trừu tượng (abstract) — để các lớp con như SinhVienIT, SinhVienKD triển khai.

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
    get_diem() = diem_X * 0.2 + diem_Y * 0.3 + diem_Z * 0.5
- xep_loai():
    ≥ 8.5: Giỏi
    ≥ 7.0: Khá
    ≥ 6.0: Trung bình
    < 6.0: Yếu

## Bài 5 – NhanVien:
- Kế thừa từ ConNguoi
- Thêm thuộc tính:
- - ma_nhan_vien
- - luong_co_ban
- Định nghĩa 2 phương thức trừu tượng (interface) được tách riêng ra như một “interface độc lập”:
- - get_thu_nhap() → mỗi phòng ban sẽ tính khác nhau
- - get_thue() → có thể được định nghĩa mặc định hoặc trừu tượng nếu mỗi nơi có mức thuế riêng
- - get_bao_hiem()
- - get_phuc_loi()

## Bài 6 - NhanVien HR:
- Kế thừa lớp NhanVien và ghi đè - Overwrite các phương thức
- get_thu_nhap() → lương cơ bản
- get_thue() → 10% thu nhập
- get_bao_hiem() → ví dụ 8% lương
- get_phuc_loi() → có thể là 0 hoặc giá trị khác tùy phòng ban

## Bài 7 - NhanVien Sale:
- Có thêm 2 thuộc tính riêng (vẫn thừa kế NhanVien):
- - doanh_so – tổng doanh số
- - hoa_hong – phần trăm hoa hồng (ví dụ: 0.05 = 5%)
- Công thức thu nhập:
- - thu_nhap = luong_co_ban + doanh_so * hoa_hong 
- - thực lãnh = thu nhập - thuế - bảo hiểm + phúc lợi

## Bài 8: kế thừa từ NhanVien
- Thuộc tính bổ sung:
- - phu_cap_trach_nhiem: float
- - he_so_chuc_vu: float – dùng để nhân với lương cơ bản
- - so_nam_cong_tac: int – ảnh hưởng đến phúc lợi

Các phương thức:
- - get_thu_nhap() = luong_co_ban * he_so_chuc_vu + phu_cap_trach_nhiem
- - get_phuc_loi() = 1_000_000 + so_nam_cong_tac * 100_000
- - get_thue() và get_bao_hiem() như trước
- - hien_thi_chi_tiet() hiển thị toàn bộ