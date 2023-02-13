Các hàm sử dụng 
-- Các fuction controller từ phía client local để điều khiển client website thực hiện --
    ----Hàm khái quát----
emit_server(task, place, content)
        --Ghi chú--

task: là nhiệm vụ cần điều khiển:
    task = TextoControllerWeb ("dùng để điều khiển những nội dung trong web client bằng text")
    task = TextoControllerLinkWeb ("dùng để điều khiển những link web client bằng text")
    task = TextoAlertWeb ("Dùng để thông báo cho web bằng text") 
        - Dùng trong thông báo cho web về trạng thái hiển thị chữ trên module xong để web client thực hiện tiếp nhiệm vụ
        - Dùng trong thông báo cho web về nhiệm vụ cần điều khiển ở các trang web

place: là nơi cần điều khiển:
    place = Home ("Dùng để điều khiển hoặc thông báo ở vị trí trang Home")
    place = Page_detect("Dùng để điều khiển hoặc thông báo ở vị trí trang Detect")
    place = Page_lesson("Dùng để điều khiển hoặc thông báo ở vị trí trang Lesson")
    place = Page_document("Dùng để điều khiển hoặc thông báo ở vị trí trang Document")

content: là nội dung mà ta cần chuyển cho web client cần thực hiện hay thông báo


<!-- Example -->
1. Gửi 1 controller lên web client thực hiện việc chuyển sang trang detect bằng nút nhấn
emit_server("TextoControllerLinkWeb", "Home", "DETECT")
2. Gửi thông báo lên web client ở trang detect việc hiển thị chữ trên thiết bị đã xong
msg = {"display_text":"done"}
emit_server("TextoAlertWeb", "Page_detect", msg)

3. Gửi 1 controller lên web client thực hiện việc chọn bài học bằng nút nhấn
lưu ý: tạo một biến local là position_curr
position_curr = "" /* để lưu vị trí hiện tại của trang lesson là đang chọn bài học hay đã chọn bài xong*/
*khi ta chuyển qua trang detect thì bên client local sẽ nhận được 1 alert là position_curr = "choose_lesson"
emit_server("TextoControllerWeb", "Page_lesson", "NEXT") => thì web client sẽ thực hiện chọn bài học


