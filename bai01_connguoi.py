# bai01_connguoi.py

class ConNguoi:
    def __init__(self, ho_ten: str, tuoi: int, gioi_tinh: str):
        self.ho_ten = ho_ten
        self.tuoi = tuoi
        self.gioi_tinh = gioi_tinh

    def __str__(self):
        return f"Họ tên: {self.ho_ten}, Tuổi: {self.tuoi}, Giới tính: {self.gioi_tinh}"

    def hien_thi_thong_tin(self):
        print(self.__str__())

# Demo test khi chạy file này trực tiếp
if __name__ == "__main__":
    nguoi = ConNguoi("Nguyen Van A", 30, "Nam")
    nguoi.hien_thi_thong_tin()
