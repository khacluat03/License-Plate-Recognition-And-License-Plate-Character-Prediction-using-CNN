> Note: Vietnamese first and English below
<h1 align="center"> Phát hiện biển số xe và dự đoán kí tự trên biển số xe </h2>

### Cần cài đặt các môn trường và thư viện trước khi sử dụng: `Python`, `cv2`, `tensorflow`, `matplotlib`. Nếu máy báo lỗi hãy sử dụng lệnh `pip install <thư viện thiếu>` để cài đặt.

### Cách sử dụng:

- Sử dụng file `Code_Demo_On_Local_Machine.ipynb` trong thư mục `notebook` để sử dụng và chạy thử với máy local.
  Hãy nhớ tải các mô hình trong thư mục model.
- Hãy tham khảo các notebook Train_Model... để đào tạo mô hình với dữ liệu của bạn.
- Các bộ dataset kèm theo, bạn có thể tham khảo trên mô hình của bạn:
  - Bộ dataset nhận diện biển số xe: [LINK](https://1drv.ms/f/c/131c537c95a10340/EmLMfz6nW55JqqGLO4BTZMcB4ooYr3uPofO46sWlmY4QEg?e=zkOHgh)

### Các bước chính được dùng trong bài toán này:

<p align="center"><img src="https://raw.githubusercontent.com/khacluat03/License-Plate-Recognition-And-License-Plate-Character-Prediction/refs/heads/master/image.png" width="300"></p>

---

## Mô tả ý tưởng các bước:

### Bước 1:
Sử dụng model đã train từ notebook `Train_Model_Detect_Plate_With_Data_Augmentation.ipynb` hay `Train_Model_Detect_Plate_With_Original_Data.ipynb` hoặc có thể sử dụng model mà tôi đã train trong thư mục model (mô tả trong file README.md trong thư mục model) để nhận diện biển số xe
### Bước 2:
Dùng các bouding box đã nhận diện biển số, sau đó cắt lưu thành ảnh mới và đưa vào mô hình dự đoán kí tự
### Bước 3:
Dùng mô hình dự đoán kí tự để dự đoán và trực quan kết quả bằng matplotlib.

> BÀI CỦA TÔI CHỈ LÀ THAM KHẢO, HÃY CẢI TIẾN CÁC MÔ HÌNH VÀ CÁCH LÀM MỚI NHÉ!!! CHÚC BẠN THÀNH CÔNG!!!

---

<h1 align="center"> Detecting license plates and predicting characters on license plates </h2>

### You need to install the following subjects and libraries before using: `Python`, `cv2`, `tensorflow`, `matplotlib`. If the machine reports an error, use the command `pip install <missing library>` to install.

### How to use:

- Use the file `Code_Demo_On_Local_Machine.ipynb` in the `notebook` folder to use and test with the local machine.

Remember to download the models in the model folder.

- Refer to the Train_Model... notebooks to train the model with your data.

- The attached datasets, you can refer to your model:

- License plate recognition dataset: [LINK](https://1drv.ms/f/c/131c537c95a10340/EmLMfz6nW55JqqGLO4BTZMcB4ooYr3uPofO46sWlmY4QEg?e=zkOHgh)

### Main steps used in this problem:

<p align="center"><img src="https://raw.githubusercontent.com/khacluat03/License-Plate-Recognition-And-License-Plate-Character-Prediction/refs/heads/master/image.png" width="300"></p>

---

# Description of the idea of ​​the steps:

### Step 1:
Use the trained model from the notebook `Train_Model_Detect_Plate_With_Data_Augmentation.ipynb` or `Train_Model_Detect_Plate_With_Original_Data.ipynb` or you can use the model that I trained in the model folder (described in the README.md file in the model folder) to recognize the license plate
### Step 2:
Use the bounding boxes that have recognized the license plate, then crop and save them as new images and put them into the character prediction model
### Step 3:
Use the character prediction model to predict and visualize the results with matplotlib.

> MY POST IS ONLY FOR REFERENCE, IMPROVE THE MODELS AND NEW METHODS!!! GOOD LUCK!!!