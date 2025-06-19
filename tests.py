from computer_builder import Computer, GamingComputerBuilder, OfficeComputerBuilder, ComputerAssembler


def test_gaming_computer_builder():
    # Arrange
    builder = GamingComputerBuilder()
    assembler = ComputerAssembler(builder)

    # Act
    computer = assembler.assemble_computer()

    # Assert
    assert computer.cpu == "Игровой Intel Core i9-13900K"
    assert computer.gpu == "Мощная NVIDIA RTX 4090"
    assert computer.ram == "32 ГБ DDR5 RGB"
    assert computer.storage == "SSD NVMe 2TB"
    assert computer.cooling == "Жидкостное охлаждение Corsair iCUE H150i"


def test_office_computer_builder():
    # Arrange
    builder = OfficeComputerBuilder()
    assembler = ComputerAssembler(builder)

    # Act
    computer = assembler.assemble_budget_computer()

    # Assert
    assert computer.cpu == "Энергоэффективный Intel Core i3-12100"
    assert computer.gpu == "Интегрированная графика Intel UHD Graphics 730"
    assert computer.ram == "8 ГБ DDR4"
    assert computer.storage == "HDD 500GB"
    assert computer.cooling == "Стандартный кулер Box cooler"