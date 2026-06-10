def show_products(products_list):
    if (len(products_list) == 0):
        print("Cửa hàng hiện chưa có sản phẩm nào!")
        return

    print("--- DANH SÁCH SẢN PHẨM ---")
    print(f"{'ID':<5} | {'Tên sản phẩm':<20} | {'Giá bán'}")
    print("----------------------------------------------------")
    for item in products_list:
        print(f"{item.get('id'):<5} | {item.get('name'):<20} | {item.get('price')}")

def add_product(products_list):
    while True:
        id_input = input("Nhập mã sản phẩm (ID): ").strip().upper()
        if (len(id_input) == 0):
            print("Mã sản phẩm không được để trống! Vui lòng nhập lại: ")
        else:
            name_input = input("Nhập tên sản phẩm: ").strip().capitalize()
            if (len(name_input) == 0):
                print("Tên sản phẩm không được để trống! Vui lòng nhập lại")
            else:
                price_input = input("Nhập giá bán: ")
                if (not price_input.isdigit() or int(price_input) <= 0):
                    print("Giá bán phải là số nguyên dương lớn hơn 0")
                price_input = int(price_input)

                new_product = [{'id': id_input, 'name': name_input, 'price': price_input}]
                products_list.append(new_product)
                print("Thêm sản phẩm thành công!")
                break

def main():
    products = [
        {'id': 'P01', 'name': 'Coca Cola', 'price': 15000},
        {'id': 'P02', 'name': 'Bánh mì', 'price': 20000}
    ]

    while True:
        title = f" QUẢN LÝ CỬA HÀNG - MINI STORE ".center(50, "=")
        user_choice = input(f"""
{title}
1. Xem danh sách sản phẩm hiện có
2. Thêm mới một sản phẩm
3. Cập nhật giá sản phẩm theo ID
4. Thoát chương trình
{len(title) * '='}
-> Nhập lựa chọn của bạn: """)

        match user_choice:
            case "1":
                show_products(products)
            case "2":
                add_product(products)
            case "3":
                pass
            case "4":
                print("Cảm ơn bạn đã sử dụng phần mềm!\n[Chương trình kết thúc]")
                break
            case _:
                print("Lựa chọn không hợp lệ, vui lòng nhập lại")

main()