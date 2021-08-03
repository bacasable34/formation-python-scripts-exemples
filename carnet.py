#! /usr/bin/env python3
# programme carnet.py

# import du module datetime utilisé dans la class Personne pour calculer l'âge avec la date de naissance
import datetime

class Contact:
    #attribut de la class Contact
    nb_contact =0
    # __init__ dunder init est le constructeur de la class --> qd tu fais c1=Contact('0312050623','5 rue du chemin','France'
    def __init__(self,telephone=None, adresse=None, pays='France'):
        self.telephone = telephone
        self.adresse = adresse
        self.pays = pays
        Contact.nb_contact+=1
    # __del__ dunder del est le destructeur de la classe --> qd tu fais c1.__del__()
    def __del__(self):
        Contact.nb_contact-=1
    # __repr__ dunder repr est la sortie print --> qd tu fais p1 pour afficher son contenu
    def __repr__(self):
        return("tel:" + str(self.telephone) +
               ", adr:" + str(self.adresse) +
               ", pays:" + str(self.pays) +
               ", Cnombre:" + str(Contact.nb_contact))


# class Personne fille de la class Contact
class Personne(Contact):
    # attribut de la class Personne
    nombre=0

    # __init__ dunder init est le constructeur de la class --> qd tu fais p1=Personne('Mike','Nom','49','0312050623','5 rue du chemin','France'
    def __init__(self, nom='Doe',prenom='John',age=33, telephone=None, adresse=None, pays=None):
        super().__init__(telephone,adresse,pays)
        self.nom = nom
        self.prenom = prenom
        self.age = age
        Personne.nombre+=1

    # __del__ dunder del est le destructeur de la classe --> qd tu fais p1.__del__()
    def __del__(self):
        super().__del__()
        Personne.nombre-=1

    def __repr__(self):
        return ("nom:"   + str(self.nom) +
                ", prenom:" + str(self.prenom) +
                ", age:" + str(self.age) +
                ", Pnombre: " + str(Personne.nombre) + "\n" +
                super().__repr__())
    #getteur
    def _get_annee_naissance(self):
        return datetime.date.today().year - self.age
    #setteur
    def _set_annee_naissance(self, annee_naissance):
        self.age=datetime.date.today().year - annee_naissance
    #property qui utilise le getteur et le setteur
    annee_naissance=property(_get_annee_naissance,_set_annee_naissance)


class Organisation(Contact):
    nombre=0

    def __init__(self, telephone=None, adresse=None, pays=None, raison='World Company'):
        super().__init__(telephone, adresse,pays)
        self.raison = raison
        Organisation.nombre+=1
    def __del__(self):
        super().__del__()
        Organisation.nombre-=1
    def __repr__(self):
        return ("raison sociale:"   + str(self.raison) +
                ", Onombre: " + str(Organisation.nombre) + "\n" +
                super().__repr__())

#test du module
if __name__=="__main__":
    print("****test de la classe Contact****")
    c1=Contact('0611222344', 'rue des Lilas','France')
    print("   c1                 :",c1)
    print("   c2=Contact()")
    c2=Contact()
    print("****test de la classe Personne****")
    print("   p1=Personne('Doe','John',33)")
    p1=Personne('0145453454','Paris','France', 'Doe', 'John',33)
    print("   p1                 :",p1)
    p2=Personne('545464546','Reims','France', 'Seror', 'Mike',49)
    print("   p2                 :",p2)
    p2.annee_naissance = 1995
    print("   p2                 :", p2)
    print("****test de la classe Organisation****")
    print("   o1=Organisation('World Company')")
    o1=Organisation('0145453454','Paris','France', 'World Company')
    print("   o1                 :",o1)


""""
#test du module
if __name__=="__main__":
    print("test de la classe Contact")
    print("   Contact.nb_contact : ", Contact.nb_contact)
    print("   c1=Contact('0612232324','rue des Lilas','France')")
    c1=Contact('0611222344', 'rue des Lilas','France')
    print("   Contact.nb_contact : ", Contact.nb_contact)
    print("   c1                 :",c1)
    print("   c2=Contact()")
    c2=Contact()
    print("   Contact.nb_contact : ", Contact.nb_contact)
    print("   del c2")
    del c2
    print("   Contact.nb_contact : ", Contact.nb_contact)

    print("test de la classe Personne")
    print("   p1=Personne('Doe','John',33)")
    p1=Personne('Doe', 'John',33)
    print("   p1                 :",p1)
    print("   c2=Personne()")
    c2=Contact()
    print("   Personne.nombre : ", Contact.nb_contact)
    print("   del c2")
    del c2
    print("   Personne.nombre : ", Contact.nb_contact)

    print("test de la classe Organisation")
    print("   o1=Organisation('World Company')")
    o1=Organisation('World Company')
    print("   o1                 :",o1)
    print("   c2=Personne()")
    c2=Contact()
    print("   Personne.nombre : ", Contact.nb_contact)
    print("   del c2")
    del c2
    print("   Personne.nombre : ", Contact.nb_contact)

"""


