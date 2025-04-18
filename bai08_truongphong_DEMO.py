# demo_bai08_truongphong.py

from bai08_truongphong import TruongPhong

def main():
    print("== Demo TruongPhong ==")
    tp = TruongPhong(
        ho_ten="Tony Tèo",
        tuoi=45,
        gioi_tinh="Nam",
        ma_nhan_vien="TP01",
        luong_co_ban=15000000,
        phu_cap_trach_nhiem=3000000,
        he_so_chuc_vu=1.6,
        so_nam_cong_tac=10
    )
    tp.hien_thi_chi_tiet()

if __name__ == "__main__":
    main()
