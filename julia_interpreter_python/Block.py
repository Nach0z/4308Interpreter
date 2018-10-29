class Block:

    def __init__(self):
        self.stmt_list = []

    def get_list(self):
        return self.stmt_list

    def add(self, stat):
        self.stmt_list.append(stat)

    def execute(self):
    	for stmt in self.stmt_list:
    		stmt.execute()



