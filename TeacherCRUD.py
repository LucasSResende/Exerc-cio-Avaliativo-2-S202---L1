from db.database import Graph
from helper.write_a_json import write_a_json as wj



class TeacherCRUD():

    def __init__(self):
        self.db = Graph(uri='bolt://1.2.3.4:5678', user='neo4j', password='pass-word-easy')

    def create(self, name, ano_nasc, cpf):
        return wj(self.db.execute_query('CREATE (p:Teacher {name:$name, ano_nasc:$ano_nasc, cpf:$cpf}) return p', {'name': name, 'ano_nasc': ano_nasc, 'cpf': cpf}), 'create')

    def read(self, name):
        return wj(self.db.execute_query('MATCH (p:Teacher {name:$name}) return p', {'name': name}), 'read')

    def update(self, name, newCpf):  # atualiza cpf com base no name`
        return wj(self.db.execute_query('MATCH (p:Teacher {name:$name}) SET p.cpf = $cpf RETURN p', {'name': name, 'cpf': newCpf}), 'update')

    def delete(self, name):  # deleta Teacher com base no name`
        return wj(self.db.execute_query('MATCH (p:Teacher {name:$name}) DELETE p', {'name': name}), 'delete')


