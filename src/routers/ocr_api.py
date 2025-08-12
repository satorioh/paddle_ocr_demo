import numpy as np
import cv2
import time
from fastapi import APIRouter, UploadFile
from src.utils.log import setup_logger
from src.ocr.paddle_ocr import ocr_predict
from pdf2image import convert_from_bytes

logger = setup_logger(__name__)

router = APIRouter()


@router.post("/recognize", summary="OCR Recognition")
async def recognize_ocr(file: UploadFile):
    content_type = file.content_type
    file_content = await file.read()

    logger.info(f"file size {len(file_content)}, content_type: {content_type}")
    start_time = time.time()

    if content_type == "application/pdf":
        # 直接从二进制数据转换PDF为图像列表
        images = convert_from_bytes(file_content)
        logger.info(f"PDF converted to {len(images)} pages")

        # 对每个页面进行OCR并合并结果
        all_text = []
        for img in images:
            # 将PIL图像转换为numpy数组
            img_np = np.array(img)

            # 对当前页面进行OCR
            page_text = ocr_predict(img_np)
            all_text.extend(page_text)

        elapsed_time = time.time() - start_time
        logger.info(f"PDF处理耗时: {elapsed_time:.3f}秒")
        return {"code": 200, "msg": "操作成功", "data": {"result": all_text}}
    else:
        # 处理图像文件
        np_arr = np.frombuffer(file_content, np.uint8)
        image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        text_list = ocr_predict(image)
        elapsed_time = time.time() - start_time
        logger.info(f"图像处理耗时: {elapsed_time:.3f}秒")
        return {"code": 200, "msg": "操作成功", "data": {"result": text_list}}
