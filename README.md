# Logradouro

### Código em Python.
### O algoritmo extrai o logradouro, o número e o complemento do endereço.
### Não há nada de AI ou ML neste código :)
### Usa os tipos básicos de logradouro na variável sLog1 (rua, avenida, estrada, etc.), e não o domínio completo dos correios.
### Mas sinta-se a vontade para complementar e adaptar para atender a sua necessidade.
### O algoritmo consegue extrair bem o numero e o complemento da maioria dos endereços, mas não de 100% dos casos.
### Em uma base de amostragem interna (que não posso compartilhar), o percentual de acerto chegou a 97%.
### Obviamente, se o endereço estiver muito ruim, não espere milagre.

### EXEMPLO
### O código abaixo irá criar o array numeroComplemento com três elementos:
### ['AVENIDA VITORINO NONATO','110','CASA 18']
    
endereco = "AVENIDA VITORINO NONATO, 110  CASA 18"

objLog = Logradouro(endereco)

numeroComplemento = objLog.numCmplto()

print(numeroComplemento)
