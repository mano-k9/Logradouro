# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 13:41:20 2022

@author: mano-K9

O algoritmo extrai o número e o complemento do endereco.
Nao há nada de AI ou ML neste codigo :)
Usa os tipos basicos de logradouro na variável sLog1 (rua, avenida, estrada, etc.), e nao o dominio completo dos correios.
Mas sinta-se a vontade para complementar e adaptar para atender a sua necessidade.
O algoritmo consegue extrair bem o numero e o complemento da maioria dos endereço, mas não de 100% dos casos
Em uma base de amostragem interna (que não posso compartilhar), o percentual de acerto chegou a 97%
Obviamente, se o endereço estiver muito ruim, não espere milagre.
"""

"""
### EXEMPLO:
    
endereco = "AVENIDA VITORINO NONATO, 110  CASA 18"
objLog = Logradouro(endereco)
numeroComplemento = objLog.numCmplto()
print(numeroComplemento)

"""

class Logradouro:
  def __init__(self, endrco):
    self.endrco = endrco
  def numCmplto(self):
    sEndrc = self.endrco
    num = ''
    cmplto = ''
    if type(sEndrc) == str:
        sEndrco = sEndrc.upper().replace(',',' ').replace('.',' ').replace(':',' ')
        if sEndrco.find(' SN') >-1 or sEndrco.find(' S/N') > -1:
            num = 'SN'
        else:
            spEndrco = sEndrco.split()
            i = 0
            sLog1 = '.ALAMEDA.AL.AVENIDA.AV.RUA.R.ESTRADA.EST.TREVO.TRV.TRAVESSA.TV.BULEVAR.BOULEVAR.BLV.TREVO.TRV.TRAVESSA.TV.'
            sLog2 = '.RODOVIA.ROD.RD.BR.QUADRA.QD.CONJUNTO.CJ.APARTAMENTO.AP.APTO.KM.FAZENDA.FAZ.FZ.CHACARA.CHÁCARA.CHC.CHAC.SITIO.SÍTIO.ST.SIT.'
            via = (sLog1.find(spEndrco[0]) > -1)
            naoVia = (sLog2.find(spEndrco[0]) > -1)
            if via:
                for stEnd in spEndrco:
                    if stEnd.isdigit():
                        if i > 1:
                            num = stEnd
                            break
                        if i > 1:
                            num = stEnd
                            break
                    i += 1
            elif naoVia:
                num = ''
            else:
                for stEnd in spEndrco:
                    if stEnd.isdigit():
                        if i > 0:
                            num = stEnd
                            break                        
                    i += 1
    if num != '':
        posNum = sEndrc.find(num) + len(num) + 1
        cmplto = sEndrc[posNum:].strip()
    return([num,cmplto])

