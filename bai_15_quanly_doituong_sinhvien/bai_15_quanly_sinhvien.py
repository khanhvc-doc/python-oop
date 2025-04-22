# bai_15_quanly_sinhvien.py

import pandas as pd
from datetime import datetime
from bai01_connguoi import ConNguoi
from bai03_sinhvien_it import SinhVienIT
from bai04_sinhvien_kd import SinhVienKD

class QuanLySinhVien:
    def __init__(self):
        self.danh_sach_sinh_vien = []
    
    def them_sinh_vien_tu_dict(self, sinh_vien_dict_list):
        """
        Thêm sinh viên từ danh sách dictionary
        """
        for sv_dict in sinh_vien_dict_list:
            # Thông tin chung
            ho_ten = sv_dict.get('ho_ten')
            ngay_sinh = sv_dict.get('ngay_sinh')
            gioi_tinh = sv_dict.get('gioi_tinh')
            dia_chi = sv_dict.get('dia_chi')
            ma_sinh_vien = sv_dict.get('ma_sinh_vien')
            loai_sinh_vien = sv_dict.get('loai_sinh_vien')
            
            # Tạo đối tượng sinh viên phù hợp
            if loai_sinh_vien == 'IT':
                diem_A = sv_dict.get('diem_A', 0)
                diem_B = sv_dict.get('diem_B', 0)
                diem_C = sv_dict.get('diem_C', 0)
                sv = SinhVienIT(ho_ten, ngay_sinh, gioi_tinh, dia_chi, ma_sinh_vien, diem_A, diem_B, diem_C)
            elif loai_sinh_vien == 'KD':
                diem_X = sv_dict.get('diem_X', 0)
                diem_Y = sv_dict.get('diem_Y', 0)
                diem_Z = sv_dict.get('diem_Z', 0)
                sv = SinhVienKD(ho_ten, ngay_sinh, gioi_tinh, dia_chi, ma_sinh_vien, diem_X, diem_Y, diem_Z)
            else:
                print(f"Loại sinh viên không hợp lệ: {loai_sinh_vien}")
                continue
                
            self.danh_sach_sinh_vien.append(sv)
            
    def hien_thi_danh_sach(self):
        """
        Hiển thị danh sách sinh viên
        """
        print("\n--- DANH SÁCH SINH VIÊN ---")
        for i, sv in enumerate(self.danh_sach_sinh_vien, 1):
            print(f"{i}. ", end="")
            sv.hien_thi_thong_tin()
            
    def luu_vao_csv(self, file_path):
        """
        Lưu danh sách sinh viên vào file CSV
        """
        data = []
        for sv in self.danh_sach_sinh_vien:
            sv_dict = {
                'ho_ten': sv.ho_ten,
                'ngay_sinh': sv.ngay_sinh.strftime("%d/%m/%Y"),
                'gioi_tinh': sv.gioi_tinh,
                'dia_chi': sv.dia_chi,
                'ma_sinh_vien': sv.ma_sinh_vien,
                'diem_trung_binh': round(sv.get_diem(), 2),
                'xep_loai': sv.xep_loai()
            }
            
            # Thêm thông tin riêng của từng loại sinh viên
            if isinstance(sv, SinhVienIT):
                sv_dict['loai_sinh_vien'] = 'IT'
                sv_dict['diem_A'] = sv.diem_A
                sv_dict['diem_B'] = sv.diem_B
                sv_dict['diem_C'] = sv.diem_C
            elif isinstance(sv, SinhVienKD):
                sv_dict['loai_sinh_vien'] = 'KD'
                sv_dict['diem_X'] = sv.diem_X
                sv_dict['diem_Y'] = sv.diem_Y
                sv_dict['diem_Z'] = sv.diem_Z
                
            data.append(sv_dict)
            
        df = pd.DataFrame(data)
        df.to_csv(file_path, index=False, encoding='utf-8-sig')
        print(f"Đã lưu danh sách sinh viên vào file {file_path}")
        
    def doc_tu_csv(self, file_path):
        """
        Đọc danh sách sinh viên từ file CSV
        """
        try:
            df = pd.read_csv(file_path, encoding='utf-8-sig')
            sinh_vien_dict_list = df.to_dict('records')
            self.danh_sach_sinh_vien = []  # Xóa danh sách hiện tại
            self.them_sinh_vien_tu_dict(sinh_vien_dict_list)
            print(f"Đã đọc danh sách sinh viên từ file {file_path}")
        except Exception as e:
            print(f"Lỗi khi đọc file CSV: {e}")
            
    def loc_sinh_vien_theo_loai(self, loai_sinh_vien):
        """
        Lọc sinh viên theo loại (IT hoặc KD)
        """
        if loai_sinh_vien == 'IT':
            return [sv for sv in self.danh_sach_sinh_vien if isinstance(sv, SinhVienIT)]
        elif loai_sinh_vien == 'KD':
            return [sv for sv in self.danh_sach_sinh_vien if isinstance(sv, SinhVienKD)]
        else:
            print(f"Loại sinh viên không hợp lệ: {loai_sinh_vien}")
            return []
            
    def tim_sinh_vien_diem_cao_nhat(self):
        """
        Tìm sinh viên có điểm trung bình cao nhất
        """
        if not self.danh_sach_sinh_vien:
            print("Danh sách sinh viên rỗng!")
            return None
            
        sv_diem_cao_nhat = max(self.danh_sach_sinh_vien, key=lambda sv: sv.get_diem())
        return sv_diem_cao_nhat


