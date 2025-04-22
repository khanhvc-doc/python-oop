from phuong_tien import PhuongTien

class TauHoa(PhuongTien):
    def di_chuyen(self):
        print(f"{self.ten_phuong_tien} đang chạy trên đường ray.")

    def tinh_toc_do(self, quang_duong, thoi_gian):
        toc_do = super().tinh_toc_do(quang_duong, thoi_gian)
        # Giảm do điểm dừng, ví dụ giảm 10%
        return toc_do * 0.9