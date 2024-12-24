import os
import time
import torch


if __name__ == "__main__":
    # Имя файла, в который будем записывать данные
    filename = "data/task1_output.txt"

    os.system("nvidia-smi")
    print("torch.__version__", torch.__version__)
    print("torch.cuda.is_available()", torch.cuda.is_available())
    print("torch.cuda.current_device()", torch.cuda.current_device())
    print("torch.cuda.device_count()", torch.cuda.current_device())
    print("torch.cuda.get_device_name(0)", torch.cuda.get_device_name(0))

    with open(filename, "w") as file:
        for i in range(12):
            line = f"{i}\n"
            file.write(line)
            print(line)
            file.flush()

            # Ждем одну секунду
            time.sleep(1)
