from portalapp.models import *

class ContactDetails ( models.Model ):
    id = models.AutoField ( primary_key=True , null=False )
    email = models.EmailField ( max_length=50 , null=False )
    website = models.URLField ( null=True )
    telephone1 = models.CharField ( max_length=15 , null=True )
    telephone2 = models.CharField ( max_length=15 , null=True )

    def __unicode__ ( self ):
        return self.email + ' ' + self.website


class Club ( models.Model ):
    id = models.AutoField ( primary_key=True , null=False )
    shortName = models.TextField ( max_length=45 , null=True )
    longName = models.TextField ( max_length=45 , null=True )
    displayName = models.TextField ( max_length=45 , null=True )
    aboutUs = models.TextField ( max_length=2000 , null=True )
    yearOfStart = models.TextField( max_length=6,null=True )
    president = models.ForeignKey ( Personinformation , related_name="president" )
    clubType = models.TextField ( max_length=45 , null=True )
    facultyInCharge1 = models.TextField ( max_length=50 )
    facultyInCharge2 = models.TextField ( max_length=50 , null=True )  #some clubs have two f.i
    contact = models.ForeignKey ( ContactDetails )   #foreign key to ContactDetails

    def __unicode__ ( self ):
        return self.longName


class ClubMember ( models.Model ):
    id = models.AutoField ( primary_key=True , null=False )
    basicDetails = models.ForeignKey ( Personinformation )
    photograph = models.ImageField ( )
    dateOfJoin = models.DateField ( null=True )
    dateOfLeave = models.DateField ( null=True )

    def __unicode__ ( self ):
        return self.basicDetails


class Photos ( models.Model ):
    id = models.AutoField ( primary_key=True , null=False )
    photograph = models.FileField (null=True, blank=True )
    details = models.TextField ( max_length=100 , null=True )
    dateOfCapture = models.DateField ( null=True )

class Event ( models.Model ):
    id = models.AutoField ( primary_key=True , null=False )
    heading = models.TextField ( max_length=100 , null=True )
    description = models.TextField ( max_length=5000 , null=True )
    place = models.TextField (max_length=200 , null=True )
    time = models.TimeField (null = True)
    date = models.DateField(null = True)

    def __unicode__ ( self ):
        return self.heading

class Activity ( models.Model ):
    id = models.AutoField ( primary_key=True , null=False )
    title = models.TextField ( null = True) #no need + need to change HTML
    description = models.TextField ( max_length=5000,null=False )
    date = models.DateField ( null=True )

    def __unicode__ ( self ):
        return self.description

class ClubEventRelationship ( models.Model ):
    id = models.AutoField ( primary_key=True , null=False )
    club = models.ForeignKey ( Club , null=False )
    event = models.ForeignKey ( Event , null=False )

class ClubActivityRelationship( models.Model ):
    id = models.AutoField ( primary_key=True , null=False )
    club = models.ForeignKey ( Club , null=False )
    activity = models.ForeignKey ( Activity , null=False )

class ClubPhotoRelationship( models.Model ):
    id = models.AutoField ( primary_key=True , null=False )
    club = models.ForeignKey ( Club , null=False )
    photo = models.ForeignKey ( Photos , null=False )

class ActivityPhotoRelationship ( models.Model ):
    id = models.AutoField ( primary_key=True , null=False )
    activity = models.ForeignKey ( Activity , null=False )
    photo = models.ForeignKey ( Photos , null=False )

