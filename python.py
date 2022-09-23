# Viết chương trình tính tiền hàng theo công thức: Thành tiền = Số lượng * Đơn giá.

'''
so_luong = int(input('Nhập số lượng : ')) 
don_gia = int(input('Nhập đơn giá : ')) 
thanh_tien = so_luong*don_gia

print('Thành tiền : ',thanh_tien)
'''

# Viết chương trình tính diện tích và chu vi hình tròn. 

'''
import math 

ban_kinh = int(input('Nhập bán kính : ')) 
p = 2 * ban_kinh * math.pi 
s = ban_kinh**2 * math.pi 

print('Chu vi hình tròn = %.2f'%p) 
print('Diện tích hình tròn = %.2f'%s)
# Dùng hàm print() để in giá trị chu vi và diện tích hình tròn, hai giá trị này sẽ được định dạng theo kiểu số thực float (f) và được làm tròn dưới dạng hai chữ số thập phân (%.2f và %p)
'''

# Viết chương trình đổi nhiệt độ từ độ C sang độ F.

'''
C = int(input('Nhập nhiệt độ C : ')) 
F = 9/5 * C + 32 

print('%.2f độ C = %.2f độ F' %(C,F))
'''

# Viết chương trình xử lý chuỗi theo yêu cầu:
# - Chuỗi s1, s2, s3 được nhập vào từ bàn phím.
# - Chỉ mục index được nhập từ bàn phím.
# - Cho biết chiều dài của chuỗi s1, s2 và s3.
# - Tạo chuỗi con s4 từ chuỗi s1 với nội dung từ Index đến hết chuỗi.
# - Lặp lại chuỗi s2: 2 lần.

'''
s1 = str(input('Nhập chuỗi s1 : ')) 
s2 = str(input('Nhập chuỗi s2 : ')) 
s3 = str(input('Nhập chuỗi s3 : ')) 
index = int(input('Nhập index là số : ')) 

print('Chiều dài của các chuỗi s1, s2 và s3 lần lượt là : ',len(s1),len(s2),len(s3)) 
print('Chuỗi s4 : ',s1[index:]) 
print('Chuỗi s2 lặp lại 2 lần :',s2*2)
'''

# Viết chương trình tính tiền lãi gửi tiết kiệm
# Tính tiền lãi gửi tiết kiệm: Lãi suất 1 năm, số tiền gửi và số tháng gửi được nhập vào từ bàn phím. Viết chương trình tính tiền lãi và tính tổng số tiền nhận được sau khi hết thời hạn gửi tiền: Tiền lãi = (Số tiền gửi * Số tháng) * (Lãi suất năm/12) ; Tổng số tiền = Số tiền gửi + Tiền lãi. Sau đó hiển thị kết quả.

'''
lai_suat = float(input('Nhập lãi suất 1 năm : ')) 
so_tien_gui = int(input('Nhập số tiền gửi : ')) 
so_thang_gui = int(input('Nhập số tháng gửi : ')) 
so_tien_lai = (so_tien_gui*so_thang_gui) * (lai_suat / 100 / 12) 
tong_tien = so_tien_gui + so_tien_lai 

print('Tiền lãi ',int(so_tien_lai)) 
print('Tổng tiền = Tiền vốn + Tiền lãi =',int(tong_tien))
'''