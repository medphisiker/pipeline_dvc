import os
import time


if __name__ == "__main__":
    # Имя файла, в который будем записывать данные
    filename = "data/task1_output.txt"

    os.system("nvidia-smi")

    with open(filename, "w") as file:
        for i in range(10):
            line = f"{i}\n"
            file.write(line)
            print(line)
            file.flush()

            # Ждем одну секунду
            time.sleep(1)
