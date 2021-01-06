segundo_str = int (input("Por favor, entre com o numero de segundos que deseja converter: "))


dias = segundo_str // 86400
segundo_restante = segundo_str % 86400
horas = segundo_restante // 3600
segs_restantes = segundo_str % 3600
minuto = segs_restantes // 60
segs_restante_final = segs_restantes % 60


print(dias,"dias,",horas,"horas,",minuto,"minutos e",segs_restante_final,"segundos.")