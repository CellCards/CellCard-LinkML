# Auto generated from cellcard.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-04-12T15:21:56
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
from linkml_runtime.linkml_model.types import Datetime, Double, Float, String
from linkml_runtime.utils.metamodelcore import XSDDateTime

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
CELLCARD = CurieNamespace('cellcard', 'https://cellcards.org/')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
QUD = CurieNamespace('qud', 'http://qudt.org/1.1/schema/qudt#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'https://schema.org/')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = CELLCARD


# Types
class Bytes(int):
    """ An integer value that corresponds to a size in bytes """
    type_class_uri = XSD.int
    type_class_curie = "xsd:int"
    type_name = "bytes"
    type_model_uri = CELLCARD.Bytes


class LanguageCode(str):
    """ A language code conforming to ISO_639-1 """
    type_class_uri = XSD.language
    type_class_curie = "xsd:language"
    type_name = "language code"
    type_model_uri = CELLCARD.LanguageCode


class Unit(str):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "unit"
    type_model_uri = CELLCARD.Unit


# Class references
class NamedThingId(extended_str):
    pass


class CellCardId(NamedThingId):
    pass


class OntologyClassId(NamedThingId):
    pass


class ActivityId(extended_str):
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
    title: Optional[str] = None
    description: Optional[str] = None
    alternative_identifiers: Optional[Union[str, List[str]]] = empty_list()
    alternative_names: Optional[Union[str, List[str]]] = empty_list()
    alternative_titles: Optional[Union[str, List[str]]] = empty_list()
    alternative_descriptions: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.alternative_identifiers, list):
            self.alternative_identifiers = [self.alternative_identifiers] if self.alternative_identifiers is not None else []
        self.alternative_identifiers = [v if isinstance(v, str) else str(v) for v in self.alternative_identifiers]

        if not isinstance(self.alternative_names, list):
            self.alternative_names = [self.alternative_names] if self.alternative_names is not None else []
        self.alternative_names = [v if isinstance(v, str) else str(v) for v in self.alternative_names]

        if not isinstance(self.alternative_titles, list):
            self.alternative_titles = [self.alternative_titles] if self.alternative_titles is not None else []
        self.alternative_titles = [v if isinstance(v, str) else str(v) for v in self.alternative_titles]

        if not isinstance(self.alternative_descriptions, list):
            self.alternative_descriptions = [self.alternative_descriptions] if self.alternative_descriptions is not None else []
        self.alternative_descriptions = [v if isinstance(v, str) else str(v) for v in self.alternative_descriptions]

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
    description_images: Optional[Union[Union[dict, "ImageValue"], List[Union[dict, "ImageValue"]]]] = empty_list()
    obo_id: Optional[str] = None
    ontology_definition: Optional[str] = None
    cell_hierarchy: Optional[str] = None
    cell_hierarchy_image: Optional[Union[dict, "ImageValue"]] = None
    anatomical_location: Optional[str] = None
    connections_and_vicinity: Optional[str] = None
    lineage: Optional[str] = None
    gene_ontology_associations: Optional[Union[str, List[str]]] = empty_list()
    biomarkers: Optional[Union[str, List[str]]] = empty_list()
    expressed_ligands: Optional[Union[str, List[str]]] = empty_list()
    expressed_receptors: Optional[Union[str, List[str]]] = empty_list()
    neighborhood_cell_types: Optional[Union[str, List[str]]] = empty_list()
    gene_expression_profiles: Optional[Union[str, List[str]]] = empty_list()
    pathways_and_functional_maps: Optional[Union[str, List[str]]] = empty_list()
    cell_images: Optional[Union[Union[dict, "ImageValue"], List[Union[dict, "ImageValue"]]]] = empty_list()
    cell_line_cells: Optional[Union[str, List[str]]] = empty_list()
    clinical_significance: Optional[str] = None
    references: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CellCardId):
            self.id = CellCardId(self.id)

        if not isinstance(self.description_images, list):
            self.description_images = [self.description_images] if self.description_images is not None else []
        self.description_images = [v if isinstance(v, ImageValue) else ImageValue(**as_dict(v)) for v in self.description_images]

        if self.obo_id is not None and not isinstance(self.obo_id, str):
            self.obo_id = str(self.obo_id)

        if self.ontology_definition is not None and not isinstance(self.ontology_definition, str):
            self.ontology_definition = str(self.ontology_definition)

        if self.cell_hierarchy is not None and not isinstance(self.cell_hierarchy, str):
            self.cell_hierarchy = str(self.cell_hierarchy)

        if self.cell_hierarchy_image is not None and not isinstance(self.cell_hierarchy_image, ImageValue):
            self.cell_hierarchy_image = ImageValue(**as_dict(self.cell_hierarchy_image))

        if self.anatomical_location is not None and not isinstance(self.anatomical_location, str):
            self.anatomical_location = str(self.anatomical_location)

        if self.connections_and_vicinity is not None and not isinstance(self.connections_and_vicinity, str):
            self.connections_and_vicinity = str(self.connections_and_vicinity)

        if self.lineage is not None and not isinstance(self.lineage, str):
            self.lineage = str(self.lineage)

        if not isinstance(self.gene_ontology_associations, list):
            self.gene_ontology_associations = [self.gene_ontology_associations] if self.gene_ontology_associations is not None else []
        self.gene_ontology_associations = [v if isinstance(v, str) else str(v) for v in self.gene_ontology_associations]

        if not isinstance(self.biomarkers, list):
            self.biomarkers = [self.biomarkers] if self.biomarkers is not None else []
        self.biomarkers = [v if isinstance(v, str) else str(v) for v in self.biomarkers]

        if not isinstance(self.expressed_ligands, list):
            self.expressed_ligands = [self.expressed_ligands] if self.expressed_ligands is not None else []
        self.expressed_ligands = [v if isinstance(v, str) else str(v) for v in self.expressed_ligands]

        if not isinstance(self.expressed_receptors, list):
            self.expressed_receptors = [self.expressed_receptors] if self.expressed_receptors is not None else []
        self.expressed_receptors = [v if isinstance(v, str) else str(v) for v in self.expressed_receptors]

        if not isinstance(self.neighborhood_cell_types, list):
            self.neighborhood_cell_types = [self.neighborhood_cell_types] if self.neighborhood_cell_types is not None else []
        self.neighborhood_cell_types = [v if isinstance(v, str) else str(v) for v in self.neighborhood_cell_types]

        if not isinstance(self.gene_expression_profiles, list):
            self.gene_expression_profiles = [self.gene_expression_profiles] if self.gene_expression_profiles is not None else []
        self.gene_expression_profiles = [v if isinstance(v, str) else str(v) for v in self.gene_expression_profiles]

        if not isinstance(self.pathways_and_functional_maps, list):
            self.pathways_and_functional_maps = [self.pathways_and_functional_maps] if self.pathways_and_functional_maps is not None else []
        self.pathways_and_functional_maps = [v if isinstance(v, str) else str(v) for v in self.pathways_and_functional_maps]

        if not isinstance(self.cell_images, list):
            self.cell_images = [self.cell_images] if self.cell_images is not None else []
        self.cell_images = [v if isinstance(v, ImageValue) else ImageValue(**as_dict(v)) for v in self.cell_images]

        if not isinstance(self.cell_line_cells, list):
            self.cell_line_cells = [self.cell_line_cells] if self.cell_line_cells is not None else []
        self.cell_line_cells = [v if isinstance(v, str) else str(v) for v in self.cell_line_cells]

        if self.clinical_significance is not None and not isinstance(self.clinical_significance, str):
            self.clinical_significance = str(self.clinical_significance)

        if not isinstance(self.references, list):
            self.references = [self.references] if self.references is not None else []
        self.references = [v if isinstance(v, str) else str(v) for v in self.references]

        if self.obo_id is not None and not isinstance(self.obo_id, str):
            self.obo_id = str(self.obo_id)

        super().__post_init__(**kwargs)


