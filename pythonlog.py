import logging
import datetime
import random
#pip install logging
def configurar_logger():
    logging.basicConfig(filename='log.tmp', level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(message)s')

def gerar_numeros():
    numeros = [random.randint(1, 50) for _ in range(50)]
    return numeros

def main():
    configurar_logger()

    # Obtém a data e hora atual
    data_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logging.debug(f'Data e Hora: {data_hora}')

    # Gera e loga os números
    numeros = gerar_numeros()
    for numero in numeros:
        logging.debug(f'Número: {numero}')


print("\x1bc\x1b[43;30mstart application:")

if __name__ == "__main__":
    main()

