from paddleocr import PaddleOCR


def ocr_predict(file_path: str):
    """Predict text in an image or PDF file using PaddleOCR."""
    ocr = PaddleOCR(
        device="cpu",  # 通过 device 参数指定使用 CPU 设备
        use_doc_orientation_classify=False,  # 通过 use_doc_orientation_classify 参数指定不使用文档方向分类模型
        use_doc_unwarping=False,  # 通过 use_doc_unwarping 参数指定不使用文本图像矫正模型
        use_textline_orientation=False,  # 通过 use_textline_orientation 参数指定不使用文本行方向分类模型
        text_detection_model_name="PP-OCRv5_mobile_det",
        text_detection_model_dir="./models/PP-OCRv5_mobile_det_infer",
        text_recognition_model_name="PP-OCRv5_mobile_rec",
        text_recognition_model_dir="./models/PP-OCRv5_mobile_rec_infer",
    )
    output = ocr.predict(file_path)
    for res in output:
        res.print()
        res.save_to_img(save_path="../output/")
        res.save_to_json(save_path="../output/res.json")
