import os
import logging
import time

def create_path(parentpath,dirname):
    d = os.path.join(parentpath,dirname)
    if not os.path.exists(d):
        os.mkdir(d)
    return d

def get_root_path(dirname):
    d = os.path.dirname(__file__)
    d = os.path.dirname(d)
    return create_path(d,dirname)


def get_temp_path():
    return get_root_path('TEMP')

def get_save_path_pictrue(fileName):
    d = get_temp_path()
    d = create_path(d,'PICTRUE')
    return os.path.join(d,fileName)

def get_save_path_log(fileName):
    d = get_temp_path()
    d = create_path(d,'log')
    return os.path.join(d,fileName)

def get_save_path_images(fileName):
    d = get_temp_path()
    d = create_path(d,'images')
    return os.path.join(d,fileName)

def save_url_to_file(url):
    try:
        with open(get_save_path_images('images_url.txt'),"a",encoding="utf-8") as f:
            f.write(url)
            f.write("\n")
    except FileNotFoundError as fnf_error:
        logging.warn(fnf_error)
    finally:
        logging.info('save_url_to_file finished')

def init_log(need_print=False):
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"    # 日志格式化输出
    DATE_FORMAT = "%Y/%d/%m %H:%M:%S %p"                        # 日期格式
    log_file_name='{}.log'.format(time.strftime("%Y%m%d%H%M%S", time.localtime()))
    log_path=get_save_path_log(log_file_name)
    fp = logging.FileHandler(log_path, encoding='utf-8')
    fs = logging.StreamHandler()

    if need_print is True:
        logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT, handlers=[fp, fs])    # 调用 
    else:
        logging.basicConfig(level=logging.INFO, format=LOG_FORMAT, datefmt=DATE_FORMAT, handlers=[fp])    # 调用 
        
    logging.info("log_file_name={}".format(log_file_name))

def check_str_list(obj_list):
    for obj in obj_list:
        if type(obj) is not str:
            return False
    return True

if __name__ == "__main__":
    texts=get_save_path_log('vatInvoice01.jpeg')
    print(type(texts))
    print(texts)