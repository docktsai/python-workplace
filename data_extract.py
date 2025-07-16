import logging

from common_functions import com_function1

data_extract_logger = logging.getLogger("data_extract")

def setup_data_extract_logger(rpt_name:str):
    global data_extract_logger
    stream_handler = logging.StreamHandler()
    file_handler = logging.FileHandler(f"/Users/docktsai/Documents/GitHub/python-workplace/log/data_extract_{rpt_name}.log")
    formater = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    stream_handler.setFormatter(formater)
    # stream_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formater)

    data_extract_logger.addHandler(stream_handler)
    data_extract_logger.addHandler(file_handler)
    data_extract_logger.setLevel(logging.DEBUG)

def data_extract(rpt_name:str):
    print("======= test logging =======")
    data_extract_logger.debug(" This is logging for Debug")
    data_extract_logger.error(" This is logging for Error")
    data_extract_logger.info(" This is logging for info")
    print("======= test common logging =======")
    com_function1()
    

if __name__ == "__main__":
    rpt_name = "CF_Test_1"
    setup_data_extract_logger(rpt_name)
    data_extract(rpt_name)


