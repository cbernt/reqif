from typing import Optional, List

from reqif.models.reqif_spec_object import SpecObjectAttribute


class ReqIFSpecRelation:  # pylint: disable=too-many-instance-attributes
    def __init__(  # pylint: disable=too-many-arguments
        self,
        children_tags: List[str],
        description: Optional[str],
        identifier: str,
        last_change: Optional[str],
        relation_type_ref,
        source: str,
        target: str,
        values_attribute: Optional[SpecObjectAttribute],
    ):
        self.children_tags: List[str] = children_tags
        self.description: Optional[str] = description
        self.identifier: str = identifier
        self.last_change: Optional[str] = last_change
        self.relation_type_ref = relation_type_ref
        self.source: str = source
        self.target: str = target
        self.values_attribute: Optional[SpecObjectAttribute] = values_attribute
