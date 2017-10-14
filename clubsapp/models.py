from portalapp.models import *


class ContactDetails ( models.Model ):
    id = models.AutoField ( primary_key=True , null=False )
    email = models.EmailField ( max_length=50 , null=False )  # ddgandhi.96@gmail.com
    website = models.URLField ( null=True )
    telephone1 = models.CharField ( max_length=15 , null=True )  # 8655022884
    telephone2 = models.CharField ( max_length=15 , null=True )

    def __unicode__ ( self ):
        return self.email + self.website



class Post ( models.Model ):
    id = models.AutoField ( primary_key=True , null=False )
    shortName = models.TextField ( max_length=45 , null=True )
    longName = models.TextField ( max_length=45 , null=True )
    displayName = models.TextField ( max_length=45 , null=True )

    def __unicode__ ( self ):
        return self.longName


class Club ( models.Model ):
    id = models.AutoField ( primary_key=True , null=False )
    shortName = models.TextField ( max_length=45 , null=True )
    longName = models.TextField ( max_length=45 , null=True )
    displayName = models.TextField ( max_length=45 , null=True )
    aboutUs = models.TextField ( max_length=200 , null=True )
    yearOfStart = models.DateField ( null=True )
    president = models.ForeignKey ( Personinformation , related_name="president" )
    clubType = models.TextField ( max_length=45 , null=True )
    facultyInCharge1 = models.ForeignKey ( Personinformation , related_name="facultyInCharge1" )
    facultyInCharge2 = models.ForeignKey(Personinformation, related_name="facultyInCharge2", null=True )  #some clubs have two f.i
    Contact = models.ForeignKey ( ContactDetails )   #foreign key to ContactDetails
    Event = models.ForeignKey ( Event )    #foreign key to Event
    Work = models.ForeignKey ( Work ) #foreign key to work
    ClubMember = models.ForeignKey ( ClubMember) #foreign key to ClubMember

    def __unicode__ ( self ):
        return self.longName


class ClubMember ( models.Model ):
    id = models.AutoField ( primary_key=True , null=False )
    basicDetails = models.ForeignKey ( Personinformation )
    post = models.ForeignKey ( Post )
    photograph = models.ImageField ( )
    dateOfJoin = models.DateField ( null=True )
    dateOfLeave = models.DateField ( null=True )

    def __unicode__ ( self ):
        return self.basicDetails


class Photos ( models.Model ):
    id = models.AutoField ( primary_key=True , null=False )
    club = models.ForeignKey ( Club , null=False )
    photograph = models.ImageField ( )
    details = models.TextField ( max_length=45 , null=True )
    dateOfCapture = models.DateField ( null=True )

class Event ( models.Model ):
    id = models.AutoField ( primary_key=True , null=False )
    shortName = models.TextField ( max_length=45 , null=True )
    longName = models.TextField ( max_length=45 , null=True )
    displayName = models.TextField ( max_length=45 , null=True )
    place = models.TextField (max_length=100 , null=True )
    time = models.TimeField ()



    def __unicode__ ( self ):
        return self.longName


class Work ( models.Model ):
    id = models.AutoField ( primary_key=True , null=False )
    club = models.ForeignKey ( Club , null=False )
    heading = models.TextField ( max_length=100 , null = False)
    description = models.TextField ( null=False )
    date = models.DateField ( null=True )

    def __unicode__ ( self ):
        return self.description
