

CREATE TABLE activity (
	id TEXT NOT NULL, 
	name TEXT, 
	started_at_time DATETIME, 
	ended_at_time DATETIME, 
	was_informed_by TEXT, 
	was_associated_with TEXT, 
	used TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_informed_by) REFERENCES activity (id)
);

CREATE TABLE cell_card (
	id TEXT NOT NULL, 
	name TEXT, 
	title TEXT, 
	description TEXT, 
	description_images TEXT, 
	obo_id TEXT, 
	ontology_definition TEXT, 
	cell_hierarchy TEXT, 
	anatomical_location TEXT, 
	connections_and_vicinity TEXT, 
	lineage TEXT, 
	cell_images TEXT, 
	clinical_significance TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "database" (
	cell_card_set TEXT, 
	PRIMARY KEY (cell_card_set)
);

CREATE TABLE ontology_class (
	id TEXT NOT NULL, 
	name TEXT, 
	title TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE agent (
	acted_on_behalf_of TEXT, 
	was_informed_by TEXT, 
	PRIMARY KEY (acted_on_behalf_of, was_informed_by), 
	FOREIGN KEY(was_informed_by) REFERENCES activity (id)
);

CREATE TABLE attribute_value (
	name TEXT, 
	title TEXT, 
	was_generated_by TEXT, 
	PRIMARY KEY (name, title, was_generated_by), 
	FOREIGN KEY(was_generated_by) REFERENCES activity (id)
);

CREATE TABLE image_value (
	name TEXT, 
	title TEXT, 
	was_generated_by TEXT, 
	url TEXT, 
	description TEXT, 
	display_order TEXT, 
	copyright TEXT, 
	image_caption TEXT, 
	image_height TEXT, 
	image_width TEXT, 
	image_bit_rate TEXT, 
	image_encoding_format TEXT, 
	PRIMARY KEY (name, title, was_generated_by, url, description, display_order, copyright, image_caption, image_height, image_width, image_bit_rate, image_encoding_format), 
	FOREIGN KEY(was_generated_by) REFERENCES activity (id)
);

CREATE TABLE person_value (
	title TEXT, 
	was_generated_by TEXT, 
	orcid TEXT, 
	profile_image_url TEXT, 
	email TEXT, 
	name TEXT, 
	websites TEXT, 
	PRIMARY KEY (title, was_generated_by, orcid, profile_image_url, email, name, websites), 
	FOREIGN KEY(was_generated_by) REFERENCES activity (id)
);

CREATE TABLE quantity_value (
	name TEXT, 
	title TEXT, 
	was_generated_by TEXT, 
	has_unit TEXT, 
	has_numeric_value FLOAT, 
	has_minimum_numeric_value FLOAT, 
	has_maximum_numeric_value FLOAT, 
	PRIMARY KEY (name, title, was_generated_by, has_unit, has_numeric_value, has_minimum_numeric_value, has_maximum_numeric_value), 
	FOREIGN KEY(was_generated_by) REFERENCES activity (id)
);

CREATE TABLE text_value (
	name TEXT, 
	title TEXT, 
	was_generated_by TEXT, 
	language TEXT, 
	PRIMARY KEY (name, title, was_generated_by, language), 
	FOREIGN KEY(was_generated_by) REFERENCES activity (id)
);

CREATE TABLE url_value (
	name TEXT, 
	title TEXT, 
	was_generated_by TEXT, 
	PRIMARY KEY (name, title, was_generated_by), 
	FOREIGN KEY(was_generated_by) REFERENCES activity (id)
);

CREATE TABLE cell_card_alternative_identifiers (
	backref_id TEXT, 
	alternative_identifiers TEXT, 
	PRIMARY KEY (backref_id, alternative_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES cell_card (id)
);

CREATE TABLE cell_card_alternative_names (
	backref_id TEXT, 
	alternative_names TEXT, 
	PRIMARY KEY (backref_id, alternative_names), 
	FOREIGN KEY(backref_id) REFERENCES cell_card (id)
);

CREATE TABLE cell_card_alternative_titles (
	backref_id TEXT, 
	alternative_titles TEXT, 
	PRIMARY KEY (backref_id, alternative_titles), 
	FOREIGN KEY(backref_id) REFERENCES cell_card (id)
);

CREATE TABLE cell_card_alternative_descriptions (
	backref_id TEXT, 
	alternative_descriptions TEXT, 
	PRIMARY KEY (backref_id, alternative_descriptions), 
	FOREIGN KEY(backref_id) REFERENCES cell_card (id)
);

CREATE TABLE cell_card_gene_ontology_associations (
	backref_id TEXT, 
	gene_ontology_associations TEXT, 
	PRIMARY KEY (backref_id, gene_ontology_associations), 
	FOREIGN KEY(backref_id) REFERENCES cell_card (id)
);

CREATE TABLE cell_card_biomarkers (
	backref_id TEXT, 
	biomarkers TEXT, 
	PRIMARY KEY (backref_id, biomarkers), 
	FOREIGN KEY(backref_id) REFERENCES cell_card (id)
);

CREATE TABLE cell_card_expressed_ligands (
	backref_id TEXT, 
	expressed_ligands TEXT, 
	PRIMARY KEY (backref_id, expressed_ligands), 
	FOREIGN KEY(backref_id) REFERENCES cell_card (id)
);

CREATE TABLE cell_card_expressed_receptors (
	backref_id TEXT, 
	expressed_receptors TEXT, 
	PRIMARY KEY (backref_id, expressed_receptors), 
	FOREIGN KEY(backref_id) REFERENCES cell_card (id)
);

CREATE TABLE cell_card_neighborhood_cell_types (
	backref_id TEXT, 
	neighborhood_cell_types TEXT, 
	PRIMARY KEY (backref_id, neighborhood_cell_types), 
	FOREIGN KEY(backref_id) REFERENCES cell_card (id)
);

CREATE TABLE cell_card_gene_expression_profiles (
	backref_id TEXT, 
	gene_expression_profiles TEXT, 
	PRIMARY KEY (backref_id, gene_expression_profiles), 
	FOREIGN KEY(backref_id) REFERENCES cell_card (id)
);

CREATE TABLE cell_card_pathways_and_functional_maps (
	backref_id TEXT, 
	pathways_and_functional_maps TEXT, 
	PRIMARY KEY (backref_id, pathways_and_functional_maps), 
	FOREIGN KEY(backref_id) REFERENCES cell_card (id)
);

CREATE TABLE cell_card_cell_line_cells (
	backref_id TEXT, 
	cell_line_cells TEXT, 
	PRIMARY KEY (backref_id, cell_line_cells), 
	FOREIGN KEY(backref_id) REFERENCES cell_card (id)
);

CREATE TABLE cell_card_references (
	backref_id TEXT, 
	"references" TEXT, 
	PRIMARY KEY (backref_id, "references"), 
	FOREIGN KEY(backref_id) REFERENCES cell_card (id)
);

CREATE TABLE ontology_class_alternative_identifiers (
	backref_id TEXT, 
	alternative_identifiers TEXT, 
	PRIMARY KEY (backref_id, alternative_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES ontology_class (id)
);

CREATE TABLE ontology_class_alternative_names (
	backref_id TEXT, 
	alternative_names TEXT, 
	PRIMARY KEY (backref_id, alternative_names), 
	FOREIGN KEY(backref_id) REFERENCES ontology_class (id)
);

CREATE TABLE ontology_class_alternative_titles (
	backref_id TEXT, 
	alternative_titles TEXT, 
	PRIMARY KEY (backref_id, alternative_titles), 
	FOREIGN KEY(backref_id) REFERENCES ontology_class (id)
);

CREATE TABLE ontology_class_alternative_descriptions (
	backref_id TEXT, 
	alternative_descriptions TEXT, 
	PRIMARY KEY (backref_id, alternative_descriptions), 
	FOREIGN KEY(backref_id) REFERENCES ontology_class (id)
);
