import pandapower as pp
import numpy

# linhas com medição de corrente
def __LinesCurrId(net:pp.pandapowerNet) -> list:
    chaves_med = (net.switch['type'] == 'LS') & (net.switch['et'] == 'l')
    return net.switch.loc[chaves_med,'element']

# correntes salvas originais
def CurrSaved(net:pp.pandapowerNet) -> dict:
    LinesID = __LinesCurrId(net)
    # fluxo de potencia sem falhas
    pp.runpp(net, neglect_open_switch_branches=True)
    ikaN = net.res_line.loc[LinesID,'i_ka'].fillna(0).values
    # corrente original total do circuito
    pattern = {0:ikaN}
    # inserindo falhas e obtendo novo fluxo
    for sw_id, r in net.switch.iterrows():
        net.switch.at[sw_id, 'closed'] = False
        pp.runpp(net, neglect_open_switch_branches=True)
        net.switch.at[sw_id, 'closed'] = True
        ikaF = net.res_line.loc[LinesID,'i_ka'].fillna(0).values
        # identificando região por maior variação de carga
        z = (ikaN - ikaF) / ikaN
        # desde que a corrente não vá a ZERO 
        local = [[id,falha] for _, _, falha, id in sorted(zip(z, ikaN, ikaF, LinesID), reverse=True) if falha > 0.0]
        # I_saved
        if len(local) == 0:
            pattern[sw_id] = [LinesID.values[0],0.0]
        else:
            pattern[sw_id] = local[0]
    return pattern

# corrente salvas ajustadas
def CurrSavedNew(net:pp.pandapowerNet, I_saved:dict) -> dict:
    # corrente original
    Io = I_saved[0]
    pp.runpp(net, neglect_open_switch_branches=True)
    # corrente pre-falta
    LinesID = __LinesCurrId(net)
    Ipf = net.res_line.loc[LinesID,'i_ka'].fillna(0).values
    # lista de ajustes por medidor
    ajuste = dict(zip(LinesID, (Ipf / Io))) 
    # novo padrão de faltas
    new_pattern = {}
    for key in I_saved.keys():
        if key == 0:
            new_pattern[key] = Ipf
        else:
            new_pattern[key] = [ I_saved[key][0], I_saved[key][1] * ajuste[I_saved[key][0]] ]
    return new_pattern

def FaultDetect(net:pp.pandapowerNet, I_saved:dict) -> list:
    # posição das chaves com medição nas linhas
    LinesID = __LinesCurrId(net)
    # medições
    ika = net.res_line.loc[LinesID,'i_ka'].fillna(0).values
    faults = dict(zip(LinesID, ika))
    # identificando medicao com valor proximo
    list_saved = list(I_saved.items())[1:]
    min_diff = sorted(list_saved, key=lambda x: numpy.linalg.norm(x[1][1] - faults[x[1][0]]))
    # retornando a lista de chaves prováveis
    fault_best = [ sw for sw, _ in min_diff]
    return fault_best
