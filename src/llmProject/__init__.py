
import os
import logging
import sys

logging_str = "[%(asctime)s : %(levelname)s: %(message)s]"

log_dir = "logs"
log_file = "running_logs.log"
log_filepath = os.path.join(log_dir, log_file)
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("mlProjectLogger")
