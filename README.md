# CellCard-LinkML
CellCard-LinkML: Cell Card LinkML project

Project goal: To use LinkML technology for CellCards.org

Have an ontology, using YML to define the schema, ...

A Similar Example: 
If you want to see linkml in action you can look at the [NMDC Schema](https://microbiomedata.github.io/nmdc-schema/). The documentation and [jsonschema](https://github.com/microbiomedata/nmdc-schema/blob/main/jsonschema/nmdc.schema.json) were generated from the LinkML [nmdc.yaml](https://github.com/microbiomedata/nmdc-schema/blob/main/src/schema/nmdc.yaml) file. A similar approach would be used for the cell cards:

1. Define schema in LinkML (i.e., yaml files)
2. Generate jsonschema, ddl, rdf, documentation, etc. from the yaml files.
3. Deploy documentation.

Moreover, the generated jsonschema is used to validate data before inputting the data into the database.





