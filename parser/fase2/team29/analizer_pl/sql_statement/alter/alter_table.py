from analizer_pl.abstract import instruction
from analizer_pl.statement.expressions import code
from analizer_pl.reports.Nodo import Nodo
from analizer_pl.abstract.environment import Environment


class AlterTable(instruction.Instruction):
    def __init__(self, table, row, column, params=[]):
        instruction.Instruction.__init__(self, row, column)
        self.table = table
        self.params = params

    def execute(self, environment):
        out = "fase1.execution(dbtemp + "
        out += '" '
        out += "ALTER "
        out += "TABLE "
        out += self.table + " "
        out += self.params
        out += ";"
        out += '")\n'
        if isinstance(environment, Environment):
            out = "\t" + out
        return code.C3D(out, "alter_db", self.row, self.column)

    def dot(self):
        return Nodo("SQL_INSTRUCTION:_ALTER_TABLE")