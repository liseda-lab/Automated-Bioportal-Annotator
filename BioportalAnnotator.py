from urllib import parse
import requests

def get_annotation(api_key,term_path,ontologies,directory):
    #This function only searches ontologies without synonims due to often redundant and meaningless labeling of classes. The updated version also stores all results in a seperate file.
    #Requires string 'terms' string form patient file, string 'ontologies' with the Ontologies used to annotate terms,string 'directory' with path to store annotation results

    with open(term_path) as data:
        terms = data.read().splitlines() 

    api_key = api_key
    site = 'http://data.bioontology.org/annotator?'
    All_Results = open(directory,"w") 
    All_Results.write("Match;Term;Completeness;Ontology;IRI" + '\n')
    
    for term in terms:
        print("'"+term+"'")
        for ontology in ontologies.split(","):
            parms = '&format=json&include=prefLabel&text='
            UsedOntology=str('&ontologies='+ontology)
            text = parse.quote(term)
            URL = site + "apikey="+ api_key + UsedOntology + parms + text
            data = requests.get(URL)
             
            if data.status_code == 200:
                Results=data.json()
                if Results==[]:
                    continue
                for Match in Results:                      
                    Class = Match['annotatedClass']
                    Annotations = Match['annotations']

                    #Find Basic Match Information
                    Label=str(Annotations[0]['text'])
                    IRI=Class["@id"]

                    #Find Term-Match completeness
                    term=term.lower().strip()
                    Label=Label.lower()

                    if term==Label:#When an annotation matches the text term fully
                        Completeness='Complete'
                    elif Label in term:#When an annotation matches part of the text term
                        if len(Label.split(' '))>1:
                            Completeness='Component'
                        else:
                            Completeness='Partial'
                    
                    #Extra info about the scoring
                    Covered=(int(Annotations[0]['to'])-int(Annotations[0]['from'])+int(Annotations[0]['from']))/int(len(term))
                    #Synonim=Annotations[0]['matchType']

                    #Write Results
                    All_Results.write(Label+';'+term+';'+Completeness+';'+ontology+';'+str(IRI)+'\n')
                    #print(Label+';'+term+';'+Completeness+';'+ontology+';'+str(IRI)+';'+Synonim+';'+str(Covered)+'\n')
    All_Results.close()


#Fill out variables below before running code
result_path="C:/...../Results.csv"
api_key='.....'
term_path="C:/...../terms.txt"
ontologies="HP,UBERON"
get_annotation(api_key,term_path,ontologies,result_path)

