from phuong_tien import PhuongTien

class MayBay(PhuongTien):
    def di_chuyen(self):
        print(f"{self.ten_phuong_tien} đang bay trên bầu trời.")

    def tinh_toc_do(self, quang_duong, thoi_gian):
        toc_do = super().tinh_toc_do(quang_duong, thoi_gian)
        # Tăng thêm do có gió thuận, ví dụ +15%
        return toc_do * 1.15



