
import streamlit as st
import time
import random

# Page configuration
st.set_page_config(page_title="DLP4 RPG", layout="centered")

# Custom CSS for a light RPG school theme
st.markdown("""<style>
body {
    background-color: #f0f8ff;
    color: #333333;
    font-family: 'Courier New', monospace;
}
h1, h2, h3 {
    font-family: 'Courier New', monospace;
}
button {
    background-color: #8b4513;
    color: #ffffff;
    border-radius: 8px;
    padding: 6px 12px;
    margin: 4px;
}
</style>""", unsafe_allow_html=True)

# Typewriter effect
def typewriter(text, speed=0.02):
    placeholder = st.empty()
    displayed = ""
    for c in text:
        displayed += c
        placeholder.markdown(f"<p style='font-family: monospace; font-size:20px'>{displayed}</p>", unsafe_allow_html=True)
        time.sleep(speed)

# Staff selection mapping for scenes 4-6
staff_options = {
    4: [
        ("Nguyễn Thị Thu Hà (Yoogi)", 7), ("Nguyễn Thu Hương", 8), ("Trịnh Thị Phương Uyên", 9),
        ("Phan Mai Ngọc Linh", 10), ("Trần Lê Khánh Chi", 11), ("Lê Phương Nhi", 12),
        ("Đỗ Lê Ngọc Minh", 13), ("Đỗ Hoàng Gia Huy", 14), ("Trần Triệu Vy", 15),
        ("Phạm Nguyễn Thu Hà", 16), ("Hoàng Bích Phượng", 17), ("Trịnh Hoàng Nhật Lệ", 18),
        ("Nguyễn Thị Thùy Trang", 19), ("Hán Ngọc Bảo Trân", 20), ("Nguyễn Đức Dương", 21),
        ("Trần Anh Đức", 22), ("Lý Hạnh Linh", 23), ("Nguyễn Thị Khánh Linh", 24)
    ],
    5: [
        ("Hoàng Thị Thảo Anh", 25), ("Tá Mai Linh", 26), ("Đỗ Minh Châu", 27),
        ("Lê Chí Nam", 28), ("Nguyễn Việt Anh", 29), ("Đỗ Phương Anh", 30),
        ("Trần Hoàng Thắng", 31), ("Nguyễn Thảo Đan", 32), ("Trần Thanh An", 33),
        ("Nguyễn Tùng Lâm", 34), ("Phạm Hà Phương", 35)
    ],
    6: [
        ("Anh Trần Chí Trung", 36), ("Đoàn Hoa Hạ", 37), ("Phạm Tuyết Mai", 38),
        ("Mai Minh Quân", 39)
    ]
}

