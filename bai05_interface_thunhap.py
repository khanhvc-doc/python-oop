# bai05_interface_thunhap.py

from abc import ABC, abstractmethod

class IThuNhap(ABC):
    @abstractmethod
    def get_thu_nhap(self) -> float:
        """Tính thu nhập (tùy từng loại nhân viên)"""
        pass

    @abstractmethod
    def get_thue(self) -> float:
        """Tính thuế thu nhập (có thể dựa trên thu nhập)"""
        pass
