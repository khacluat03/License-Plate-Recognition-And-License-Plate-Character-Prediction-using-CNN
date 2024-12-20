import matplotlib.pyplot as plt
import cv2
import numpy as np


def preprocess_image(image_path, input_size=200):
    """
    Đọc và chuẩn bị ảnh đầu vào cho mô hình.

    Args:
        image_path (str): Đường dẫn tới ảnh.
        input_size (int): Kích thước đầu vào của mô hình.

    Returns:
        numpy.ndarray: Ảnh đã được chuẩn hóa và resize.
        tuple: Kích thước gốc của ảnh (height, width).
    """
    image = cv2.imread(image_path)
    original_size = image.shape[:2]  # Lưu kích thước gốc (height, width)
    image_resized = cv2.resize(image, (input_size, input_size))
    image_normalized = image_resized / 255.0  # Chuẩn hóa về [0, 1]
    return image_normalized, original_size


def predict_bounding_box(image, model, original_size):
    """
    Dự đoán bounding box trên một ảnh duy nhất.

    Args:
        image (numpy.ndarray): Ảnh đã được chuẩn hóa và thay đổi kích thước.
        model (keras.Model): Mô hình CNN đã được huấn luyện.
        original_size (tuple): Kích thước gốc của ảnh (height, width).

    Returns:
        tuple: Bounding box dự đoán (xmin, ymin, xmax, ymax).
    """
    original_height, original_width = original_size

    # Dự đoán bounding box # Output: [xmin, ymin, xmax, ymax]
    pred_bbox = model.predict(np.expand_dims(image, axis=0))[0]

    # Chuyển bounding box về kích thước gốc của ảnh
    xmin = int(pred_bbox[0] * original_width)
    ymin = int(pred_bbox[1] * original_height)
    xmax = int(pred_bbox[2] * original_width)
    ymax = int(pred_bbox[3] * original_height)

    return (xmin, ymin, xmax, ymax)


def visualize_prediction(image_path, bbox):
    """
    Hiển thị ảnh cùng với bounding box dự đoán.

    Args:
        image_path (str): Đường dẫn tới ảnh gốc.
        bbox (tuple): Bounding box (xmin, ymin, xmax, ymax).
    """
    image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    plt.imshow(image_rgb)
    plt.gca().add_patch(plt.Rectangle(
        (bbox[0], bbox[1]),                # xmin, ymin
        bbox[2] - bbox[0],                 # width
        bbox[3] - bbox[1],                 # height
        fill=False, edgecolor="red", linewidth=2, label="Prediction"
    ))
    plt.legend()
    plt.axis("on")
    # plt.title("Prediction")
    plt.savefig('D:\\Python_Code\\PYTHON_Nam4_HK1\\ANPR\\output\\image\\output.png', dpi=300, bbox_inches='tight')

    plt.show()


# def visualize_prediction_video(image_path, bbox):
#     """
#     Hiển thị ảnh cùng với bounding box dự đoán.

#     Args:
#         image_path (str): Đường dẫn tới ảnh gốc.
#         bbox (tuple): Bounding box (xmin, ymin, xmax, ymax).
#     """
#     image = cv2.imread(image_path)
#     image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#     plt.imshow(image_rgb)
#     plt.gca().add_patch(plt.Rectangle(
#         (bbox[0], bbox[1]),                # xmin, ymin
#         bbox[2] - bbox[0],                 # width
#         bbox[3] - bbox[1],                 # height
#         fill=False, edgecolor="red", linewidth=2, label="Prediction"
#     ))
#     plt.legend()
#     plt.axis("on")
#     # plt.title("Prediction")
#     plt.savefig('output\\output.png', dpi=300, bbox_inches='tight')

#     plt.show()
