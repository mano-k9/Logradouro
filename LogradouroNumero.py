# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 13:41:20 2022

@author: mano-K9

O algoritmo extrai o logradouro, o número e o complemento do endereco.
Nao há nada de AI ou ML neste codigo :)
Usa os tipos basicos de logradouro na variável sLog1 (rua, avenida, estrada, etc.), e nao o dominio completo dos correios.
Mas sinta-se a vontade para baixar em sua máquina e adaptar para atender a sua necessidade.
O algoritmo consegue extrair bem o numero e o complemento da maioria dos endereços, mas não de 100% dos casos
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
    endrco = sEndrc
    num = ''
    cmplto = ''
    if type(sEndrc) == str:
        sEndrco = sEndrc.upper().replace(',',' ').replace('.',' ').replace(':',' ')
        posNum = sEndrco.find(' SN')
        if posNum >-1:
            num = 'SN'
            endrco = sEndrc[0:posNum].replace(',','')
            cmplto = sEndrc[posNum+3:]
        else:
            posNum = sEndrco.find(' S/N')
            if posNum > -1:
                num = 'SN'
                endrco = sEndrc[0:posNum].replace(',','')
                cmplto = sEndrc[posNum+4:]
        if posNum == -1:
            spEndrco = sEndrco.split()
            i = 0
            sLog1 = '.ALAMEDA.AL.AVENIDA.AV.RUA.R.ESTRADA.EST.TREVO.TRV.TRAVESSA.TV.BULEVAR.BOULEVAR.BLV.TREVO.TRV.TRAVESSA.TV.'
            sLog2 = '.RODOVIA.ROD.RD.BR.KM.FAZENDA.FAZ.FZ.CHACARA.CHÁCARA.CHC.CHAC.SITIO.SÍTIO.ST.SIT.'
            sComp = '.QUADRA.QD.CONJUNTO.CJ.APARTAMENTO.AP.APTO.CASA.C.CS.BLOCO.BL.BLCO.CONDOMINIO.COND.CD.'
            via = (sLog1.find(spEndrco[0]) > -1)
            naoVia = (sLog2.find(spEndrco[0]) > -1)
            comp = False
            if via:
                endrco = ''
                for stEnd in spEndrco:
                    if not comp:
                        comp = (sComp.find('.' + stEnd + '.') > -1)
                    if comp:
                        cmplto += (stEnd + ' ')
                    elif stEnd.isdigit() and i > 1:
                        num = stEnd
                        break
                    elif '.N.NO.NUM.NUMERO.NÚMERO.'.find('.' + stEnd + '.'):
                        endrco += (stEnd + ' ')
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
        posNum = sEndrc.find(num)
        if endrco == sEndrc:
            endrco = sEndrc[0:posNum].replace(',','').strip()
        posNum += len(num) + 1
        if cmplto == '':
            cmplto = sEndrc[posNum:]
    return([endrco.strip(),num,cmplto.strip()])
