# Описание

Тест запуска пайплайна из двух шагов:

Шаг 1.

Запускается Docker-контейнер указанный для шага 1 в файле `params.yaml`.

Данный контейнер выполняет скрипт `pipeline/scripts/reader.py` без поддержи ГПУ.

Шаг 2.

Запускается Docker-контейнер указанный для шага 2 в файле `params.yaml`.

Данный контейнер выполняет скрипт `pipeline/scripts/writer.py` с поддержкой поддержи ГПУ.

Пайплайн описан в файле `dvc.yaml`.

Весь пайплайн запускается командой:
```
dvc repro
```

При этом в терминал из которого был запущен пайплайн на исполнение, аже выводятся все логи внутри docker-контейнера, что очень удобно для отладки и анализа.

Ниже приведен вывод терминала, исполняющего пайплайн:

```
Running stage 'step1':                                                                                                                                 
> docker run --rm -v $(pwd)/pipeline:/workspace -w /workspace vlmevalkit:v0.2rc1-cu124 python scripts/writer.py

==========
== CUDA ==
==========

CUDA Version 12.4.1

Container image Copyright (c) 2016-2023, NVIDIA CORPORATION & AFFILIATES. All rights reserved.

This container image and its contents are governed by the NVIDIA Deep Learning Container License.
By pulling and using the container, you accept the terms and conditions of this license:
https://developer.nvidia.com/ngc/nvidia-deep-learning-container-license

A copy of this license is made available in this container at /NGC-DL-CONTAINER-LICENSE for your convenience.

WARNING: The NVIDIA Driver was not detected.  GPU functionality will not be available.
   Use the NVIDIA Container Toolkit to start this container with GPU support; see
   https://docs.nvidia.com/datacenter/cloud-native/ .

sh: 1: nvidia-smi: not found
0

1

2

3

4

5

6

7

Updating lock file 'dvc.lock'                                                                                                                          

Running stage 'step2':                                                                                                                                 
> docker run --rm -v $(pwd)/pipeline:/workspace -w /workspace --gpus all vlmevalkit:v0.2rc1-cu124 python scripts/reader.py

==========
== CUDA ==
==========

CUDA Version 12.4.1

Container image Copyright (c) 2016-2023, NVIDIA CORPORATION & AFFILIATES. All rights reserved.

This container image and its contents are governed by the NVIDIA Deep Learning Container License.
By pulling and using the container, you accept the terms and conditions of this license:
https://developer.nvidia.com/ngc/nvidia-deep-learning-container-license

A copy of this license is made available in this container at /NGC-DL-CONTAINER-LICENSE for your convenience.

Tue Nov 26 09:20:59 2024       
+---------------------------------------------------------------------------------------+
| NVIDIA-SMI 535.216.01             Driver Version: 535.216.01   CUDA Version: 12.4     |
|-----------------------------------------+----------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |         Memory-Usage | GPU-Util  Compute M. |
|                                         |                      |               MIG M. |
|=========================================+======================+======================|
|   0  NVIDIA A10                     On  | 00000000:01:00.0 Off |                  Off |
|  0%   26C    P8              15W / 150W |      0MiB / 24564MiB |      0%      Default |
|                                         |                      |                  N/A |
+-----------------------------------------+----------------------+----------------------+
                                                                                         
+---------------------------------------------------------------------------------------+
| Processes:                                                                            |
|  GPU   GI   CI        PID   Type   Process name                            GPU Memory |
|        ID   ID                                                             Usage      |
|=======================================================================================|
|  No running processes found                                                           |
+---------------------------------------------------------------------------------------+
torch.__version__ 2.1.2+cu121
torch.cuda.is_available() True
torch.cuda.current_device() 0
torch.cuda.device_count() 0
torch.cuda.get_device_name(0) NVIDIA A10
0
2
4
6
8
10
12
14
Updating lock file 'dvc.lock'                                                                                                                          

To track the changes with git, run:

        git add dvc.lock

To enable auto staging, run:

        dvc config core.autostage true
Use `dvc push` to send your updates to remote storage.
```