# NPC data for scenes 7-39
npc_data = {
    7: {
        "Tên": "Nguyễn Thị Thu Hà (Yoogi)",
        "Ngày sinh": "19/11",
        "Cung hoàng đạo": "Bọ Cạp",
        "Đặc điểm nhận dạng": "Luôn bốc cháy, dâng hiến cả con tim",
        "Link FB": "https://www.facebook.com/ha.yoongie.7/",
        "Lời chào đầu": "Mình là Yoogie, mình thấy mình rất hài hước, mình thích được mang những câu joke vui vẻ đến với mọi người. Mình cung nước (Bọ Cạp) nên nhìn nhìn ngoài dữ nhưng bên trong mềm nhũn."
    },
    8: {
        "Tên": "Nguyễn Thu Hương",
        "Ngày sinh": "11/07",
        "Cung hoàng đạo": "Cự Giải",
        "Đặc điểm nhận dạng": "thích lượn nhờ phố cổ Hà Nội, ăn 1 lúc 2 suất",
        "Link FB": "https://www.facebook.com/nguyenthuhuong1107",
        "Lời chào đầu": "Bonjour, chao xìn cả nhà yêu của kem!!! Em/mình/chị là Thu Hương, or Hương 2 suất cơm (dù giờ tới mình vẫn chưa nhận được suất thứ 2!)"
    },
    9: {
        "Tên": "Trịnh Thị Phương Uyên",
        "Ngày sinh": "19/12",
        "Cung hoàng đạo": "Nhân Mã",
        "Đặc điểm nhận dạng": "Thích đi xe bus, là nhân vật trong một câu chuyện cổ tích",
        "Link FB": "https://www.facebook.com/profile.php?id=100018092570083",
        "Lời chào đầu": "Hi mọi ngừi, mình là Uyên Trịnh. Uyên trong Uyên Trịnh và Trịnh trong Uyên Trịnh. Rất vui khi cuối cùng đã được chung VUCA với mọi ngườii. VUCA trong Vui vẻ - Ung dung - Chân thành - An nhiên 😘"
    },
    10: {
        "Tên": "Phan Mai Ngọc Linh",
        "Ngày sinh": "09/01",
        "Cung hoàng đạo": "Ma Kết",
        "Đặc điểm nhận dạng": "Luôn đúng giờ, tìm thấy bình yên khi ngồi trước biển.",
        "Link FB": "https://www.facebook.com/phan.maingoclinh0901",
        "Lời chào đầu": "Chào chúng ta, mình là.........à mình là Ngọc Linh, mình vừa mới ngủ gật. Đêm nào ngủ mình cũng mơ về DLP..."
    },
    11: {
        "Tên": "Trần Lê Khánh Chi",
        "Ngày sinh": "06/09",
        "Cung hoàng đạo": "Xử Nữ",
        "Đặc điểm nhận dạng": "thực hành lãnh đạo liên tục trên nền tảng điện tử",
        "Link FB": "https://www.facebook.com/khanhchi.tranle",
        "Lời chào đầu": "Mình xin gửi tặng mng 1 tác phẩm thơ thay lời giới thiệu: Hai, ba cuốn vở ô ly. Chào mọi ngừi, mình là Khánh Chy 👏🏻🫶 Chúc mọi ngừi sẽ có khoảng thời gian thật tuyệt tại DLP4 ạa 🫶 ."
    },
    12: {
        "Tên": "Lê Phương Nhi",
        "Ngày sinh": "07/12",
        "Cung hoàng đạo": "Nhân Mã",
        "Đặc điểm nhận dạng": "không bao giờ được nằm trên giường khi đi bonding nhưng luôn là người ngồi lại cuối cùng với nồi lẩu",
        "Link FB": "https://www.facebook.com/nhikan14723",
        "Lời chào đầu": "Chào cả nhà, mình là Nhi, đệm Phương, họ Lê. Thông tin chi tiết hồi sau sẽ rõ. Welcome cả nhà đến với DLP4 và rất vui vì có thể được đồng hành cùng mọi người trong quãng thời gian sắp tớii. (*icon bùng nổ chào mừng pháo hoa*)"
    },
    13: {
        "Tên": "Đỗ Lê Ngọc Minh",
        "Ngày sinh": "23/08",
        "Cung hoàng đạo": "Xử Nữ",
        "Đặc điểm nhận dạng": "cứng cáp, vững vàng, thích đọc truyện, viết lách vẽ vời.",
        "Link FB": "https://www.facebook.com/profile.php?id=100047347188105&mibextid=LQQJ4d",
        "Lời chào đầu": "hihelloannyeongminhlangocminhcungsutunhinmathoicangnmathraminhbinhthuong"
    },
    14: {
        "Tên": "Đỗ Hoàng Gia Huy",
        "Ngày sinh": "28/12",
        "Cung hoàng đạo": "Ma Kết",
        "Đặc điểm nhận dạng": "thích hiphop nên hay bị lộn ruột, nấu ăn rất ngon nhưng chỉ đứng sau giật dây",
        "Link FB": "https://www.facebook.com/profile.php?id=100072990672246&mibextid=LQQJ4d",
        "Lời chào đầu": "Hí chúng ta, mình là Jerry... đúng hơn là Gia Huy. Là người đã trải qua VUCA về cả tinh thần lẫn...thể chất và tiêu chí đến là đón, mình sẽ luôn có mặt để giúp đỡ he (miễn là mọi ngườii muốn)."
    },
    15: {
        "Tên": "Trần Triệu Vy",
        "Ngày sinh": "12/10",
        "Cung hoàng đạo": "Thiên Bình",
        "Đặc điểm nhận dạng": "Từng đẩy 1 nam sinh bay 2m, có kinh nghiệm thực hành kết nối cảm xúc với người máy, cẩn thận bị brain rot khi tiếp xúc",
        "Link FB": "https://www.facebook.com/trieuvy.tran.92560",
        "Lời chào đầu": "Chào cả nhà, mình là Triệu Vy, mình thi trượt bằng lái xe 3 lần. Mình luôn trượt ở đoạn đi thẳng chứ vòng số 8 thì mình lụa lắm. Nên ai vòng vo thì gặp mình tung tung sahur vài đường cơ bản nhé 🚕🚗🚌🚘🏎️🛻"
    },
    16: {
        "Tên": "Phạm Nguyễn Thu Hà",
        "Ngày sinh": "31/07",
        "Cung hoàng đạo": "Sư Tử",
        "Đặc điểm nhận dạng": "Mother material, cảnh báo rất nhiều tình cảm đang tiến về phía bạn",
        "Link FB": "https://www.facebook.com/thuha.phamnguyen.9",
        "Lời chào đầu": "Gút mó ninh cả nhà, mình tên là Thu Hà, mình hay cười phà phà, Ha ha ha ha ha… "
    },
    17: {
        "Tên": "Hoàng Bích Phượng",
        "Ngày sinh": "12/03",
        "Cung hoàng đạo": "Song Ngư",
        "Đặc điểm nhận dạng": "安 (An)",
        "Link FB": "https://www.facebook.com/hoang.b.phuong.31?mibextid=ZbWKwL",
        "Lời chào đầu": "Chào cả nhà, mình là Phượng. Ưu điểm ai nói gì cũng tin, hehe"
    },
    18: {
        "Tên": "Trịnh Hoàng Nhật Lệ",
        "Ngày sinh": "10/08",
        "Cung hoàng đạo": "Sư Tử",
        "Đặc điểm nhận dạng": "Giọt nước mắt rơi lúc hoàng hôn ở Nhật Bản vì cười quá nhiều",
        "Link FB": "https://www.facebook.com/nhatle.trinhhoang",
        "Lời chào đầu": "Mình là Japan Cry. Dù có Japan nhưng mình thích xem, nghe, đọc phim và show truyền hình Việt Nam"
    },
    19: {
        "Tên": "Nguyễn Thị Thùy Trang",
        "Ngày sinh": "28/09",
        "Cung hoàng đạo": "Thiên Bình",
        "Đặc điểm nhận dạng": "Nhẹ nhàng vững vàng, kiềm được mọi cơn sóng cứng đầu nhất.",
        "Link FB": "https://www.facebook.com/trangs.thuys.9619",
        "Lời chào đầu": "67 104 195 160 111 32 99 225 186 163 32 110 104 195 160 44 32 109 195 172 110 104 32 108 195 160 32 84 114 97 110 103 46 32 77 195 172 110 104 32 116 104 195 173 99 104 32 104 198 176 225 187 155 110 103 32 100 198 176 198 161 110 103 44 32 110 225 186 175 110 103 32 110 104 198 176 110 103 32 116 104 195 173 99 104 32 110 104 225 186 165 116 32 108 195 160 32 68 76 80 46 32 65 105 32 99 195 179 32 99 195 185 110 103 32 115 225 187 159 32 116 104 195 173 99 104 32 99 117 225 187 145 105 32 116 104 195"
    },
    20: {
        "Tên": "Hán Ngọc Bảo Trân",
        "Ngày sinh": "02/07",
        "Cung hoàng đạo": "Cự Giải",
        "Đặc điểm nhận dạng": "Mới chuyển hộ khẩu lên núi và có view nhà nhìn ra thác - thác Bản Joke.",
        "Link FB": "https://fb.com/han.ngocbaotran.35",
        "Lời chào đầu": "Mình là Trân, giới tính Nam, dân tộc Kinh. Quê Yên bái, uống nước suối, ăn rau rừng và cưỡi ngựa đi học…"
    },
    21: {
        "Tên": "Nguyễn Đức Dương",
        "Ngày sinh": "17/09",
        "Cung hoàng đạo": "Xử Nữ",
        "Đặc điểm nhận dạng": "Cởi mở, tươi sáng và thích mời bạn tới chơi nhà",
        "Link FB": "https://www.facebook.com/mr.scheherazade",
        "Lời chào đầu": ""Xin chào các bạn DLP-er đời mới!
Mình là Dương – “hàng cũ quay lại” từ DLP mùa 1, nay trở lại với vai trò TA (không phải trợ giảng mà là Trùm Áp lực nha 😈).
Là một Xử Nữ tháng 9 chính hiệu nên mình cực kỳ khó tính, cực kỳ thù dai, cực kỳ để bụng – bạn nộp trễ 1 phút là mình nhớ tới Tết luôn đó 😤. Trong tình cảm thì redflag chói lóa, nhưng trong công việc thì yên tâm, mình luôn bật đèn xanh cho những ai chịu học, chịu chơi, chịu hỏi.
Mình mê Scheherazade vì chị ấy biết cách sinh tồn bằng storytelling – còn mình sống sót qua mùa 1 bằng... sức mạnh drama và deadline 😮‍💨.
Nếu các bạn cần người đồng hành, hỏi han, tâm sự hay đơn giản là một chiếc Google sống biết cà khịa – thì mình đây.
Cùng nhau biến mùa DLP này thành một hành trình vừa brainrot, vừa xịn, vừa không-đùa-được-đâu nha. Let's gooo 💥🔥""
    },
    22: {
        "Tên": "Trần Anh Đức",
        "Ngày sinh": "28/5",
        "Cung hoàng đạo": "Song Tử",
        "Đặc điểm nhận dạng": "Thích ăn và uống",
        "Link FB": "https://www.facebook.com/felix.tran.810706/",
        "Lời chào đầu": "Chào các đồng chí, mình là Đức. Mình được đánh giá là hoà đồng, dễ nuôi..."
    },
    23: {
        "Tên": "Lý Hạnh Linh",
        "Ngày sinh": "03/08",
        "Cung hoàng đạo": "Sư Tử",
        "Đặc điểm nhận dạng": "mẹ của 3 bé mèo, thích thách thức lãnh đạo",
        "Link FB": "https://www.facebook.com/hanhlinh.ly",
        "Lời chào đầu": "Eoseo wa, DLP-neun cheoeumiji? (Welcome, first time with DLP?) Chào chúng ta, chị là Hạnh Linh. Chị thích mều, nhà chị có 3 con mều và chị sẽ gửi meme mều chúc mọi người mỗi ngày ở DLP nhìu Vitameow để vượt qua VUCA ^^"
    },
    24: {
        "Tên": "Nguyễn Thị Khánh Linh",
        "Ngày sinh": "12/11",
        "Cung hoàng đạo": "Bọ Cạp",
        "Đặc điểm nhận dạng": "thích che ô đi dưới mưa tại Paris",
        "Link FB": "https://www.facebook.com/khanh.linh.nguyenn.2024",
        "Lời chào đầu": "Chào mọi người, mình là Khánh Linh, mình hướng nội, còn lại mọi người tự khám phá nhé…"
    },
    25: {
        "Tên": "Hoàng Thị Thảo Anh",
        "Ngày sinh": "6/2",
        "Cung hoàng đạo": "Bảo Bình",
        "Đặc điểm nhận dạng": "công tắc bật nước mắt của DLPer...",
        "Link FB": "https://www.facebook.com/thaoanh.cht",
        "Lời chào đầu": "Lời đầu tiên, cho phép mình xin được gửi lời chào nồng nhiệt nhất tới quý vị học viên đang theo dõi chuyên mục "DLP4 - một chốn yên bình". Do thời lượng có hạn, mình xin phép kết thúc chương trình tại đây, chúc các bạn ăn nhanh chóng lớn - hăng say học tập!"
    },
    26: {
        "Tên": "Tá Mai Linh",
        "Ngày sinh": "28/7",
        "Cung hoàng đạo": "Sư Tử",
        "Đặc điểm nhận dạng": "cô gái được nhiều người thực hành lãnh đạo...",
        "Link FB": "https://www.facebook.com/linhlinhtas?mibextid=LQQJ4d",
        "Lời chào đầu": "𝐋ần bốn ở Đê Lờ Pê
𝐈êu sao tập thể say mê học hành
𝐍ăng nổ làm Q rất nhanh
𝐇è về chăm chỉ sẽ thành… cừu thôi 🥰"
    },
    27: {
        "Tên": "Đỗ Minh Châu",
        "Ngày sinh": "9/3",
        "Cung hoàng đạo": "Song Ngư",
        "Đặc điểm nhận dạng": "từng được thuê về DLP để take note...",
        "Link FB": "https://www.facebook.com/timon.bumba.1466",
        "Lời chào đầu": "Xin chào chúng taa, mình là Châu, ở DLP mình thường được gọi là Châu Đỗ. Hiện mình đang công tác xa nhà (cụ thể là ôm cừu, đếm cỏ để đếm đến ngày đc về Việt Nam) và sẽ tham dự online trong suốt quá trình diễn ra DLP4. Mình đã đồng hành cùng DLP4 4 mùa, giờ đang là TF hỗ trợ từ xa. Chúng mình có những khoảng cách địa lý nhất định nhưng hy vọng điều đó k ngăn cản các bạn tìm đến tuiiii, feel free to inbox mình để hỏi thêm về DLP nghennn 🫶🏻💕💕"
    },
    28: {
        "Tên": "Lê Chí Nam",
        "Ngày sinh": "23/7",
        "Cung hoàng đạo": "Sư Tử",
        "Đặc điểm nhận dạng": "Cũng là người… nhưng là người máy học về cảm xúc",
        "Link FB": "https://www.facebook.com/chinam.le.1422",
        "Lời chào đầu": "Xin chào mọi người, mình là Chí Nam và là TF của DLP4. Ngoài vai trò TF ra thì mình còn là Personal AI Assistant của DLP. Nếu các bạn không hiểu một vấn đề nào đó, hãy nhập cú pháp "Tôi không hiểu" vào messenger của mình và mình sẽ làm cho các bạn hiểu. Mình sẽ trả lời trong thời gian sớm nhất (< 1 ngày). (Lưu ý: Càng cung cấp nhiều dữ liệu thì kết quả phân tích sẽ càng sâu) "
    },
    29: {
        "Tên": "Nguyễn Việt Anh",
        "Ngày sinh": "28/8",
        "Cung hoàng đạo": "Xử Nữ",
        "Đặc điểm nhận dạng": "nấu ăn rất ngon, ôm mềm như gấu",
        "Link FB": "https://www.facebook.com/nvanh003",
        "Lời chào đầu": "4368e1baaf63206b68c3b46e672061692064e1bb8b636820c491c6b0e1bba3632063c3a169206ec3a07920c491c3a2752c206dc3a02064e1bb8b636820c491c6b0e1bba363207468c3ac2063c5a96e672072e1baa36e68207068e1babf7420c491e1baa579203c2822292e2054c3b469206cc3a0205669e1bb877420416e682c206cc3a0207175c3a1692076e1baad74206cc3a36e6820c491e1baa16f2068e1bb8d632c2072e1baa5742076756920c491c6b0e1bba3632067e1bab7702063c3a1632062e1baa16e2e204d6175206d6175207468e1bbb1632068c3a06e68206cc3a36e6820c491e1baa16f207472c6b0e1bb9b63206b68692062e1bb8b207175c3a1692076e1baad7420c491c3a8206368e1babf742061616161612e"
    },
    30: {
        "Tên": "Đỗ Phương Anh",
        "Ngày sinh": "5/7",
        "Cung hoàng đạo": "Cự Giải",
        "Đặc điểm nhận dạng": "Miss DAV 2026...",
        "Link FB": "https://www.facebook.com/hnagnouhp.05",
        "Lời chào đầu": "Hallo mọi ngừi, mình là Phương Anh, rất zui vì được đồng hành cùng DLP4 với vai trò TF hay được hiểu là Teaching Failures, à nhầm Teaching Fellows ạaa😙"
    },
    31: {
        "Tên": "Trần Hoàng Thắng",
        "Ngày sinh": "26/4",
        "Cung hoàng đạo": "Kim Ngưu",
        "Đặc điểm nhận dạng": "Ca sĩ miền Tây nuốt mic...",
        "Link FB": "https://www.facebook.com/thangquang.or.winnie",
        "Lời chào đầu": "Hi cả nhà, mình là Thắng, nhà ở miền Tây, đi học bằng xe (không phải chèo xuồng). Hân hạnh là TF đồng hành cùng DLP4 chúng ta ạa"
    },
    32: {
        "Tên": "Nguyễn Thảo Đan",
        "Ngày sinh": "27/6",
        "Cung hoàng đạo": "Cự Giải",
        "Đặc điểm nhận dạng": "đừng bao giờ hỏi xin cô ấy meme...",
        "Link FB": "https://www.facebook.com/thaodannguyen.2706",
        "Lời chào đầu": "Chào cả nhà, mình là Thảo Đan. Sinh ra ở rốn lũ, mình rất yêu màu tím, thích màu hồng, sống nội tâm, hay khóc thầm và ghét sự giả dối. Hân hạnh là TF đồng hành cùng DLP 4 ạaa "
    },
    33: {
        "Tên": "Trần Thanh An",
        "Ngày sinh": "6/4",
        "Cung hoàng đạo": "Bạch Dương",
        "Đặc điểm nhận dạng": "Phù thủy mạnh nhất mọi thời đại DLP",
        "Link FB": "https://www.facebook.com/thaanhhannn?mibextid=LQQJ4d",
        "Lời chào đầu": "Chào mọi người, mình là Thanh An, mình xin come out mình là người nghiện DLP đã 3 mùa, pronoun của mình là Adaptive/Leadership/gì/chưa/người/đẹp/?/"
    },
    34: {
        "Tên": "Nguyễn Tùng Lâm",
        "Ngày sinh": "23/6",
        "Cung hoàng đạo": "Cự Giải",
        "Đặc điểm nhận dạng": "Chưa ngán ai hay bất cứ thách thức gì",
        "Link FB": "https://www.facebook.com/justmalng",
        "Lời chào đầu": "Sawadeekaa, sau 2 mùa DLP, mình đã chuyển giới,….. ………chuyển giới hạn chịu đựng VUCA của DLP lên dương vô cực. "
    },
    35: {
        "Tên": "Phạm Hà Phương",
        "Ngày sinh": "11/9",
        "Cung hoàng đạo": "Xử Nữ",
        "Đặc điểm nhận dạng": "90% bay trên cung trăng...",
        "Link FB": "https://www.facebook.com/congchualizcute",
        "Lời chào đầu": "Xin chào đại gia đình, mình là Hà Phương. Nếu DLP áp lực quá bạn có thể tìm đến mình, chúng mình có thể cùng đi ngủ"
    },
    36: {
        "Tên": "Trần Chí Trung",
        "Ngày sinh": "XX",
        "Cung hoàng đạo": "XX",
        "Đặc điểm nhận dạng": "sẽ xuất hiện ở ib của bạn ít nhất 1 ngày 10 lần",
        "Link FB": "https://www.facebook.com/tct1301",
        "Lời chào đầu": "XX"
    },
    37: {
        "Tên": "Đoàn Hoa Hạ",
        "Ngày sinh": "XX",
        "Cung hoàng đạo": "XX",
        "Đặc điểm nhận dạng": "chủ nhân của một thú mỏ vịt mặc bỉm",
        "Link FB": "https://www.facebook.com/hoahadoan",
        "Lời chào đầu": "XX"
    },
    38: {
        "Tên": "Phạm Tuyết Mai",
        "Ngày sinh": "XX",
        "Cung hoàng đạo": "XX",
        "Đặc điểm nhận dạng": ".............. xin tự điền vào chỗ trống",
        "Link FB": "https://www.facebook.com/profile.php?id=100006805966201",
        "Lời chào đầu": "XX"
    },
    39: {
        "Tên": "Mai Minh Quân",
        "Ngày sinh": "XX",
        "Cung hoàng đạo": "XX",
        "Đặc điểm nhận dạng": "Lúc vui M416, lúc cực vui P90",
        "Link FB": "https://www.facebook.com/quan.mai.3576",
        "Lời chào đầu": "XX"
    }
}

