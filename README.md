# Cell Card Schema
## Cell Card LinkML project

Project goal: Use [LinkML](https://linkml.io/linkml/) to define the schema for [cellcards.org](https://cellcards.org).  

The CellCard Schema is developed using the Linked Data Modeling Language (LinkML). LinkML allows developers to design schemas that are easily shared across many platforms and communities. By using LinkML, we can easily define the minimum information standards, the structure of the cell cards, mappings between cell card fields and ontology terms, and generate multiple types of schemas, such as JSON and SQL schemas, to fit the needs of various information systems. The generated schemas will allow us to validate data that goes into the cell cards and disseminate documentation to the community about the information standards required to produce CellCards. We will also use LinkML to drive the CellCards user interface. This will standardize the workflows, making it easier for other groups to use and ensuring rigor and reproducibility, and facilitate the integration of data from knowledge base created in other resources such as [ASCT+B2](https://hubmapconsortium.github.io/ccf/pages/ccf-anatomical-structures.html). 

Note that the CellCard-Schema will also work closely with interoperable ontologies, which will provide standard representation of related terms and relations among the terms. 

For our first testing, the podocyte cell card example is used:  
https://cellcards.org/podocyte.php. 

### Cell Card Schema information:  
- Schema cellcard.yaml: https://github.com/CellCards/CellCard-Schema/blob/main/src/linkml/cellcard.yaml
- Data example (podocyte): https://github.com/CellCards/CellCard-Schema/blob/main/src/data/examples/podocyte-001.yaml
- Jupyter notebook example (podocyte): https://github.com/CellCards/CellCard-Schema/blob/main/notebooks/podocyte-linkml-example.ipynb
- CellCard Schema Documentation: https://cellcards.github.io/CellCard-Schema/CellCard/ 
- CellCard Schema Tutorial: https://cellcards.org/tutorial 

### Developers:  
- Bill Duncan
- Chris Mungall
- Oliver He
- Alex Diehl
- Sivaram Arabandi
- Jie Zheng

### A Similar Example: 
If you want to see LinkML in action you can look at the [NMDC Schema](https://microbiomedata.github.io/nmdc-schema/). The documentation and [jsonschema](https://github.com/microbiomedata/nmdc-schema/blob/main/jsonschema/nmdc.schema.json) were generated from the LinkML [nmdc.yaml](https://github.com/microbiomedata/nmdc-schema/blob/main/src/schema/nmdc.yaml) file. A similar approach would be used for the cell cards:

1. Define schema in LinkML (i.e., yaml files)
2. Generate jsonschema, ddl, rdf, documentation, etc. from the yaml files.
3. Deploy documentation.

Moreover, the generated jsonschema is used to validate data before inputting the data into the database.

