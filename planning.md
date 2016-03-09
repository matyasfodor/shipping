mikor van kesz?
Ha elfogynak a rendelesek -> Teljesitett utasitas eseten penzt hozzaadni, kitorolni az objektumot, vagy csokkenteni kell a vart erteket ha nem a teljes szallitmany

Reprezentaciok:
-korokre van osztva
kikoto objektumok vannak, illetve hajo objektumok
a hajok mindig kiteszik az oszes szallitmanyukat, hiszen csak ket kikoto kozott ingaznak
a hajo objektumbol egyszeru mod-dal kiszedheto, hogy hol tart epp. Ha utkozben van: None, ha epp celba ert, a kikoto neve
az rendeleseket el kell erni source szerint -> inicializalas, es target szerint -> ez az element torleshez
az objektumot tenylegesen nem torolom, hanem deleted flag-gel latom el
van szallitmany reprezentacio, amely oszthato ket reszre, ha nem fer fol minden a hajora

egy kor a kovetkezo keppen nez ki:
    minden hajot leptetek
    ha egy hajo kikotobe er, kipakolok mindent
        ha a targetbe ert, egyszeruen levonodik/torlodik az a rendeles
        egyebkent a kikoto belso raktaraba kerul eltarolasra
    eldontom, hogy mit pakolok be (ebbol lesznek az utasitasok):
        ha van olyan rakomany, ami pont a hajo targetje, akkor bepakolom (lejarat szerint rendezve, ha meg idoben odaer)
        csak olyan szallitmanyt teszek a hajora, ami nem pont akkor erkezett
        !!!Problema: Egyszerre tobb hajo is lehet a kikotoben, igy eloszor mindig a kipakolassal kell kezdeni, elhelyezni a cuccot, majd utana bepakolni (ugyanarra a hajora nem szabad visszapakolni)

MVP:
menetrend: 
    -> hajo objektum 
    -> leptetes 
    -> megmondja, hol van
szallitmany: 
    -> hajora folpakolas (nem a logika, csak funkcionalitas) 
    -> lepakolas 
    -> osztas, ha nem fer fol.
main loop: 
    -> hajok leptetese 
    -> hajok csoportositasa kikoto szerint 
    -> ido leptetese
kikoto: 
    ->inicializalas rendeles alapjan 
    -> inicializalas menetrend alapjan (lehet olyan kikoto ahol nincs rendeles?) 
    -> rendeles alapjan szallitmany raktar letrehozasa 
    -> hajo felpakolas MVP - random - (ez lesz a fo logika, de meg csak buta) 
    -> hajok lepakolasa, majd felpakolasa 
    -> lepakolas eseten osszenezni a rendelessel, torolni/csokkenteni az allomanyt 
    -> felpakolas soran utasiast letrehozni 
    -> utasitast exportalni 
    -> felpakolas soran ugyanarra a hajora nem pakolni (ez mar okositas) 
    -> felpakolas soran figyelembe venni a bonuszt + targetet, ez alapjan priorizalni
main: 
    -> utasitas listat exportalni, rendezni
