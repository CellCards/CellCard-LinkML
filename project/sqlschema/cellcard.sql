

CREATE TABLE cell_card (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	cell_type TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "database" (
	cell_card_set TEXT, 
	PRIMARY KEY (cell_card_set)
);

CREATE TABLE cell_card_alternative_identifiers (
	backref_id TEXT, 
	alternative_identifiers TEXT, 
	PRIMARY KEY (backref_id, alternative_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES cell_card (id)
);
