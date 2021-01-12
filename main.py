#các thư viện cần thiết
import folder_op, wed_op


def  start():
    url_list = ['https:''vietnamnet.vn'] #chứa các đường link sẽ được duyệt
    history = []  #chứa các đường link đã được duyệt
    max_page = 1000 #quy định đố lượng trang wed được tải về
    count = 0 # số lượng trang wed được tải về
    data_folder = "O:\\wed_scraping"


    #kịch bản tải các trang wed
    while (count < max_page) and (len(url_list) > 0) :
        url = url_list.pop(0)
        page = wed_op.doc_noi_dung(url)
        links = wed_op.lay_cac_duong_link(page)
        for item in links : #duyệt đường link để kiểm tra tính hợp lệ
            if wed_op.kiem_tra_link(item): #nếu đường link là hợp lệ thì tiếp tục
                item = wed_op.chinh_sua_link(item) #chỉnh sửa nếu thấy thiếu phần https://.....
                if not((item in url_list) and (item in history)):# nếu đường link chưa hề được duyệt và chưa
                    url_list.append(item) #thêm đường link mới vào danh sách chờ duyệt

        folder_op.luu_noi_dung_xuong_file(page, data_folder)
        history.append(url)
        count +=1








# Press the green button in the gutter to run the script.
if __name__ == '__main__':
     start()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
