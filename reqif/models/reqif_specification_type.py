from typing import List, Dict

from reqif.models.reqif_spec_object_type import SpecAttributeDefinition


class ReqIFSpecificationType:
    def __init__(  # pylint: disable=too-many-arguments
        self,
        identifier: str,
        last_change: str,
        long_name: str,
        spec_attributes: List[SpecAttributeDefinition],
        spec_attribute_map: Dict[str, str],
    ):
        self.identifier: str = identifier
        self.last_change: str = last_change
        self.long_name: str = long_name
        self.spec_attributes = spec_attributes
        self.spec_attribute_map = spec_attribute_map

    def __str__(self) -> str:
        return f"ReqIFSpecificationType(" f"identifier: {self.identifier}," f")"

    def __repr__(self) -> str:
        return self.__str__()
