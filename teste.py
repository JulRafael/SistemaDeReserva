import function

reservas2 = function.getReservas()
matriz = function.FazMatrizParaRelatorioCadeirasLivres()
novamatriz = function.RetiraDaMatriz(matriz,reservas2)
function.AdcionaEmRelatorioCadeirasLivres(novamatriz)

for c in range(12):
    for x in range(8):
        for y in range(len(reservas2)):
            if (str(matriz[c][x]) == reservas2[y]):
                matriz[c][x] = "[***]"