@dataclass
class OntologyClass(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CELLCARD.OntologyClass
    class_class_curie: ClassVar[str] = "cellcard:OntologyClass"
    class_name: ClassVar[str] = "ontology class"
    class_model_uri: ClassVar[URIRef] = CELLCARD.OntologyClass

    id: Union[str, OntologyClassId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OntologyClassId):
            self.id = OntologyClassId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class AttributeValue(YAMLRoot):
    """
    The value for any value of a attribute for an entity. This object can hold both the un-normalized atomic value and
    the structured value
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CELLCARD.AttributeValue
    class_class_curie: ClassVar[str] = "cellcard:AttributeValue"
    class_name: ClassVar[str] = "attribute value"
    class_model_uri: ClassVar[URIRef] = CELLCARD.AttributeValue

    was_generated_by: Optional[Union[str, ActivityId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.was_generated_by is not None and not isinstance(self.was_generated_by, ActivityId):
            self.was_generated_by = ActivityId(self.was_generated_by)

        super().__post_init__(**kwargs)


@dataclass
class QuantityValue(AttributeValue):
    """
    A simple quantity, e.g. 2cm
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CELLCARD.QuantityValue
    class_class_curie: ClassVar[str] = "cellcard:QuantityValue"
    class_name: ClassVar[str] = "quantity value"
    class_model_uri: ClassVar[URIRef] = CELLCARD.QuantityValue

    has_unit: Optional[str] = None
    has_numeric_value: Optional[float] = None
    has_minimum_numeric_value: Optional[float] = None
    has_maximum_numeric_value: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_unit is not None and not isinstance(self.has_unit, str):
            self.has_unit = str(self.has_unit)

        if self.has_numeric_value is not None and not isinstance(self.has_numeric_value, float):
            self.has_numeric_value = float(self.has_numeric_value)

        if self.has_minimum_numeric_value is not None and not isinstance(self.has_minimum_numeric_value, float):
            self.has_minimum_numeric_value = float(self.has_minimum_numeric_value)

        if self.has_maximum_numeric_value is not None and not isinstance(self.has_maximum_numeric_value, float):
            self.has_maximum_numeric_value = float(self.has_maximum_numeric_value)

        super().__post_init__(**kwargs)


@dataclass
class ImageValue(AttributeValue):
    """
    An attribute value representing an image.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CELLCARD.ImageValue
    class_class_curie: ClassVar[str] = "cellcard:ImageValue"
    class_name: ClassVar[str] = "image value"
    class_model_uri: ClassVar[URIRef] = CELLCARD.ImageValue

    url: Optional[str] = None
    description: Optional[str] = None
    display_order: Optional[str] = None
    copyright: Optional[str] = None
    image_caption: Optional[str] = None
    image_height: Optional[str] = None
    image_width: Optional[str] = None
    image_bit_rate: Optional[str] = None
    image_encoding_format: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.url is not None and not isinstance(self.url, str):
            self.url = str(self.url)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.display_order is not None and not isinstance(self.display_order, str):
            self.display_order = str(self.display_order)

        if self.copyright is not None and not isinstance(self.copyright, str):
            self.copyright = str(self.copyright)

        if self.image_caption is not None and not isinstance(self.image_caption, str):
            self.image_caption = str(self.image_caption)

        if self.image_height is not None and not isinstance(self.image_height, str):
            self.image_height = str(self.image_height)

        if self.image_width is not None and not isinstance(self.image_width, str):
            self.image_width = str(self.image_width)

        if self.image_bit_rate is not None and not isinstance(self.image_bit_rate, str):
            self.image_bit_rate = str(self.image_bit_rate)

        if self.image_encoding_format is not None and not isinstance(self.image_encoding_format, str):
            self.image_encoding_format = str(self.image_encoding_format)

        super().__post_init__(**kwargs)


@dataclass
class TextValue(AttributeValue):
    """
    A basic string value
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CELLCARD.TextValue
    class_class_curie: ClassVar[str] = "cellcard:TextValue"
    class_name: ClassVar[str] = "text value"
    class_model_uri: ClassVar[URIRef] = CELLCARD.TextValue

    language: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.language is not None and not isinstance(self.language, str):
            self.language = str(self.language)

        super().__post_init__(**kwargs)


class UrlValue(AttributeValue):
    """
    A value that is a string that conforms to URL syntax
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CELLCARD.UrlValue
    class_class_curie: ClassVar[str] = "cellcard:UrlValue"
    class_name: ClassVar[str] = "url value"
    class_model_uri: ClassVar[URIRef] = CELLCARD.UrlValue


@dataclass
class PersonValue(AttributeValue):
    """
    An attribute value representing a person
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CELLCARD.PersonValue
    class_class_curie: ClassVar[str] = "cellcard:PersonValue"
    class_name: ClassVar[str] = "person value"
    class_model_uri: ClassVar[URIRef] = CELLCARD.PersonValue

    orcid: Optional[str] = None
    profile_image_url: Optional[str] = None
    email: Optional[str] = None
    name: Optional[str] = None
    websites: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.orcid is not None and not isinstance(self.orcid, str):
            self.orcid = str(self.orcid)

        if self.profile_image_url is not None and not isinstance(self.profile_image_url, str):
            self.profile_image_url = str(self.profile_image_url)

        if self.email is not None and not isinstance(self.email, str):
            self.email = str(self.email)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.websites, list):
            self.websites = [self.websites] if self.websites is not None else []
        self.websites = [v if isinstance(v, str) else str(v) for v in self.websites]

        super().__post_init__(**kwargs)


