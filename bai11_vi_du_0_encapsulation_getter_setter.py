class Thuong:
    def __init__(self):
        self.__value = 0

    
    def value(self):
        return self.__value
    

    def main(self):
        obj = Thuong()
        print(f"Thường: {obj.value()}") # gọi hàm value() , có dấu ()



class dungGetter:
    def __init__(self):
        self.__value = 0

    @property
    def value(self):
        return self.__value
    

    def main(self):
        obj = dungGetter()
        print(f"dùng getter: {obj.value}")  # không có dấu ()
        # obj.value = 1000 # dòng này sẽ bị lỗi vì @property chỉ dùng để lấy giá trị


class dungSetter:
    def __init__(self):
        self.__value = 0

    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, new_value):
        print("Setter được gọi")
        self.__value = new_value

    def main(self):
        obj = dungSetter()
        print(f"Getter CHƯA thiết lập giá trị: {obj.value}")
        obj.value = 123
        print(f"Getter ĐÃ thiết lập giá trị: {obj.value}")


if __name__ == '__main__':
    # Thuong().main()
    dungGetter().main()
    # dungSetter().main()
    
