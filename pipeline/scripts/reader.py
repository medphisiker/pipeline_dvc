import os
import time


if __name__ == "__main__":
    # Имя файла, из которого будем читать данные
    input_txt = "data/task1_output.txt"
    output_txt = "data/task2_output.txt"

    os.system("nvidia-smi")

    with open(input_txt, "r") as input_file, open(output_txt, "w") as output_file:
        # Читаем файл построчно
        for line in input_file:
            number = int(line.strip())
            doubled_number = number * 2

            print(doubled_number)
            output_file.write(f"{doubled_number}\n")
            output_file.flush()

            # Ждем одну секунду
            time.sleep(1)
