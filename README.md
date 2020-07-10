# Automated-Bioportal-Annotator
This Python script iterates a list of terms over the Bioportal API's Annotator tool and returns a table with detailed ontology annotations. 
Each entry on the table also specifies the annotation IRI, its Ontology, and a value for how complete the annotation was in relation to the term (Complete, Component, Partial). A typical result file should look like this:

| Term        | Match           | Completeness  | Ontology | IRI|
| ------------- |:-------------:|:-------------:|:-------:|:-------------:|
|depression	|depression	|Complete	|HP	|http://purl.obolibrary.org/obo/HP_0000716|
|spasticity	|tongue spasticity	|Partial	|HP|	http://purl.obolibrary.org/obo/HP_0001257|
|hyporeflexia	|hyporeflexia	|Complete|	HP	|http://purl.obolibrary.org/obo/HP_0001265|
|bulbar palsy	|progressive bulbar palsy|Component	|HP|	http://purl.obolibrary.org/obo/HP_0001283	|




### How do I use this?
You must have the **requests** and **urllib** Python modules installed.

Open the script, fill out the variables for:
- __apikey -__ A valid Bioportal user API key (requires a Bioportal account)
- __term_path -__ A path to a .txt file with a list of terms
- __result_path -__ A path to a .csv file to write your results
- __ontologies -__ A list of comma-separated ontologies (must be Bioportal acronyms) you want to use for the annotation process

and run it.


### Can I have some test data?
A Terms.txt file detailing a list of terms for medical symptoms and body regions is provided.
