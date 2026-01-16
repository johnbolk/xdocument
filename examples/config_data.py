"""config_data.py - An XML document class for dataclass attribute values."""

from dataclasses import asdict
from xdocument import XDocument


class ConfigData(XDocument):
    """An XML document class for dataclass attribute values."""

    def __init__(self, filename, dataclass):
        """Load an existing file or create a new XML document file."""
        super().__init__(filename, details=dataclass)

    def _subclass_details(self) -> None:
        """Provide the initialization details for the derived subclass."""
        if self._details is not None:
            self.write(self._details)  # The default dataclass attribute values

    def read(self, dataclass):
        """Read the dataclass attribute values from the XML document."""
        element = self.root.find_child(class_name(dataclass))
        if element is not None:  # The XML document may be blank or corrupted
            for name, value in asdict(dataclass).items():
                attribute_value = element.read_child(pascal_case(name), value)
                setattr(dataclass, name, attribute_value)
        return dataclass

    def write(self, dataclass):
        """Write the dataclass attribute values to the XML document."""
        element = self.root.find_child(class_name(dataclass))
        if element is None:  # The XML document may be blank or corrupted
            element = self.root.add(class_name(dataclass))
        for name, value in asdict(dataclass).items():
            element.write_child(pascal_case(name), value)


def class_name(dataclass):
    """Return the name of the dataclass."""
    return type(dataclass).__name__


def pascal_case(attribute_name):
    """Convert the attribute name to a Pascal Case name."""
    return attribute_name.replace('_', ' ').title().replace(' ', '')
