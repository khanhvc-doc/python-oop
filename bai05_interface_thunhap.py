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
    
    @abstractmethod
    def get_bao_hiem(self) -> float:
        """Tính khoản bảo hiểm cần đóng"""
        pass

    @abstractmethod
    def get_phuc_loi(self) -> float:
        """Tiền phúc lợi được cộng thêm vào lương (nếu có)"""
        pass
