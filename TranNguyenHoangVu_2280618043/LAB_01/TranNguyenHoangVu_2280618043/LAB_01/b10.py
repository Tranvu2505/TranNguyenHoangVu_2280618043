def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]
input_string = input("mời nhập chuỗi cần dảo ngược: ")
print("Chuỗi đảo ngược là: ", dao_nguoc_chuoi(input_string))