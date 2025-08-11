from paddleocr import PaddleOCR
from pathlib import Path
from src.utils.log import setup_logger

logger = setup_logger(__name__)

detection_model_dir = Path(__file__).parent.parent / "models" / "PP-OCRv5_mobile_det_infer"
recognition_model_dir = Path(__file__).parent.parent / "models" / "PP-OCRv5_mobile_rec_infer"
logger.info(f"Detection model dir: {detection_model_dir}")
logger.info(f"Recognition model dir: {recognition_model_dir}")

ocr = PaddleOCR(
    # device="cpu",  # 通过 device 参数指定使用 CPU 设备
    use_doc_orientation_classify=False,  # 通过 use_doc_orientation_classify 参数指定不使用文档方向分类模型
    use_doc_unwarping=False,  # 通过 use_doc_unwarping 参数指定不使用文本图像矫正模型
    use_textline_orientation=False,  # 通过 use_textline_orientation 参数指定不使用文本行方向分类模型
    text_detection_model_name="PP-OCRv5_mobile_det",
    text_detection_model_dir=detection_model_dir.as_posix(),
    text_recognition_model_name="PP-OCRv5_mobile_rec",
    text_recognition_model_dir=recognition_model_dir.as_posix(),
)


def ocr_predict(file: str):
    """Predict text in an image or PDF file using PaddleOCR."""
    output = ocr.predict(file)
    result = output[0]['rec_texts']
    logger.info(f"OCR output: {result}")
    return result
