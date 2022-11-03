import TeacherCRUD as tt
from db.database import Graph
from helper.write_a_json import write_a_json as wj

if __name__ == '__main__':
    db = Graph(uri='bolt://54.152.81.182:7687', user='neo4j', password='acceptors-reports-supermarkets')




def criar_nos():
    query = [
        'CREATE(:Teacher{name:"Rosana",ano_nasc:1970,cpf:"321.654.987-00"})',
        'CREATE(:Teacher{name:"Guilherme",ano_nasc:1990,cpf:"111.222.333-03"});',
        'CREATE(:Teacher{name:"Justino",ano_nasc:1930,cpf:"444.555.666-05"})',
        'CREATE(:Teacher{name:"Karina",ano_nasc:1988,cpf:"213.456.897-01"})',
        'CREATE(:Teacher{name:"Rosimara",ano_nasc:1966,cpf:"231.465.879-02"})',
        'CREATE(:Teacher{name:"Renzo",ano_nasc:1986,cpf:"999.888.777-04"})',
        'CREATE(:School{name:"ETE FMC",address:"Av. Sinhá Moreira",number:350})',
        'CREATE(:School{name:"Inatel",address:"Av. João de Camargo",number:510})',
        'CREATE(:School{name:"Grupão",address:"Praça Dr. Américo Lopes",number:00})',
        'CREATE(:School{name:"YPE",address:"R. Prof. Francisco Ribeiro de Magalhães",number:10})',
        'CREATE(:City{name:"Santa Rita do Sapucai", cep:"37540-000", population: 43260})',
        'CREATE(:City{name:"Alfenas", cep:"35617-000", population: 80973})',
        'CREATE(:City{name:"Poços de Caldas", cep:"13737-635", population: 169838})',
        'CREATE(:State{name:"Minas Gerais", country:"Brasil"})'
    ]
    for q in query:
        db.write(query=q)

    def criar_relacionamentos():
        query = [
            'MATCH(p:Teacher{name:"Renzo"}),(s:School{name:"YPE"}) CREATE(t)-[:WORKS]->(s)',
            'MATCH(p:Teacher{name:"Justino"}),(s:School{name:"Grupão"}) CREATE(t)-[:WORKS]->(s)',
            'MATCH(p:Teacher{name:"Rosana"}),(s:School{name:"ETE FMC"}) CREATE(t)-[:WORKS]->(s)',
            'MATCH(p:Teacher{name:"Guilherme"}),(s:School{name:"ETE FMC"}) CREATE(t)-[:WORKS]->(s)',
            'MATCH(p:Teacher{name:"Karina"}),(s:School{name:"Inatel"}) CREATE(t)-[:WORKS]->(s)',
            'MATCH(p:Teacher{name:"Rosimara"}),(s:School{name:"ETE FMC"}) CREATE(t)-[:WORKS]->(s)',
            'MATCH(s:School{name:"Inatel"}),(c:City{name:"Santa Rita do Sapucai"}) CREATE(s)-[:LOCATES]->(c)',
            'MATCH(s:School{name:"ETE FMC"}),(c:City{name:"Santa Rita do Sapucai"}) CREATE(s)-[:LOCATES]->(c)',
            'MATCH(s:School{name:"YPE"}),(c:City{name:"Alfenas"}) CREATE(s)-[:LOCATES]->(c)',
            'MATCH(s:School{name:"Grupão"}),(c:City{name:"Poços de Caldas"}) CREATE(s)-[:LOCATES]->(c)',
            'MATCH(c:City{name:"Santa Rita do Sapucai"}),(st:State{name:"Minas Gerais"}) CREATE(c)-[:BELONGS]->(st)',
            'MATCH(c:City{name:"Alfenas"}),(st:State{name:"Minas Gerais"}) CREATE(c)-[:BELONGS]->(st)',
            'MATCH(c:City{name:"Poços de Caldas"}),(st:State{name:"Minas Gerais"}) CREATE(c)-[:BELONGS]->(st)'
        ]
        for q in query:
            db.write(query=q)

    # LIMPANDO GRAFO
    def limpar_grafo():
        db.execute_query("MATCH(n) DETACH DELETE n;")

    # EXECUTANDO
    def executar():
        limpar_grafo()
        criar_nos()
        criar_relacionamentos()

    executar()

    # Questão 01
    # A
    wj(db.execute_query("MATCH(p:Teacher{name:'Renzo'}) RETURN p.ano_nasc, p.cpf;"), 'A')
    # B
    wj(db.execute_query("MATCH(p:Teacher) WHERE p.name STARTS WITH 'M' RETURN p.name, p.cpf;"), 'B')
    # C
    wj(db.execute_query("MATCH(c:City) RETURN c.name"),'C')
    # D
    wj(db.execute_query("MATCH(e:School) WHERE e.number >= 150 AND e.number <= 550 RETURN e.name, e.address"), 'D')

    # Questão 02
    # A
    wj(db.execute_query("MATCH(p:Teacher) return MIN(p.ano_nasc), MAX(p.ano_nasc)"), 'A')
    # B
    wj(db.execute_query("MATCH(c:City) return AVG(c.population)"), 'B')
    # C
    wj(db.execute_query("MATCH(c:City) WHERE c.cep = '37540-000' RETURN REPLACE(c.name, 'a', 'A')"), 'C')
    # D
    wj(db.execute_query("MATCH(p:Teacher) RETURN SUBSTRING(p.name, 3, 1)"), 'D')


    # Questão 03
    # A - criado no import 'as tt'
    # B
    tt.create('Chris Lima', 1956, '189.052.396-66')
    # C
    tt.read('Chris Lima')
    # D
    tt.update('Chris Lima', '162.052.777-77')

