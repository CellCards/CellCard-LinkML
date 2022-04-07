# CellCard-LinkML
CellCard-LinkML: Cell Card LinkML project

Project goal: To use LinkML technology for [cellcards.org](https://cellcards.org).  

Have an ontology, using YML to define the schema, ...

The LinkML modeling language will be used to design schemas that are easily shared across many platforms and communities. We will leverage the modeling features of LinkML to define the minimum information standards, the structure of the cell cards, and mappings between cell card fields and ontology terms. This will allow us to validate data that goes into the cell cards and disseminate documentation to the community about the information standards required to produce CellCards. We will also use LinkML to drive the CellCards user interface. This will standardize the workflows, making it easier for other groups to use and ensuring rigor and reproducibility. Here, we will leverage the knowledgebase created in ASCT+B2, including contributions from investigators worldwide.

A Similar Example: 
If you want to see linkml in action you can look at the [NMDC Schema](https://microbiomedata.github.io/nmdc-schema/). The documentation and [jsonschema](https://github.com/microbiomedata/nmdc-schema/blob/main/jsonschema/nmdc.schema.json) were generated from the LinkML [nmdc.yaml](https://github.com/microbiomedata/nmdc-schema/blob/main/src/schema/nmdc.yaml) file. A similar approach would be used for the cell cards:

1. Define schema in LinkML (i.e., yaml files)
2. Generate jsonschema, ddl, rdf, documentation, etc. from the yaml files.
3. Deploy documentation.

Moreover, the generated jsonschema is used to validate data before inputting the data into the database.

