import dissasembler
import simulator

mydis = dissasembler.Dissasembler()
output = {}
output = mydis.run()

# TODO: The numbers after the extra lines (232-272) correct?
mydis.print()
print(output)

# mysim= simulator.Simulator(output.instructions,output.opcode,output.dataval,output.address,output.arg1,output.arg2,output.arg3,output.numInstructs,output.opcodeStr,output.arg1Str,output.arg2Str,output.arg3Str)
mysim = simulator.Simulator(**output)
mysim.run()
