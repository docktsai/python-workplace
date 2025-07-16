from data_extract import data_extract,setup_data_extract_logger
from common_functions import com_function2
import logging

main_logger = logging.getLogger("main")
stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler("/Users/docktsai/Documents/GitHub/python-workplace/log/main.log")
formater = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
stream_handler.setFormatter(formater)
file_handler.setFormatter(formater)

# main_logger.addHandler(stream_handler)
main_logger.addHandler(file_handler)
main_logger.setLevel(logging.DEBUG)


def main():
    print("-------- test from main -------")
    main_logger.info(" ============= start calling data_extract =================")
    rpt_name = "CF_Test_22"
    setup_data_extract_logger(rpt_name)
    data_extract(rpt_name)
    main_logger.info(" ============= start calling com_function2 =================")
    com_function2()

    main_logger.info(" ============= end testing =================")


if __name__ == "__main__":
    main()
