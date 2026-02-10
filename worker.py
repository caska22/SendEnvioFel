import time
import logging
import sys


from c_factorial import Factorial

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def main():
    logging.info("Servicio Python iniciado")
    logging.critical("muu")
    while True:
        logging.info("Procesandol")
        factorial = Factorial()
        factorial.hello()
        time.sleep(1000)





if __name__ == "__main__":
    main()
