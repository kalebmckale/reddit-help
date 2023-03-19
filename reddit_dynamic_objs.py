"""
Create object dynamically

Hello,

I have following code:

            eleventh=source(rate=.93,eta=1,name="eleventh")
            twelveth=source(rate=.96,eta=1,name="twelveth")
            thirteen=source(rate=.96,eta=1,name="thirteen")
            fourteen=source(rate=.96,eta=1,name="fourteen")
            fifteen=source(rate=.96,eta=1,name="fifteen")
    
            zz=link(eta=eta6, deltat=link_dt2, inputs=eleventh.portA)
            zzp=link(eta=eta6, deltat=link_dt2, inputs=eleventh.portB)
            tw=link(eta=eta6, deltat=link_dt2, inputs=twelveth.portA)
            twp=link(eta=eta6, deltat=link_dt2, inputs=twelveth.portB)
            thr=link(eta=eta6, deltat=link_dt2, inputs=thirteen.portA)
            thrp=link(eta=eta6, deltat=link_dt2, inputs=thirteen.portB)
            ften=link(eta=eta6, deltat=link_dt2, inputs=fourteen.portA)
            ftenp=link(eta=eta6, deltat=link_dt2, inputs=fourteen.portB)
            fif=link(eta=eta6, deltat=link_dt2, inputs=fifteen.portA)
            fifp=link(eta=eta6, deltat=link_dt2, inputs=fifteen.portB)
    
            Minport=node(t0=0, tmem=i, bits=zz, physsize=j, dt=dt3and4,name='M') 
            Mpinport=node(t0=0, tmem=i, bits=zzp, physsize=j, dt=dt3and4, port=Minport,name='Nprime')  
            Ninport=node(t0=0, tmem=i, bits=tw, physsize=j, dt=dt3and4,name='N') 
            Npinport=node(t0=0, tmem=i, bits=twp, physsize=j, dt=dt3and4, port=Ninport,name='Nprime') 
            Oinport=node(t0=0, tmem=i, bits=thr, physsize=j, dt=dt3and4,name='O') 
            Opinport=node(t0=0, tmem=i, bits=thrp, physsize=j, dt=dt3and4, port=Oinport,name='Oprime')  
            Pinport=node(t0=0, tmem=i, bits=ften, physsize=j, dt=dt3and4,name='P') 
            Ppinport=node(t0=0, tmem=i, bits=ftenp, physsize=j, dt=dt3and4, port=Pinport,name='Pprime')  
            Rinport=node(t0=0, tmem=i, bits=fif, physsize=j, dt=dt3and4,name='R') 
            Rpinport=node(t0=0, tmem=i, bits=fifp, physsize=j, dt=dt3and4, port=Rinport,name='Rprime') 
    

As you can see, each part has some input from the other parts and I need to go to till 100, and I do not want to write 100 lines one by one. However I know that giving dynamic name can be problematic. Do you have any suggestion for it?
"""
from string import ascii_uppercase


class Source:
    def __init__(self, name, rate, eta):
        self._name = name
        self._rate = rate
        self._eta = eta
        self._source = source(rate=self._rate, eta=self._eta, name=self._name)

    def link_source(self, eta, deltat):
        self._link = link(eta=eta, deltat=deltat, inputs=self._source.portA)
        self._prime_link = link(eta=eta, deltat=deltat, inputs=self._source.portB)

    def set_nodes(self, t0, tmem, physsize, dt):
        self._node = node(
            t0=t0, tmem=tmem, bits=self._link, physsize=j, dt=dt, name=self._name
        )
        self._prime_node = node(
            t0=t0,
            tmem=tmem,
            bits=self._prime_link,
            physsize=j,
            dt=dt,
            name=f"{self._name}_prime",
        )


sources = {
    letter: Source(name=letter, rate=0.96, eta=1)
    for letter in ascii_uppercase
}
for letter, src in sources.items():
    src.link_source(eta=eta6, deltat=link_dt2)
    src.set_nodes(t0=0, tmem=i, physsize=j, dt=dt3and4)