@dataclass
class Activity(YAMLRoot):
    """
    A provence-generating activity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CELLCARD.Activity
    class_class_curie: ClassVar[str] = "cellcard:Activity"
    class_name: ClassVar[str] = "activity"
    class_model_uri: ClassVar[URIRef] = CELLCARD.Activity

    id: Union[str, ActivityId] = None
    name: Optional[str] = None
    started_at_time: Optional[Union[str, XSDDateTime]] = None
    ended_at_time: Optional[Union[str, XSDDateTime]] = None
    was_informed_by: Optional[Union[str, ActivityId]] = None
    was_associated_with: Optional[Union[dict, "Agent"]] = None
    used: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ActivityId):
            self.id = ActivityId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.started_at_time is not None and not isinstance(self.started_at_time, XSDDateTime):
            self.started_at_time = XSDDateTime(self.started_at_time)

        if self.ended_at_time is not None and not isinstance(self.ended_at_time, XSDDateTime):
            self.ended_at_time = XSDDateTime(self.ended_at_time)

        if self.was_informed_by is not None and not isinstance(self.was_informed_by, ActivityId):
            self.was_informed_by = ActivityId(self.was_informed_by)

        if self.was_associated_with is not None and not isinstance(self.was_associated_with, Agent):
            self.was_associated_with = Agent(**as_dict(self.was_associated_with))

        if self.used is not None and not isinstance(self.used, str):
            self.used = str(self.used)

        super().__post_init__(**kwargs)


@dataclass
class Agent(YAMLRoot):
    """
    A provence-generating agent
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CELLCARD.Agent
    class_class_curie: ClassVar[str] = "cellcard:Agent"
    class_name: ClassVar[str] = "agent"
    class_model_uri: ClassVar[URIRef] = CELLCARD.Agent

    acted_on_behalf_of: Optional[Union[dict, "Agent"]] = None
    was_informed_by: Optional[Union[str, ActivityId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.acted_on_behalf_of is not None and not isinstance(self.acted_on_behalf_of, Agent):
            self.acted_on_behalf_of = Agent(**as_dict(self.acted_on_behalf_of))

        if self.was_informed_by is not None and not isinstance(self.was_informed_by, ActivityId):
            self.was_informed_by = ActivityId(self.was_informed_by)

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

slots.title = Slot(uri=CELLCARD.title, name="title", curie=CELLCARD.curie('title'),
                   model_uri=CELLCARD.title, domain=None, range=Optional[str])

slots.description = Slot(uri=DCTERMS.description, name="description", curie=DCTERMS.curie('description'),
                   model_uri=CELLCARD.description, domain=None, range=Optional[str])

slots.alternative_names = Slot(uri=CELLCARD.alternative_names, name="alternative names", curie=CELLCARD.curie('alternative_names'),
                   model_uri=CELLCARD.alternative_names, domain=None, range=Optional[Union[str, List[str]]])

slots.alternative_descriptions = Slot(uri=CELLCARD.alternative_descriptions, name="alternative descriptions", curie=CELLCARD.curie('alternative_descriptions'),
                   model_uri=CELLCARD.alternative_descriptions, domain=None, range=Optional[Union[str, List[str]]])

slots.alternative_identifiers = Slot(uri=CELLCARD.alternative_identifiers, name="alternative identifiers", curie=CELLCARD.curie('alternative_identifiers'),
                   model_uri=CELLCARD.alternative_identifiers, domain=None, range=Optional[Union[str, List[str]]])

slots.alternative_titles = Slot(uri=CELLCARD.alternative_titles, name="alternative titles", curie=CELLCARD.curie('alternative_titles'),
                   model_uri=CELLCARD.alternative_titles, domain=None, range=Optional[Union[str, List[str]]])

slots.email = Slot(uri=SCHEMA.email, name="email", curie=SCHEMA.curie('email'),
                   model_uri=CELLCARD.email, domain=None, range=Optional[str])

slots.websites = Slot(uri=CELLCARD.websites, name="websites", curie=CELLCARD.curie('websites'),
                   model_uri=CELLCARD.websites, domain=None, range=Optional[Union[str, List[str]]])

slots.url = Slot(uri=CELLCARD.url, name="url", curie=CELLCARD.curie('url'),
                   model_uri=CELLCARD.url, domain=None, range=Optional[str])

slots.display_order = Slot(uri=CELLCARD.display_order, name="display order", curie=CELLCARD.curie('display_order'),
                   model_uri=CELLCARD.display_order, domain=None, range=Optional[str])

slots.has_unit = Slot(uri=CELLCARD.has_unit, name="has unit", curie=CELLCARD.curie('has_unit'),
                   model_uri=CELLCARD.has_unit, domain=None, range=Optional[str], mappings = [QUD.unit, SCHEMA.unitCode])

slots.has_numeric_value = Slot(uri=CELLCARD.has_numeric_value, name="has numeric value", curie=CELLCARD.curie('has_numeric_value'),
                   model_uri=CELLCARD.has_numeric_value, domain=None, range=Optional[float], mappings = [QUD.quantityValue, SCHEMA.value])

slots.has_minimum_numeric_value = Slot(uri=CELLCARD.has_minimum_numeric_value, name="has minimum numeric value", curie=CELLCARD.curie('has_minimum_numeric_value'),
                   model_uri=CELLCARD.has_minimum_numeric_value, domain=None, range=Optional[float])

slots.has_maximum_numeric_value = Slot(uri=CELLCARD.has_maximum_numeric_value, name="has maximum numeric value", curie=CELLCARD.curie('has_maximum_numeric_value'),
                   model_uri=CELLCARD.has_maximum_numeric_value, domain=None, range=Optional[float])

slots.term = Slot(uri=RDF.type, name="term", curie=RDF.curie('type'),
                   model_uri=CELLCARD.term, domain=None, range=Optional[Union[dict, OntologyClass]])

slots.orcid = Slot(uri=CELLCARD.orcid, name="orcid", curie=CELLCARD.curie('orcid'),
                   model_uri=CELLCARD.orcid, domain=PersonValue, range=Optional[str])

slots.profile_image_url = Slot(uri=CELLCARD.profile_image_url, name="profile image url", curie=CELLCARD.curie('profile_image_url'),
                   model_uri=CELLCARD.profile_image_url, domain=PersonValue, range=Optional[str])

slots.language = Slot(uri=CELLCARD.language, name="language", curie=CELLCARD.curie('language'),
                   model_uri=CELLCARD.language, domain=None, range=Optional[str])

slots.copyright = Slot(uri=CELLCARD.copyright, name="copyright", curie=CELLCARD.curie('copyright'),
                   model_uri=CELLCARD.copyright, domain=None, range=Optional[str])

slots.image_caption = Slot(uri=CELLCARD.image_caption, name="image caption", curie=CELLCARD.curie('image_caption'),
                   model_uri=CELLCARD.image_caption, domain=ImageValue, range=Optional[str])

slots.image_height = Slot(uri=CELLCARD.image_height, name="image height", curie=CELLCARD.curie('image_height'),
                   model_uri=CELLCARD.image_height, domain=ImageValue, range=Optional[str])

slots.image_width = Slot(uri=CELLCARD.image_width, name="image width", curie=CELLCARD.curie('image_width'),
                   model_uri=CELLCARD.image_width, domain=ImageValue, range=Optional[str])

slots.image_bit_rate = Slot(uri=CELLCARD.image_bit_rate, name="image bit rate", curie=CELLCARD.curie('image_bit_rate'),
                   model_uri=CELLCARD.image_bit_rate, domain=ImageValue, range=Optional[str])

slots.image_encoding_format = Slot(uri=CELLCARD.image_encoding_format, name="image encoding format", curie=CELLCARD.curie('image_encoding_format'),
                   model_uri=CELLCARD.image_encoding_format, domain=ImageValue, range=Optional[str])

slots.started_at_time = Slot(uri=CELLCARD.started_at_time, name="started at time", curie=CELLCARD.curie('started_at_time'),
                   model_uri=CELLCARD.started_at_time, domain=None, range=Optional[Union[str, XSDDateTime]],
                   pattern=re.compile(r'^([\+-]?\d{4}(?!\d{2}\b))((-?)((0[1-9]|1[0-2])(\3([12]\d|0[1-9]|3[01]))?|W([0-4]\d|5[0-2])(-?[1-7])?|(00[1-9]|0[1-9]\d|[12]\d{2}|3([0-5]\d|6[1-6])))([T\s]((([01]\d|2[0-3])((:?)[0-5]\d)?|24\:?00)([\.,]\d+(?!:))?)?(\17[0-5]\d([\.,]\d+)?)?([zZ]|([\+-])([01]\d|2[0-3]):?([0-5]\d)?)?)?)?$'))

slots.ended_at_time = Slot(uri=CELLCARD.ended_at_time, name="ended at time", curie=CELLCARD.curie('ended_at_time'),
                   model_uri=CELLCARD.ended_at_time, domain=None, range=Optional[Union[str, XSDDateTime]],
                   pattern=re.compile(r'^([\+-]?\d{4}(?!\d{2}\b))((-?)((0[1-9]|1[0-2])(\3([12]\d|0[1-9]|3[01]))?|W([0-4]\d|5[0-2])(-?[1-7])?|(00[1-9]|0[1-9]\d|[12]\d{2}|3([0-5]\d|6[1-6])))([T\s]((([01]\d|2[0-3])((:?)[0-5]\d)?|24\:?00)([\.,]\d+(?!:))?)?(\17[0-5]\d([\.,]\d+)?)?([zZ]|([\+-])([01]\d|2[0-3]):?([0-5]\d)?)?)?)?$'))

slots.was_informed_by = Slot(uri=CELLCARD.was_informed_by, name="was informed by", curie=CELLCARD.curie('was_informed_by'),
                   model_uri=CELLCARD.was_informed_by, domain=None, range=Optional[Union[str, ActivityId]])

slots.was_associated_with = Slot(uri=CELLCARD.was_associated_with, name="was associated with", curie=CELLCARD.curie('was_associated_with'),
                   model_uri=CELLCARD.was_associated_with, domain=None, range=Optional[Union[dict, Agent]])

slots.acted_on_behalf_of = Slot(uri=CELLCARD.acted_on_behalf_of, name="acted on behalf of", curie=CELLCARD.curie('acted_on_behalf_of'),
                   model_uri=CELLCARD.acted_on_behalf_of, domain=None, range=Optional[Union[dict, Agent]])

slots.was_generated_by = Slot(uri=CELLCARD.was_generated_by, name="was generated by", curie=CELLCARD.curie('was_generated_by'),
                   model_uri=CELLCARD.was_generated_by, domain=None, range=Optional[Union[str, ActivityId]])

slots.used = Slot(uri=CELLCARD.used, name="used", curie=CELLCARD.curie('used'),
                   model_uri=CELLCARD.used, domain=Activity, range=Optional[str], mappings = [PROV.used])

slots.cellCard__description_images = Slot(uri=CELLCARD.description_images, name="cellCard__description_images", curie=CELLCARD.curie('description_images'),
                   model_uri=CELLCARD.cellCard__description_images, domain=None, range=Optional[Union[Union[dict, ImageValue], List[Union[dict, ImageValue]]]])

slots.cellCard__obo_id = Slot(uri=CELLCARD.obo_id, name="cellCard__obo_id", curie=CELLCARD.curie('obo_id'),
                   model_uri=CELLCARD.cellCard__obo_id, domain=None, range=Optional[str],
                   pattern=re.compile(r'CL_\d{7}'))

slots.cellCard__ontology_definition = Slot(uri=CELLCARD.ontology_definition, name="cellCard__ontology_definition", curie=CELLCARD.curie('ontology_definition'),
                   model_uri=CELLCARD.cellCard__ontology_definition, domain=None, range=Optional[str])

slots.cellCard__cell_hierarchy = Slot(uri=CELLCARD.cell_hierarchy, name="cellCard__cell_hierarchy", curie=CELLCARD.curie('cell_hierarchy'),
                   model_uri=CELLCARD.cellCard__cell_hierarchy, domain=None, range=Optional[str])

slots.cellCard__cell_hierarchy_image = Slot(uri=CELLCARD.cell_hierarchy_image, name="cellCard__cell_hierarchy_image", curie=CELLCARD.curie('cell_hierarchy_image'),
                   model_uri=CELLCARD.cellCard__cell_hierarchy_image, domain=None, range=Optional[Union[dict, ImageValue]])

slots.cellCard__anatomical_location = Slot(uri=CELLCARD.anatomical_location, name="cellCard__anatomical_location", curie=CELLCARD.curie('anatomical_location'),
                   model_uri=CELLCARD.cellCard__anatomical_location, domain=None, range=Optional[str])

slots.cellCard__connections_and_vicinity = Slot(uri=CELLCARD.connections_and_vicinity, name="cellCard__connections_and_vicinity", curie=CELLCARD.curie('connections_and_vicinity'),
                   model_uri=CELLCARD.cellCard__connections_and_vicinity, domain=None, range=Optional[str])

slots.cellCard__lineage = Slot(uri=CELLCARD.lineage, name="cellCard__lineage", curie=CELLCARD.curie('lineage'),
                   model_uri=CELLCARD.cellCard__lineage, domain=None, range=Optional[str])

slots.cellCard__gene_ontology_associations = Slot(uri=CELLCARD.gene_ontology_associations, name="cellCard__gene_ontology_associations", curie=CELLCARD.curie('gene_ontology_associations'),
                   model_uri=CELLCARD.cellCard__gene_ontology_associations, domain=None, range=Optional[Union[str, List[str]]])

slots.cellCard__biomarkers = Slot(uri=CELLCARD.biomarkers, name="cellCard__biomarkers", curie=CELLCARD.curie('biomarkers'),
                   model_uri=CELLCARD.cellCard__biomarkers, domain=None, range=Optional[Union[str, List[str]]])

slots.cellCard__expressed_ligands = Slot(uri=CELLCARD.expressed_ligands, name="cellCard__expressed_ligands", curie=CELLCARD.curie('expressed_ligands'),
                   model_uri=CELLCARD.cellCard__expressed_ligands, domain=None, range=Optional[Union[str, List[str]]])

slots.cellCard__expressed_receptors = Slot(uri=CELLCARD.expressed_receptors, name="cellCard__expressed_receptors", curie=CELLCARD.curie('expressed_receptors'),
                   model_uri=CELLCARD.cellCard__expressed_receptors, domain=None, range=Optional[Union[str, List[str]]])

slots.cellCard__neighborhood_cell_types = Slot(uri=CELLCARD.neighborhood_cell_types, name="cellCard__neighborhood_cell_types", curie=CELLCARD.curie('neighborhood_cell_types'),
                   model_uri=CELLCARD.cellCard__neighborhood_cell_types, domain=None, range=Optional[Union[str, List[str]]])

slots.cellCard__gene_expression_profiles = Slot(uri=CELLCARD.gene_expression_profiles, name="cellCard__gene_expression_profiles", curie=CELLCARD.curie('gene_expression_profiles'),
                   model_uri=CELLCARD.cellCard__gene_expression_profiles, domain=None, range=Optional[Union[str, List[str]]])

slots.cellCard__pathways_and_functional_maps = Slot(uri=CELLCARD.pathways_and_functional_maps, name="cellCard__pathways_and_functional_maps", curie=CELLCARD.curie('pathways_and_functional_maps'),
                   model_uri=CELLCARD.cellCard__pathways_and_functional_maps, domain=None, range=Optional[Union[str, List[str]]])

slots.cellCard__cell_images = Slot(uri=CELLCARD.cell_images, name="cellCard__cell_images", curie=CELLCARD.curie('cell_images'),
                   model_uri=CELLCARD.cellCard__cell_images, domain=None, range=Optional[Union[Union[dict, ImageValue], List[Union[dict, ImageValue]]]])

slots.cellCard__cell_line_cells = Slot(uri=CELLCARD.cell_line_cells, name="cellCard__cell_line_cells", curie=CELLCARD.curie('cell_line_cells'),
                   model_uri=CELLCARD.cellCard__cell_line_cells, domain=None, range=Optional[Union[str, List[str]]])

slots.cellCard__clinical_significance = Slot(uri=CELLCARD.clinical_significance, name="cellCard__clinical_significance", curie=CELLCARD.curie('clinical_significance'),
                   model_uri=CELLCARD.cellCard__clinical_significance, domain=None, range=Optional[str])

slots.cellCard__references = Slot(uri=CELLCARD.references, name="cellCard__references", curie=CELLCARD.curie('references'),
                   model_uri=CELLCARD.cellCard__references, domain=None, range=Optional[Union[str, List[str]]])

slots.obo_id = Slot(uri=CELLCARD.obo_id, name="obo id", curie=CELLCARD.curie('obo_id'),
                   model_uri=CELLCARD.obo_id, domain=None, range=Optional[str],
                   pattern=re.compile(r'CL_\d{7}'))

slots.cell_card_obo_id = Slot(uri=CELLCARD.obo_id, name="cell card_obo id", curie=CELLCARD.curie('obo_id'),
                   model_uri=CELLCARD.cell_card_obo_id, domain=CellCard, range=Optional[str],
                   pattern=re.compile(r'CL_\d{7}'))

slots.quantity_value_has_unit = Slot(uri=CELLCARD.has_unit, name="quantity value_has unit", curie=CELLCARD.curie('has_unit'),
                   model_uri=CELLCARD.quantity_value_has_unit, domain=QuantityValue, range=Optional[str], mappings = [QUD.unit, SCHEMA.unitCode])

slots.quantity_value_has_numeric_value = Slot(uri=CELLCARD.has_numeric_value, name="quantity value_has numeric value", curie=CELLCARD.curie('has_numeric_value'),
                   model_uri=CELLCARD.quantity_value_has_numeric_value, domain=QuantityValue, range=Optional[float], mappings = [QUD.quantityValue, SCHEMA.value])