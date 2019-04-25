def leiaDinheiro(n):
    while True:
        try:
            a = float(input(n))
            return a
        # PRECISO ARRUMAR ESSA EXCEPT PRA FICAR IGUAL DA AULA,
        # MAS FUNCIONA PERFEITAMENTE COM TRY EXCEPT
        except BaseException as b:
            print("AVISO:", b)
