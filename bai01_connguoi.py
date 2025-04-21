# bai01_connguoi.py

from datetime import datetime, date

class ConNguoi:
    def __init__(self, ho_ten, ngay_sinh, gioi_tinh):
        # Ép kiểu nếu truyền vào là chuỗi
        if isinstance(ngay_sinh, str):
            self.ngay_sinh = datetime.strptime(ngay_sinh, "%d/%m/%Y").date()
        elif isinstance(ngay_sinh, date):
            self.ngay_sinh = ngay_sinh
        else:
            raise ValueError("ngay_sinh phải là date hoặc chuỗi dạng dd/mm/yyyy")
        self.ho_ten = ho_ten
        self.gioi_tinh = gioi_tinh

    def get_tuoi(self):
        today = date.today()
        return today.year - self.ngay_sinh.year - (
            (today.month, today.day) < (self.ngay_sinh.month, self.ngay_sinh.day)
        )

    def __str__(self):
        return f"Họ tên: {self.ho_ten}, Tuổi: {self.get_tuoi()}, Giới tính: {self.gioi_tinh}"

    def hien_thi_thong_tin(self):
        print(self.__str__())


# Demo test khi chạy file này trực tiếp
if __name__ == "__main__":
    nguoi = ConNguoi("Van Cong Khanh", "10/10/2000", "Nam")
    nguoi.hien_thi_thong_tin()
