<h2 align="center">MÔ TẢ</h2>

---
> Link models: [Link](https://1drv.ms/f/c/131c537c95a10340/Epe07KnXpIZNtjTJJGASA3oBbwxY-m2oajqsKaRWh7bSOg?e=YzwE7I)

Thông tin chi tiết về các mô hình được đào tạo từ dữ liệu liên quan đến dự đoán ký tự và biển số xe. Các mô hình được lưu trữ dưới các tệp .h5 và được thiết kế để phục vụ các bài toán nhận diện ký tự và biển số xe.

1. `license_plate_model.h5`
    - Mục đích: Dự đoán toàn bộ biển số xe từ hình ảnh với dữ liệu gốc chưa qua tăng cường.
    - Dữ liệu: Tập dữ liệu ảnh biển số xe thực tế, chưa áp dụng các kỹ thuật tăng cường dữ liệu.
    - Ứng dụng: Tự động nhận diện biển số xe từ ảnh chụp.

2. `license_plate_model_2.h5`
    - Mục đích: Dự đoán toàn bộ biển số xe từ hình ảnh với dữ liệu đã được tăng cường.
    - Dữ liệu: Tập dữ liệu đã áp dụng các kỹ thuật tăng cường (augmentation) như xoay, cắt, và thay đổi độ sáng để cải thiện độ chính xác trong các điều kiện khác nhau.
    - Ứng dụng: Nhận diện biển số xe trong các điều kiện phức tạp, bao gồm ánh sáng kém hoặc góc chụp khác thường.
3. `char_model_01.h5`
    - Mục đích: Dự đoán các ký tự trong hình ảnh, hỗ trợ nhận diện từng ký tự riêng lẻ.
    - Dữ liệu: Tập dữ liệu chứa các hình ảnh ký tự (chữ cái và số) được tiền xử lý để tối ưu hóa quá trình huấn luyện.
    - Ứng dụng: Nhận diện ký tự trong biển số xe hoặc các bài toán tương tự.
### Hướng dẫn sử dụng
- Môi trường cần thiết:
    - Python >= 3.8
    - TensorFlow >= 2.5
- Cách tải mô hình:
```bash
from tensorflow.keras.models import load_model

char_model = load_model('char_model_01.h5')
license_plate_model = load_model('license_plate_model.h5')
license_plate_model_2 = load_model('license_plate_model_2.h5')
```

----

<h2 align="center">DESCRIPTION</h2>
---
Details about the models trained from data related to character and license plate prediction. The models are stored in .h5 files and are designed to serve the character and license plate recognition problems.

1. `license_plate_model.h5`
- Purpose: Predict all license plates from images with raw data without augmentation.

- Data: Real license plate image dataset, without applying data augmentation techniques.

- Application: Automatically recognize license plates from photos.

2. `license_plate_model_2.h5`
- Purpose: Predict all license plates from images with augmentation data.
- Data: The dataset has applied augmentation techniques such as rotation, cropping, and illumination changes to improve accuracy in different conditions.

- Application: License plate recognition in complex conditions, including poor lighting or unusual shooting angles.

3. `char_model_01.h5`
- Purpose: Predict characters in images, supporting the recognition of individual characters.

- Data: The dataset contains preprocessed character images (letters and numbers) to optimize the training process.

- Application: License plate character recognition or similar problems.

### How to use
- Required environment:
    - Python >= 3.8
    - TensorFlow >= 2.5
- How to load the model:
```bash
from tensorflow.keras.models import load_model

char_model = load_model('char_model_01.h5')
license_plate_model = load_model('license_plate_model.h5')
license_plate_model_2 = load_model('license_plate_model_2.h5')
```