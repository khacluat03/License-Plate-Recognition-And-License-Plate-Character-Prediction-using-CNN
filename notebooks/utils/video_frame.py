import cv2
import os

def extract_frames(video_path, output_dir):
    """
    Tách các frame từ video và lưu vào thư mục chỉ định.

    Args:
        video_path (str): Đường dẫn tới file video.
        output_dir (str): Thư mục để lưu các frame.

    Returns:
        int: Số lượng frame được tách ra.
    """
    # Tạo thư mục lưu frame nếu chưa có
    os.makedirs(output_dir, exist_ok=True)

    # Mở video
    cap = cv2.VideoCapture(video_path)
    frame_count = 0

    # Lặp qua từng frame trong video
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Tên file cho mỗi frame
        frame_filename = os.path.join(output_dir, f'frame_{frame_count:03d}.jpg')

        # Lưu frame dưới dạng ảnh JPG
        cv2.imwrite(frame_filename, frame)

        frame_count += 1

    # Giải phóng video
    cap.release()
    print(f"Đã tách {frame_count} frame và lưu trong thư mục '{output_dir}'")
    return frame_count

def create_video_from_frames(frame_dir, output_video_path, fps=30):
    """
    Tạo video từ các frame trong một thư mục.

    Parameters:
        frame_dir (str): Đường dẫn thư mục chứa các frame.
        output_video_path (str): Đường dẫn tệp video đầu ra.
        fps (int): Số khung hình trên giây (mặc định là 30).

    Raises:
        ValueError: Nếu không tìm thấy frame nào trong thư mục.
    """
    # Các định dạng ảnh được hỗ trợ
    supported_formats = ('.jpg', '.png')

    # Lấy danh sách file ảnh trong thư mục
    frame_files = sorted([
        os.path.join(frame_dir, f)
        for f in os.listdir(frame_dir)
        if f.endswith(supported_formats)
    ])

    # Đảm bảo danh sách frame không rỗng
    if not frame_files:
        raise ValueError("Không tìm thấy frame nào trong thư mục!")

    # Đọc frame đầu tiên để lấy kích thước video
    first_frame = cv2.imread(frame_files[0])
    if first_frame is None:
        raise ValueError(
            "Không thể đọc frame đầu tiên. Hãy kiểm tra đường dẫn và định dạng file.")

    height, width, layers = first_frame.shape

    # Định nghĩa codec và tạo VideoWriter
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec cho định dạng MP4
    video_writer = cv2.VideoWriter(
        output_video_path, fourcc, fps, (width, height))

    # Ghi từng frame vào video
    for frame_file in frame_files:
        frame = cv2.imread(frame_file)
        if frame is not None:
            video_writer.write(frame)
        else:
            print(
                f"Warning: Không thể đọc frame '{frame_file}', bỏ qua frame này.")

    # Giải phóng tài nguyên
    video_writer.release()
    print(f"Video đã được tạo tại '{output_video_path}'")