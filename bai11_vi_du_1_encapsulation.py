class BankAccount:
    def __init__(self, so_tai_khoan, so_du):
        self.__so_tai_khoan = so_tai_khoan   # Thuộc tính private
        self.__so_du = so_du                 # Không cho ai ngoài truy cập trực tiếp

    def nap_tien(self, so_tien):
        if so_tien > 0:
            self.__so_du += so_tien

    def rut_tien(self, so_tien):
        if 0 < so_tien <= self.__so_du:
            self.__so_du -= so_tien

    def hien_thi_so_du(self):
        print(f"Số dư hiện tại: {self.__so_du}")

# --- Demo ---
acc = BankAccount("123456", 1000)
acc.nap_tien(500)
acc.rut_tien(300)
acc.hien_thi_so_du()   # Kết quả: Số dư hiện tại: 1200

# acc.__so_du = 999999  # Sẽ không sửa được trực tiếp do bị "ẩn"
