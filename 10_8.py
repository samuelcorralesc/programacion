val=int(input())
dia={0:"sabado",1:"domingo",2:"lunes",3:"martes",4:"miercoles",5:"jueves",6:"viernes"}
mes={"marzo":3,"abril":4,"mayo":5,"junio":6,"julio":7,"agosto":8,"septiembre":9,"octubre":10,"noviembre":11,"diciembre":12,"enero":13,"febrero":14}
for i in range(val):
  C=input().split("-")
  D=int(C[0])
  M=C[1]
  A=int(C[2])
  if M=="enero" or M=="febrero":
    F=(D+((13*(mes[M]+1))//5)+(A-1)+((A-1)//4)-(((A-1)//100))+((A-1)//400))%7
    print(dia[F])
  else:
    F=(D+((13*(mes[M]+1))//5)+A+(A//4)-((A//100))+((A)//400))%7
    print(dia[F])