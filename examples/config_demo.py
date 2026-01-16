"""config_demo.py - Store and retrieve the attribute values of a dataclass."""

from dataclasses import dataclass, asdict
from config_data import ConfigData, class_name


@dataclass
class Parameters:
    """An example of configuration parameters."""

    min_threshold: int = 25
    calibration: float = 0.035
    display_results: bool = True
    units: str = 'millimeters'


if __name__ == '__main__':
    document = ConfigData('Config.xml', Parameters())
    parameters = document.read(Parameters())
    print('\n' + class_name(parameters))
    for name, value in asdict(parameters).items():
        print(f'   {name} = {value}')
