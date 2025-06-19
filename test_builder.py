from computer_builder import (
    Computer,
    GamingComputerBuilder,
    OfficeComputerBuilder,
    ComputerAssembler
)
import pytest

@pytest.fixture
def gaming_builder():
    return GamingComputerBuilder()


@pytest.fixture
def office_builder():
    return OfficeComputerBuilder()


@pytest.fixture
def gaming_assembler(gaming_builder):
    return ComputerAssembler(gaming_builder)


@pytest.fixture
def office_assembler(office_builder):
    return ComputerAssembler(office_builder)


class TestComputerClass:
    def test_computer_initialization(self):
        computer = Computer()
        assert computer.cpu is None
        assert computer.gpu is None
        assert computer.ram is None
        assert computer.storage is None
        assert computer.cooling is None

    def test_computer_str_representation(self):
        computer = Computer()
        computer.cpu = "Test CPU"
        assert "Процессор: Test CPU" in str(computer)


class TestGamingComputerBuilder:
    @pytest.mark.parametrize("method,value,expected", [
        ("set_cpu", "i9", "Игровой i9"),
        ("set_gpu", "RTX 4090", "Мощная RTX 4090"),
        ("set_ram", 64, "64 ГБ DDR5 RGB"),
        ("set_storage", "1TB", "SSD NVMe 1TB"),
        ("set_cooling", "Cooler", "Жидкостное охлаждение Cooler"),
    ])
    def test_gaming_builder_methods(self, gaming_builder, method, value, expected):
        builder_method = getattr(gaming_builder, method)
        builder_method(value)
        computer = gaming_builder.get_computer()
        assert getattr(computer, method[4:]) == expected  # method[4:] removes 'set_'


class TestOfficeComputerBuilder:
    @pytest.mark.parametrize("method,value,expected", [
        ("set_cpu", "i3", "Энергоэффективный i3"),
        ("set_gpu", "UHD", "Интегрированная графика UHD"),
        ("set_ram", 8, "8 ГБ DDR4"),
        ("set_storage", "256GB", "HDD 256GB"),
        ("set_cooling", "Basic", "Стандартный кулер Basic"),
    ])
    def test_office_builder_methods(self, office_builder, method, value, expected):
        builder_method = getattr(office_builder, method)
        builder_method(value)
        computer = office_builder.get_computer()
        assert getattr(computer, method[4:]) == expected


class TestComputerAssembler:
    def test_gaming_assembler(self, gaming_assembler):
        computer = gaming_assembler.assemble_computer()
        assert isinstance(computer, Computer)
        assert "Игровой Intel" in computer.cpu
        assert "Мощная NVIDIA" in computer.gpu
        assert "DDR5" in computer.ram
        assert "NVMe" in computer.storage
        assert "Жидкостное" in computer.cooling

    def test_office_assembler(self, office_assembler):
        computer = office_assembler.assemble_budget_computer()
        assert isinstance(computer, Computer)
        assert "Энергоэффективный" in computer.cpu
        assert "Интегрированная" in computer.gpu
        assert "DDR4" in computer.ram
        assert "HDD" in computer.storage
        assert "Стандартный" in computer.cooling

    def test_assembler_builder_change(self, gaming_builder, office_builder):
        # Test assembler can work with different builders
        gaming_assembler = ComputerAssembler(gaming_builder)
        office_assembler = ComputerAssembler(office_builder)

        gaming_pc = gaming_assembler.assemble_computer()
        office_pc = office_assembler.assemble_budget_computer()

        assert "Игровой" in gaming_pc.cpu
        assert "Энергоэффективный" in office_pc.cpu
        assert gaming_pc.cpu != office_pc.cpu


def test_builder_fluent_interface(gaming_builder):
    # Test that builder methods return self for fluent interface
    builder = gaming_builder.set_cpu("test")
    assert builder is gaming_builder
    builder = gaming_builder.set_gpu("test")
    assert builder is gaming_builder


# Специально падающий тест
def test_failing_condition():
    """Этот тест специально написан чтобы падать - проверяет нереалистичное условие"""
    builder = OfficeComputerBuilder()
    computer = builder.set_cpu("i5").get_computer()
    # Это утверждение неверно, так как офисный компьютер добавляет префикс "Энергоэффективный"
    assert computer.cpu == "i5", "Офисный компьютер должен добавлять префикс к процессору"