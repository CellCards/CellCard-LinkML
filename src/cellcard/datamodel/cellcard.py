# Auto generated from cellcard.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-04-09T18:19:37
# Schema: cellcard
#
# id: https://cellcards.org/schema/cellcard
# description: LinkML schema for cell cards.
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import String

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
CELLCARD = CurieNamespace('cellcard', 'https://cellcards.org/')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = CELLCARD


# Types

# Class references
class NamedThingId(extended_str):
    pass


class CellCardId(NamedThingId):
    pass


@dataclass
class Database(YAMLRoot):
    """
    An abstract holder for any set of metadata and data. It does not need to correspond to an actual managed database
    top level holder class. When translated to JSON-Schema this is the 'root' object. It should contain pointers to
    other objects of interest
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CELLCARD.Database
    class_class_curie: ClassVar[str] = "cellcard:Database"
    class_name: ClassVar[str] = "database"
    class_model_uri: ClassVar[URIRef] = CELLCARD.Database

    cell_card_set: Optional[Union[Dict[Union[str, CellCardId], Union[dict, "CellCard"]], List[Union[dict, "CellCard"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="cell_card_set", slot_type=CellCard, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class NamedThing(YAMLRoot):
    """
    A databased entity or concept/class
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CELLCARD.NamedThing
    class_class_curie: ClassVar[str] = "cellcard:NamedThing"
    class_name: ClassVar[str] = "named thing"
    class_model_uri: ClassVar[URIRef] = CELLCARD.NamedThing

    id: Union[str, NamedThingId] = None
    name: Optional[str] = None
    description: Optional[str] = None
    alternative_identifiers: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.alternative_identifiers, list):
            self.alternative_identifiers = [self.alternative_identifiers] if self.alternative_identifiers is not None else []
        self.alternative_identifiers = [v if isinstance(v, str) else str(v) for v in self.alternative_identifiers]

        super().__post_init__(**kwargs)


@dataclass
class CellCard(NamedThing):
    """
    General cell card class from which more specific cells inherit.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CELLCARD.CellCard
    class_class_curie: ClassVar[str] = "cellcard:CellCard"
    class_name: ClassVar[str] = "cell card"
    class_model_uri: ClassVar[URIRef] = CELLCARD.CellCard

    id: Union[str, CellCardId] = None
    cell_type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CellCardId):
            self.id = CellCardId(self.id)

        if self.cell_type is not None and not isinstance(self.cell_type, str):
            self.cell_type = str(self.cell_type)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.object_set = Slot(uri=CELLCARD.object_set, name="object set", curie=CELLCARD.curie('object_set'),
                   model_uri=CELLCARD.object_set, domain=Database, range=Optional[Union[str, List[str]]])

slots.cell_card_set = Slot(uri=CELLCARD.cell_card_set, name="cell card set", curie=CELLCARD.curie('cell_card_set'),
                   model_uri=CELLCARD.cell_card_set, domain=Database, range=Optional[Union[Dict[Union[str, CellCardId], Union[dict, "CellCard"]], List[Union[dict, "CellCard"]]]])

slots.id = Slot(uri=CELLCARD.id, name="id", curie=CELLCARD.curie('id'),
                   model_uri=CELLCARD.id, domain=None, range=URIRef)

slots.name = Slot(uri=CELLCARD.name, name="name", curie=CELLCARD.curie('name'),
                   model_uri=CELLCARD.name, domain=None, range=Optional[str])

slots.description = Slot(uri=DCTERMS.description, name="description", curie=DCTERMS.curie('description'),
                   model_uri=CELLCARD.description, domain=None, range=Optional[str])

slots.alternative_names = Slot(uri=CELLCARD.alternative_names, name="alternative names", curie=CELLCARD.curie('alternative_names'),
                   model_uri=CELLCARD.alternative_names, domain=None, range=Optional[Union[str, List[str]]])

slots.alternative_descriptions = Slot(uri=CELLCARD.alternative_descriptions, name="alternative descriptions", curie=CELLCARD.curie('alternative_descriptions'),
                   model_uri=CELLCARD.alternative_descriptions, domain=None, range=Optional[Union[str, List[str]]])

slots.alternative_identifiers = Slot(uri=CELLCARD.alternative_identifiers, name="alternative identifiers", curie=CELLCARD.curie('alternative_identifiers'),
                   model_uri=CELLCARD.alternative_identifiers, domain=None, range=Optional[Union[str, List[str]]])

slots.cellCard__cell_type = Slot(uri=CELLCARD.cell_type, name="cellCard__cell_type", curie=CELLCARD.curie('cell_type'),
                   model_uri=CELLCARD.cellCard__cell_type, domain=None, range=Optional[str])