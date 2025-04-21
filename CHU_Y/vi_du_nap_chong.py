class TinhToan:
    def tinh_tong(self, *args): # args là tên biến tùy ý, quan trọng là dấu *. mà nên dùng chữ args
        if not args:
            return 0  # Không truyền gì thì trả về 0
        tong = 0
        for x in args:
            tong += x
        return tong
    


# Test
if __name__ == "__main__":
    tt = TinhToan()
    print(tt.tinh_tong(5))               # 5
    print(tt.tinh_tong(5, 10))           # 15
    print(tt.tinh_tong(1, 2, 3))         # 6
    print(tt.tinh_tong(1, 2, 3, 4, 5))   # 15
    print(tt.tinh_tong())                # 0

