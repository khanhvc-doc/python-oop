from abc import ABC, abstractmethod

class PhuongTien(ABC):
    def __init__(self, ten_phuong_tien):
        self.ten_phuong_tien = ten_phuong_tien

    @abstractmethod
    def di_chuyen(self):
        pass

    def tinh_toc_do(self, quang_duong, thoi_gian):
        if thoi_gian <= 0:
            raise ValueError("Thời gian phải lớn hơn 0")
        return quang_duong / thoi_gian