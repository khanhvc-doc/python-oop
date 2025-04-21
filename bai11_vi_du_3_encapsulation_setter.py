from abc import ABC, abstractmethod

class TaiKhoan(ABC):
    def __init__(self, so_tai_khoan: str, so_du: float = 0.0):
        self.__so_tai_khoan = so_tai_khoan
        self.__so_du = so_du

    @property
    def so_tai_khoan(self):
        return self.__so_tai_khoan

    @property
    def so_du(self):
        return self.__so_du

    @so_du.setter
    def so_du(self, value):
        if value >= 0:
            self.__so_du = value
        else:
            raise ValueError("Số dư không thể âm")

    def nap_tien(self, so_tien: float):
        if so_tien > 0:
            self.__so_du += so_tien
        else:
            raise ValueError("Số tiền phải lớn hơn 0")

    def rut_tien(self, so_tien: float):
        if 0 < so_tien <= self.__so_du:
            self.__so_du -= so_tien
        else:
            raise ValueError("Không thể rút số tiền này")

    def hien_thi_thong_tin(self):
        print(f"Tài khoản: {self.__so_tai_khoan}, Số dư: {self.__so_du:,.0f} VND")

    @abstractmethod
    def tinh_lai(self):
        pass


class TietKiem(TaiKhoan):
    def __init__(self, so_tai_khoan, so_du, lai_suat):
        super().__init__(so_tai_khoan, so_du)
        self.__lai_suat = lai_suat

    def tinh_lai(self):
        return self.so_du * self.__lai_suat

    @property
    def lai_suat(self):
        return self.__lai_suat

    @lai_suat.setter
    def lai_suat(self, value):
        if 0 < value <= 1:
            self.__lai_suat = value
        else:
            raise ValueError("Lãi suất phải nằm trong khoảng (0, 1]")


# ===== DEMO =====
if __name__ == "__main__":
    tk1 = TietKiem("987654", 5000000, 0.05)
    tk1.nap_tien(2000000)
    tk1.rut_tien(1000000)
    tk1.hien_thi_thong_tin()
    print(f"Lãi dự kiến: {tk1.tinh_lai():,.0f} VND")

    # Setter hoạt động:
    tk1.so_du = 10000000       # cập nhật số dư
    tk1.lai_suat = 0.08        # cập nhật lãi suất
    tk1.hien_thi_thong_tin()
    print(f"Lãi mới dự kiến: {tk1.tinh_lai():,.0f} VND")
