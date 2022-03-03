import pandapower as pp
import pandapower.plotting as plot
import random

# maxLoad=50kW, minLoad=25kW
def new_network(minLoad=0.015, maxLoad=0.100, medidores:list=[65]) -> pp.pandapowerNet:
    net = pp.create_empty_network()

    pp.create_bus(net, 13.8, index=00, geodata=(55,1022), name='SE')
    pp.create_bus(net, 13.8, index=64, geodata=(182,1022))
    pp.create_bus(net, 13.8, index=65, geodata=(322,1022))
    pp.create_bus(net, 13.8, index=66, geodata=(454,1022))
    pp.create_bus(net, 13.8, index=67, geodata=(593,1022))
    pp.create_bus(net, 13.8, index=68, geodata=(698,1022))
    pp.create_bus(net, 13.8, index=69, geodata=(818,1022))
    pp.create_bus(net, 13.8, index=70, geodata=(960,740))
    pp.create_bus(net, 13.8, index=71, geodata=(1100,740))
    pp.create_bus(net, 13.8, index=72, geodata=(960,1304))
    pp.create_bus(net, 13.8, index=73, geodata=(960,1022))
    pp.create_bus(net, 13.8, index=74, geodata=(1100,1022))
    pp.create_bus(net, 13.8, index=75, geodata=(1232,1022))
    pp.create_bus(net, 13.8, index=76, geodata=(1232,740))
    pp.create_bus(net, 13.8, index=77, geodata=(818,740))
    pp.create_bus(net, 13.8, index=78, geodata=(818,1304))
    pp.create_bus(net, 13.8, index=79, geodata=(454,740))
    pp.create_bus(net, 13.8, index=80, geodata=(454,1304))
    pp.create_bus(net, 13.8, index=81, geodata=(593,1304))
    pp.create_bus(net, 13.8, index=82, geodata=(322,450))
    pp.create_bus(net, 13.8, index=83, geodata=(454,450))
    pp.create_bus(net, 13.8, index=84, geodata=(454,160))

    pp.create_ext_grid(net, bus=0, vm_pu=1.00, name='SE')

    pp.create_line(net, index=64, from_bus=00, to_bus=64, length_km=5.0, std_type='94-AL1/15-ST1A 20.0', geodata=((55,1022),(182,1022)))
    pp.create_line(net, index=82, from_bus=64, to_bus=82, length_km=5.0, std_type='94-AL1/15-ST1A 20.0', geodata=((182,1022),(322,450)))
    pp.create_line(net, index=83, from_bus=82, to_bus=83, length_km=5.0, std_type='94-AL1/15-ST1A 20.0', geodata=((322,450),(454,450)))
    pp.create_line(net, index=84, from_bus=82, to_bus=84, length_km=5.0, std_type='94-AL1/15-ST1A 20.0', geodata=((322,450),(454,160)))
    pp.create_line(net, index=65, from_bus=64, to_bus=65, length_km=5.0, std_type='94-AL1/15-ST1A 20.0', geodata=((182,1022),(322,1022)))
    pp.create_line(net, index=79, from_bus=65, to_bus=79, length_km=5.0, std_type='94-AL1/15-ST1A 20.0', geodata=((322,1022),(454,740)))
    pp.create_line(net, index=80, from_bus=65, to_bus=80, length_km=5.0, std_type='94-AL1/15-ST1A 20.0', geodata=((322,1022),(454,1304)))
    pp.create_line(net, index=81, from_bus=80, to_bus=81, length_km=5.0, std_type='94-AL1/15-ST1A 20.0', geodata=((454,1304),(593,1304)))
    pp.create_line(net, index=66, from_bus=65, to_bus=66, length_km=5.0, std_type='94-AL1/15-ST1A 20.0', geodata=((322,1022),(454,1022)))
    pp.create_line(net, index=67, from_bus=66, to_bus=67, length_km=5.0, std_type='94-AL1/15-ST1A 20.0', geodata=((454,1022),(593,1022)))
    pp.create_line(net, index=68, from_bus=67, to_bus=68, length_km=5.0, std_type='94-AL1/15-ST1A 20.0', geodata=((593,1022),(698,1022)))
    pp.create_line(net, index=77, from_bus=68, to_bus=77, length_km=5.0, std_type='94-AL1/15-ST1A 20.0', geodata=((698,1022),(818,740)))
    pp.create_line(net, index=78, from_bus=68, to_bus=78, length_km=5.0, std_type='94-AL1/15-ST1A 20.0', geodata=((698,1022),(818,1304)))
    pp.create_line(net, index=72, from_bus=78, to_bus=72, length_km=5.0, std_type='94-AL1/15-ST1A 20.0', geodata=((818,1304),(960,1304)))
    pp.create_line(net, index=69, from_bus=68, to_bus=69, length_km=5.0, std_type='94-AL1/15-ST1A 20.0', geodata=((698,1022),(818,1022)))
    pp.create_line(net, index=70, from_bus=69, to_bus=70, length_km=5.0, std_type='94-AL1/15-ST1A 20.0', geodata=((818,1022),(960,740)))
    pp.create_line(net, index=71, from_bus=70, to_bus=71, length_km=5.0, std_type='94-AL1/15-ST1A 20.0', geodata=((960,740),(1100,740)))
    pp.create_line(net, index=73, from_bus=69, to_bus=73, length_km=5.0, std_type='94-AL1/15-ST1A 20.0', geodata=((818,1022),(960,1022)))
    pp.create_line(net, index=74, from_bus=73, to_bus=74, length_km=5.0, std_type='94-AL1/15-ST1A 20.0', geodata=((960,1022),(1100,1022)))
    pp.create_line(net, index=76, from_bus=74, to_bus=76, length_km=5.0, std_type='94-AL1/15-ST1A 20.0', geodata=((1100,1022),(1232,740)))
    pp.create_line(net, index=75, from_bus=74, to_bus=75, length_km=5.0, std_type='94-AL1/15-ST1A 20.0', geodata=((1100,1022),(1232,1022)))

    buses = net.bus.loc[net.bus['name']!='SE'].index
    p_mws = [random.uniform(minLoad, maxLoad) for i in range(len(buses))]
    pp.create_loads(net, buses, p_mw=p_mws)
    
    # barras com medidores
    for id, row in net.line.iterrows():
        if id in medidores:
            pp.create_switch(net, index=id, bus=id, element=id, et='l', closed=True, type='LS', name=str(id))
        else:
            pp.create_switch(net, index=id, bus=id, element=id, et='l', closed=True, type='LBS', name=str(id))

    return net

if __name__ == "__main__":
    net = new_network()
    #pp.to_json(net,'p64.json')
    pp.runpp(net)
    print(net.res_bus)      
    # index vm_pu va_degree p_mw q_mvar
    print(net.res_line)     
    # index p_from_mw q_from_mvar p_to_mw q_to_mvar pl_mw ql_mvar i_from_ka i_to_ka i_ka vm_from_pu va_from_degree vm_to_pu va_to_degree loading_percent
    plot.simple_plot(net, respect_switches=True,plot_line_switches=True)