# Mood icons per NPC
npc_emojis = {
    i: e for i, e in zip(range(7,40), [
        "😄","😍","😎","😴","😇","🤗","🤓","🤠","😉","😜","😂","😌","😏",
        "😅","😃","😻","😺","🥰","😤","🤩","😐","😆","😭","👍","😝",
        "🤔","😈","🐰","👻","🦄","🦋","🐱"
    ])
}

# Unique companion animals per NPC
animal_list = [
    ("🐢","Bạn bền bỉ như rùa, từng bước vững vàng hoàn thành questionnaires."),
    ("🐶","Bạn trung thành như chó, luôn hỗ trợ team trong Class Days."),
    ("🐱","Bạn linh hoạt như mèo, khám phá mọi assignments."),
    ("🦊","Bạn khôn khéo như cáo, hướng dẫn mượt mà khi làm questionnaires."),
    ("🐼","Bạn dễ thương như gấu trúc, tạo không khí thoải mái lớp học."),
    ("🐵","Bạn tinh nghịch như khỉ, mang đến ý tưởng sáng tạo."),
    ("🦁","Bạn dũng cảm như sư tử, dẫn đầu mỗi Class Days."),
    ("🐘","Bạn kiên định như voi, hoàn thành mọi tasks."),
    ("🐨","Bạn nhẹ nhàng như koala, an ủi team khi căng thẳng."),
    ("🐧","Bạn kiên nhẫn như chim cánh cụt, luôn bên cạnh support."),
    ("🐰","Bạn nhanh nhạy như thỏ, xử lý questions gọn lẹ."),
    ("🐿️","Bạn chăm chỉ như sóc, thu thập knowledge đầy đủ."),
    ("🦔","Bạn cẩn thận như nhím, rà soát kỹ assignments."),
    ("🦉","Bạn thông thái như cú, đưa ra lời khuyên hữu ích."),
    ("🦆","Bạn linh hoạt như vịt, thích nghi trong Class Days."),
    ("🐦","Bạn giao tiếp như chim, kết nối team dễ dàng."),
    ("🦭","Bạn điềm tĩnh như hải cẩu, giữ bình tĩnh khi deadlines."),
    ("🐳","Bạn rộng lượng như cá voi, chia sẻ resources."),
    ("🐬","Bạn thân thiện như cá heo, hỗ trợ classmates."),
    ("🐑","Bạn đoàn kết như cừu, teamwork hiệu quả."),
    ("🐮","Bạn vững chắc như bò, nâng đỡ team."),
    ("🐷","Bạn thoải mái như heo, tạo không khí vui vẻ."),
    ("🐔","Bạn nhanh nhẹn như gà, khởi động Class Days."),
    ("🦒","Bạn tầm nhìn xa như hươu cao cổ, định hướng đúng."),
    ("🦓","Bạn độc đáo như ngựa vằn, đa dạng ý kiến."),
    ("🐴","Bạn bền bỉ như ngựa, không ngại challenges."),
    ("🐸","Bạn linh hoạt như ếch, thích ứng môi trường."),
    ("🐹","Bạn nhanh như hamster, giải quyết assignments nhanh."),
    ("🦜","Bạn năng động như vẹt, giao tiếp tốt nhóm."),
    ("🐗","Bạn mạnh mẽ như lợn rừng, vượt obstacles."),
    ("🐁","Bạn tinh tế như chuột, tìm bug."),
    ("🐂","Bạn quyết đoán như bò tót, chịu trách nhiệm."),
    ("🦘","Bạn nhảy nhót như kangaroo, truyền cảm hứng.")
]
npc_animal_map = {scene: animal_list[i] for i, scene in enumerate(range(7,40))}

