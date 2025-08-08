from fastapi import APIRouter, File
from src.utils.log import setup_logger
from src.ocr.paddle_ocr import ocr_predict
import numpy as np
import cv2

logger = setup_logger(__name__)

router = APIRouter()


@router.post("/recognize", summary="OCR Recognition")
async def recognize_ocr(file: bytes = File()):
    logger.info(f"file size {len(file)}")

    # 将字节数据转换为numpy数组
    nparr = np.frombuffer(file, np.uint8)

    # 使用OpenCV解码图像
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # 转换为RGB格式（OpenCV默认是BGR）
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    text_list = ocr_predict(image)
    return {"code": 200, "msg": "操作成功", "data": {"result": text_list}}
