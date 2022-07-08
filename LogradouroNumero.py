"""
Created on Fri Jun 17 13:41:20 2022

@author: mano-K9

O algoritmo extrai o logradouro, o número e o complemento do endereco.
Nao há nada de AI ou ML neste codigo :)
Usa os tipos basicos de logradouro (rua, avenida, estrada, etc.), e nao o dominio completo dos correios.
Ver variável "self.tipoBasicoLogradouro"
A tabela completa de tipos de logradouro dos correios se encontra em:
http://portal.pmf.sc.gov.br/arquivos/arquivos/pdf/04_01_2010_10.27.25.2b615e6755138defe1bdb00f1c86031f.PDF
Sinta-se a vontade para complementar e incluir os tipos de logradouro para suas necessidades.
O algoritmo consegue extrair bem o numero e o complemento da maioria dos casos, mas não de 100% dos casos
Em uma base de amostragem interna (que não posso compartilhar), o percentual de acerto chegou a 97%
Obviamente, se o endereço estiver muito ruim, não espere milagre.
"""

"""
### EXEMPLO:
    
objLog = Logradouro()

print('')
print(objLog.numCmplto("rua da esquina s/n beco das flores"))
print('')
print(objLog.numCmplto("av. luis cartlos prestes, 150 apto 15"))
print('')
print(objLog.numCmplto("blv dos diamantes, 15 - casa 12"))

"""

"""
### RESULTADO DO CÓDIGO ACIMA:

['RUA DA ESQUINA', 'SN', 'BECO DAS FLORES']

['AV LUIS CARTLOS PRESTES', '150', 'APTO 15']

['BLV DOS DIAMANTES', '15', '- CASA 12']
"""

class Logradouro:
  def __init__(self):
# lista parcial dos tipos de logradouro
# consulte a lista completa dos correios para incluir algum tipo que vc acha importante
    self.tipoBasicoLogradouro = '.ALAMEDA.AL.AVENIDA.AV.RUA.R.ESTRADA.EST.TREVO.TRV.BULEVAR.BOULEVAR.BLV.VIA.TRAVESSA.TRAV.TVS.TRVSA.TV.'
    self.tipoBasicoLogradouroSemNumero = '.RODOVIA.ROD.RD.BR.KM.FAZENDA.FAZ.FZ.CHACARA.CHÁCARA.CHC.CHAC.SITIO.SÍTIO.ST.SIT.'
    self.tipoComplemento = '.QUADRA.QD.CONJUNTO.CJ.APARTAMENTO.AP.APTO.CASA.C.CS.BLOCO.BL.BLCO.CONDOMINIO.COND.CD.'
  def numCmplto(self, endereco):
    endrco = sEndrc = endereco.upper()
    num = ''
    cmplto = ''
    if type(sEndrc) == str:
        sEndrco = sEndrc.replace(',',' ').replace('.',' ').replace(':',' ')
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
            sLog1 = self.tipoBasicoLogradouro
            sLog2 = self.tipoBasicoLogradouroSemNumero
            sComp = self.tipoComplemento
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