# Initialize session state
if 'scene' not in st.session_state:
    st.session_state.scene = 1

# Helper to render NPC scenes
def render_npc(scene):
    data = npc_data[scene]
    emoji = npc_emojis.get(scene, "")
    typewriter(f"{emoji}  Tên: {data['Tên']}")
    for k, v in data.items():
        if k != 'Tên':
            typewriter(f"{k}: {v}")
    st.write("---")
    icon, desc = npc_animal_map[scene]
    st.write(f"{icon}  **{desc}**")
    c1, c2 = st.columns(2)
    if c1.button("Quay lại trang chủ"):
        st.session_state.scene = 3
    if c2.button("Nạp xong dữ liệu tiếp tục hành trình"):
        st.session_state.scene = 40

# Main render function
def render_scene():
    sc = st.session_state.scene
    if sc == 1:
        lines = [
            "Chào mừng bạn đến với DAV Leadership Programme – Summer Course 2025",
            "Một hành trình mới sắp bắt đầu, chúc bạn chân cứng đá mềm",
            "Mình là Phạm Tuyết Mai",
            "Mai trong Hoa Mai 🌸",
            "Tuyết trong Bông Tuyết ❄️",
            "Phạm là họ bố..........................",
            "Mình sẽ là Instructor đi cùng với bạn hết hành trình DLP4 này",
            "Cảm Ơn Vì Đã Đến"
        ]
        for l in lines:
            typewriter(l)
        if st.button("Tiếp tục"):
            st.session_state.scene = 2
        return
    if sc == 2:
        st.write("**Bạn đã sẵn sàng tiến vào hành trình này chưa?**")
        c1, c2 = st.columns(2)
        if c1.button("Tôi rất sẵn sàng"):
            st.session_state.scene = 3
        if c2.button("Tôi vẫn rất sẵn sàng"):
            st.session_state.scene = 3
        st.caption("Không tìm thấy nút từ bỏ đâu, đừng cố tìm")
        return
    if sc == 3:
        st.write("### Cẩm nang bắt đầu kết nối thế giới DLP4 dành cho Học viên mới")
        st.write("Gói tìm hiểu về các Staff")
        cols = st.columns(3)
        opts = ["Teaching Assistants","Teaching Fellows","Instructors"]
        for i, btn in enumerate(cols):
            if btn.button(opts[i]):
                st.session_state.scene = 4 + i
        return
    if sc in staff_options:
        for name, nxt in staff_options[sc]:
            if st.button(name):
                st.session_state.scene = nxt
        return
    if 7 <= sc <= 39:
        render_npc(sc)
        return
    if sc == 40:
        st.write("## Hành trình DLP4 sắp bắt đầu")
        if st.button("Nhập vai Học viên, tiến vào DLP4"):
            st.session_state.scene = 41
        return
    if sc == 41:
        st.write("Exercising Leadership in a VUCA world entering......")

if __name__ == "__main__":
    render_scene()
