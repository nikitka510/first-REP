from abc import ABC, abstractmethod


# Продукт - Компьютер
class Computer:
    def __init__(self):
        self.cpu = None
        self.gpu = None
        self.ram = None
        self.storage = None
        self.cooling = None

    def __str__(self):
        return (f"Компьютер:\n"
                f"  Процессор: {self.cpu}\n"
                f"  Видеокарта: {self.gpu}\n"
                f"  Оперативная память: {self.ram}\n"
                f"  Накопитель: {self.storage}\n"
                f"  Охлаждение: {self.cooling}\n")


# Абстрактный строитель
class ComputerBuilder(ABC):
    @abstractmethod
    def set_cpu(self, cpu):
        pass

    @abstractmethod
    def set_gpu(self, gpu):
        pass

    @abstractmethod
    def set_ram(self, ram):
        pass

    @abstractmethod
    def set_storage(self, storage):
        pass

    @abstractmethod
    def set_cooling(self, cooling):
        pass

    @abstractmethod
    def get_computer(self):
        pass


# Конкретный строитель - Игровой компьютер
class GamingComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer = Computer()

    def set_cpu(self, cpu):
        self.computer.cpu = f"Игровой {cpu}"
        return self

    def set_gpu(self, gpu):
        self.computer.gpu = f"Мощная {gpu}"
        return self

    def set_ram(self, ram):
        self.computer.ram = f"{ram} ГБ DDR5 RGB"
        return self

    def set_storage(self, storage):
        self.computer.storage = f"SSD NVMe {storage}"
        return self

    def set_cooling(self, cooling):
        self.computer.cooling = f"Жидкостное охлаждение {cooling}"
        return self

    def get_computer(self):
        return self.computer


# Конкретный строитель - Офисный компьютер
class OfficeComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer = Computer()

    def set_cpu(self, cpu):
        self.computer.cpu = f"Энергоэффективный {cpu}"
        return self

    def set_gpu(self, gpu):
        self.computer.gpu = f"Интегрированная графика {gpu}"
        return self

    def set_ram(self, ram):
        self.computer.ram = f"{ram} ГБ DDR4"
        return self

    def set_storage(self, storage):
        self.computer.storage = f"HDD {storage}"
        return self

    def set_cooling(self, cooling):
        self.computer.cooling = f"Стандартный кулер {cooling}"
        return self

    def get_computer(self):
        return self.computer


# Директор - Сборщик компьютеров
class ComputerAssembler:
    def __init__(self, builder):
        self.builder = builder

    def assemble_computer(self):
        return (self.builder.set_cpu("Intel Core i9-13900K")
                .set_gpu("NVIDIA RTX 4090")
                .set_ram(32)
                .set_storage("2TB")
                .set_cooling("Corsair iCUE H150i")
                .get_computer())

    def assemble_budget_computer(self):
        return (self.builder.set_cpu("Intel Core i3-12100")
                .set_gpu("Intel UHD Graphics 730")
                .set_ram(8)
                .set_storage("500GB")
                .set_cooling("Box cooler")
                .get_computer())


# Клиентский код
if __name__ == "__main__":
    print("Сборка игрового компьютера:")
    gaming_builder = GamingComputerBuilder()
    assembler = ComputerAssembler(gaming_builder)
    gaming_pc = assembler.assemble_computer()
    print(gaming_pc)

    print("\nСборка бюджетного офисного компьютера:")
    office_builder = OfficeComputerBuilder()
    assembler = ComputerAssembler(office_builder)
    office_pc = assembler.assemble_budget_computer()
    print(office_pc)
