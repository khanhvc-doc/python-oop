# test nhân viên HR
from bai06_nhanvien_hr import NhanVienHR

def main():
    print("== Demo NhanVienHR ==")
    nv = NhanVienHR("Nguyen Thi Hoa", 32, "Nữ", "HR001", 10000000)
    nv.hien_thi_chi_tiet()

if __name__ == "__main__":
    main()