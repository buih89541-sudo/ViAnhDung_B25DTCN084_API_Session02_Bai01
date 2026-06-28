"""
1. Quy trình xử lý khi truy cập /students:
    - Client gửi yêu cầu GET đến /students.
    - FastAPI kiểm tra URL và tìm endpoint phù hợp.
    - Hàm get_students() được thực thi.
    - Hàm trả về dictionary {"students": students}.
    - FastAPI tự động chuyển dictionary thành JSON rồi gửi phản hồi cho client.

2. Vì sao không trả về string?
    - String chỉ là một chuỗi văn bản đơn giản.
    - JSON có cấu trúc rõ ràng, giúp client dễ xử lý và có thể bổ sung thêm các trường dữ liệu khi cần.

3. Thiết kế REST endpoint:
    - Không đặt tên endpoint bằng động từ như /getStudents.
    - Nên sử dụng danh từ số nhiều, ví dụ: GET /students, để đúng nguyên tắc REST.
"""
from fastapi import FastAPI

app = FastAPI()

students = ["An", "Binh", "Cuong"]

@app.get("/students")
def get_students():
    return {"students": students}
