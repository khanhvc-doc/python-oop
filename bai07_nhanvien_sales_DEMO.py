from bai07_nhanvien_sales import NhanVienSales

def main():
    nv = NhanVienSales(
        ho_ten='Van Cong Khanh',
        tuoi= 30,
        gioi_tinh= 'Nam',
        ma_nhan_vien= 'NVSales01',
        luong_co_ban= 800000,
        doanh_so= 10000000,
        hoa_hong=0.05

    )
    nv.hien_thi_chi_tiet()

if __name__ == '__main__':
    main()