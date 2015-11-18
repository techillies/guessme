from django.core.management.base import BaseCommand, CommandError
# import xlrd
from django.db import models
import csv
from django.db import transaction
from optparse import make_option
from words.models import Words

class Command(BaseCommand):
    #args = "./data/items.csv"
    #help = 'Initializes Item instances from csv file'

    # @transaction.commit_on_success
    def handle(self, *args, **options):
        try:
            csvFile  = args[0]
        except:
            raise CommandError('csv file-name must to be provided as an argument')

        csv.register_dialect('escaped', escapechar='\\',skipinitialspace=True)
        NAME              = 0
        SUBWORD1          = 1
        SUBWORD2          = 2
        SUBWORD3          = 3
        SUBWORD4          = 4
        SUBWORD5          = 5
        try:
            ifile  = open(csvFile, "rb")
            reader = csv.reader(ifile, dialect='escaped')
            next(reader,None)
            #db_department = Division.objects.all()[0]
            #db_asset, db_asset_isnew = Asset.objects.get_or_create(name="sample", code="xxx", description="decription", department=db_department)
            for row in reader:
                try:
                    db_item, is_created = Words.objects.get_or_create(
                        # code=row[ITEMCODE],
                        name=row[NAME],
                        subword1=row[SUBWORD1],
                        subword2 = row[SUBWORD2],
                        subword3 = row[SUBWORD3],
                        subword4 = row[SUBWORD4],
                        subword5 = row[SUBWORD5]
                    )
                    db_item.save()
                    print "Created word: %s" % (row[NAME])
                except Exception, e:
                    print "Error creating word: %s---%s " %(row[NAME], e)

            self.stdout.write('Successfully initialized words ')
        except Exception, e:
            raise CommandError('error opening csv file! - ', e)
