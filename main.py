from paddleocr import PaddleOCR

# test_file = "./test/1.png"
test_file = "./test/1.pdf"


def main():
    # model = TextDetection(model_name="PP-OCRv5_mobile_det", model_dir="./models/PP-OCRv5_mobile_det_infer")
    # model = TextRecognition(model_name="PP-OCRv5_mobile_rec", model_dir="./models/PP-OCRv5_mobile_rec_infer")
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
    output = ocr.predict(test_file)
    for res in output:
        res.print()
        res.save_to_img(save_path="./output/")
        res.save_to_json(save_path="./output/res.json")


if __name__ == "__main__":
    main()
