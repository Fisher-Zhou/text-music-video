import logging
from pathlib import Path
from ..config import LOG_DIR, LOG_LEVEL

def setup_logger(name, log_file=None, level=None):
    """
    设置日志记录器
    :param name: 日志记录器名称
    :param log_file: 日志文件路径，如果为None则使用默认路径
    :param level: 日志级别，如果为None则使用配置中的级别
    :return: 配置好的日志记录器
    """
    if log_file is None:
        log_file = LOG_DIR / f"{name}.log"
    
    if level is None:
        level = getattr(logging, LOG_LEVEL.upper())

    # 创建日志记录器
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # 创建文件处理器
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setLevel(level)

    # 创建控制台处理器
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)

    # 创建格式化器
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # 添加处理器
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger 