from xe_dap import XeDap
from xe_may import XeMay
from oto import Oto
from may_bay import MayBay
from tau_hoa import TauHoa


if __name__ == "__main__":
    # khởi tạo đối tượng
    xe_dap = XeDap("Xe Đạp Thống Nhất")
    xe_may = XeMay("Xe Máy Honda")
    xe_oto = Oto("Ôtô VinFast")
    tau_hoa = TauHoa("SE4 Hà Nội - Sài Gòn")
    may_bay = MayBay("Airbus A350")

    # Gọi phương thức
    xe_dap.di_chuyen()
    tau_hoa.di_chuyen()
    may_bay.di_chuyen()

    # Gọi hàm tính tốc độ kế thừa từ lớp cha
    print(f"Tốc độ máy bay: {may_bay.tinh_toc_do(1000, 2)} km/h")
    print(f"Tốc độ tàu hỏa: {tau_hoa.tinh_toc_do(600, 6)} km/h")
    print(f"Tốc độ Ô tô: {xe_oto.tinh_toc_do(600, 6)} km/h")