# Demo test
if __name__ == "__main__":
    quan_ly = QuanLySinhVien()
    
    # Dữ liệu mẫu
    sinh_vien_list = [
        {
            'ho_ten': 'Nguyễn Văn A',
            'ngay_sinh': '15/05/2000',
            'gioi_tinh': 'Nam',
            'dia_chi': 'Quận 1, TP.HCM',
            'ma_sinh_vien': 'IT001',
            'loai_sinh_vien': 'IT',
            'diem_A': 8.5,
            'diem_B': 9.0,
            'diem_C': 7.5
        },
        {
            'ho_ten': 'Trần Thị B',
            'ngay_sinh': '20/10/2001',
            'gioi_tinh': 'Nữ',
            'dia_chi': 'Quận 7, TP.HCM',
            'ma_sinh_vien': 'KD001',
            'loai_sinh_vien': 'KD',
            'diem_X': 7.0,
            'diem_Y': 8.0,
            'diem_Z': 9.0
        },
        {
            'ho_ten': 'Lê Văn C',
            'ngay_sinh': '05/12/1999',
            'gioi_tinh': 'Nam',
            'dia_chi': 'Quận 3, TP.HCM',
            'ma_sinh_vien': 'IT002',
            'loai_sinh_vien': 'IT',
            'diem_A': 7.0,
            'diem_B': 7.5,
            'diem_C': 8.0
        }
    ]
    
    # Thêm sinh viên từ dictionary
    quan_ly.them_sinh_vien_tu_dict(sinh_vien_list)
    
    # Hiển thị danh sách sinh viên
    quan_ly.hien_thi_danh_sach()
    
    # Lưu vào file CSV
    quan_ly.luu_vao_csv('danh_sach_sinh_vien.csv')
    
    # Xóa danh sách hiện tại và đọc lại từ file CSV
    quan_ly.danh_sach_sinh_vien = []
    quan_ly.doc_tu_csv('danh_sach_sinh_vien.csv')
    
    print("\n--- SAU KHI ĐỌC TỪ FILE CSV ---")
    quan_ly.hien_thi_danh_sach()
    
    # Lọc sinh viên theo loại
    sv_it = quan_ly.loc_sinh_vien_theo_loai('IT')
    print("\n--- DANH SÁCH SINH VIÊN IT ---")
    for sv in sv_it:
        sv.hien_thi_thong_tin()
        
    # Tìm sinh viên có điểm cao nhất
    sv_diem_cao = quan_ly.tim_sinh_vien_diem_cao_nhat()
    print("\n--- SINH VIÊN CÓ ĐIỂM CAO NHẤT ---")
    if sv_diem_cao:
        sv_diem_cao.hien_thi_thong_tin()