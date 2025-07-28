from django.core.management.base import BaseCommand
from orders.models import Order
from decimal import Decimal

class Command(BaseCommand):
    help = 'Load sample order data'

    def handle(self, *args, **options):
        # Clear existing orders
        Order.objects.all().delete()
        
        sample_orders = [
            {'order_id': '10248', 'customer_name': 'Vins et alcools Chevalier', 'freight': Decimal('32.38'), 'ship_name': 'Vins et alcools Chevalier', 'ship_country': 'France'},
            {'order_id': '10249', 'customer_name': 'Toms Spezialitäten', 'freight': Decimal('11.61'), 'ship_name': 'Toms Spezialitäten', 'ship_country': 'Germany'},
            {'order_id': '10250', 'customer_name': 'Hanari Carnes', 'freight': Decimal('65.83'), 'ship_name': 'Hanari Carnes', 'ship_country': 'Brazil'},
            {'order_id': '10251', 'customer_name': 'Victuailles en stock', 'freight': Decimal('41.34'), 'ship_name': 'Victuailles en stock', 'ship_country': 'France'},
            {'order_id': '10252', 'customer_name': 'Suprêmes délices', 'freight': Decimal('51.30'), 'ship_name': 'Suprêmes délices', 'ship_country': 'Belgium'},
            {'order_id': '10253', 'customer_name': 'Hanari Carnes', 'freight': Decimal('58.17'), 'ship_name': 'Hanari Carnes', 'ship_country': 'Brazil'},
            {'order_id': '10254', 'customer_name': 'Chop-suey Chinese', 'freight': Decimal('22.98'), 'ship_name': 'Chop-suey Chinese', 'ship_country': 'Switzerland'},
            {'order_id': '10255', 'customer_name': 'Richter Supermarkt', 'freight': Decimal('148.33'), 'ship_name': 'Richter Supermarkt', 'ship_country': 'Switzerland'},
            {'order_id': '10256', 'customer_name': 'Wellington Importadora', 'freight': Decimal('13.97'), 'ship_name': 'Wellington Importadora', 'ship_country': 'Brazil'},
            {'order_id': '10257', 'customer_name': 'HILARIÓN-Abastos', 'freight': Decimal('81.91'), 'ship_name': 'HILARIÓN-Abastos', 'ship_country': 'Venezuela'},
            {'order_id': '10258', 'customer_name': 'Ernst Handel', 'freight': Decimal('140.51'), 'ship_name': 'Ernst Handel', 'ship_country': 'Austria'},
            {'order_id': '10259', 'customer_name': 'Centro comercial Moctezuma', 'freight': Decimal('3.25'), 'ship_name': 'Centro comercial Moctezuma', 'ship_country': 'Mexico'},
            {'order_id': '10260', 'customer_name': 'Ottilies Käseladen', 'freight': Decimal('55.09'), 'ship_name': 'Ottilies Käseladen', 'ship_country': 'Germany'},
            {'order_id': '10261', 'customer_name': 'Que Delícia', 'freight': Decimal('3.05'), 'ship_name': 'Que Delícia', 'ship_country': 'Brazil'},
            {'order_id': '10262', 'customer_name': 'Rattlesnake Canyon Grocery', 'freight': Decimal('48.29'), 'ship_name': 'Rattlesnake Canyon Grocery', 'ship_country': 'USA'},
            {'order_id': '10263', 'customer_name': 'Ernst Handel', 'freight': Decimal('146.06'), 'ship_name': 'Ernst Handel', 'ship_country': 'Austria'},
            {'order_id': '10264', 'customer_name': 'Folk och fä HB', 'freight': Decimal('3.67'), 'ship_name': 'Folk och fä HB', 'ship_country': 'Sweden'},
            {'order_id': '10265', 'customer_name': 'Blondel père et fils', 'freight': Decimal('55.28'), 'ship_name': 'Blondel père et fils', 'ship_country': 'France'},
            {'order_id': '10266', 'customer_name': 'Wartian Herkku', 'freight': Decimal('25.73'), 'ship_name': 'Wartian Herkku', 'ship_country': 'Finland'},
            {'order_id': '10267', 'customer_name': 'Frankenversand', 'freight': Decimal('208.58'), 'ship_name': 'Frankenversand', 'ship_country': 'Germany'},
            {'order_id': '10268', 'customer_name': 'GROSELLA-Restaurante', 'freight': Decimal('66.29'), 'ship_name': 'GROSELLA-Restaurante', 'ship_country': 'Venezuela'},
            {'order_id': '10269', 'customer_name': 'White Clover Markets', 'freight': Decimal('4.56'), 'ship_name': 'White Clover Markets', 'ship_country': 'USA'},
            {'order_id': '10270', 'customer_name': 'Mère Paillarde', 'freight': Decimal('136.00'), 'ship_name': 'Mère Paillarde', 'ship_country': 'Canada'},
            {'order_id': '10271', 'customer_name': 'Consolidated Holdings', 'freight': Decimal('45.54'), 'ship_name': 'Consolidated Holdings', 'ship_country': 'UK'},
            {'order_id': '10272', 'customer_name': 'Alfreds Futterkiste', 'freight': Decimal('258.64'), 'ship_name': 'Alfreds Futterkiste', 'ship_country': 'Germany'},
            {'order_id': '10273', 'customer_name': 'Toms Spezialitäten', 'freight': Decimal('24.39'), 'ship_name': 'Toms Spezialitäten', 'ship_country': 'Germany'},
            {'order_id': '10274', 'customer_name': 'Chop-suey Chinese', 'freight': Decimal('18.69'), 'ship_name': 'Chop-suey Chinese', 'ship_country': 'Switzerland'},
            {'order_id': '10275', 'customer_name': 'B\'s Beverages', 'freight': Decimal('6.19'), 'ship_name': 'B\'s Beverages', 'ship_country': 'UK'},
            {'order_id': '10276', 'customer_name': 'Tortuga Restaurante', 'freight': Decimal('13.84'), 'ship_name': 'Tortuga Restaurante', 'ship_country': 'Mexico'},
            {'order_id': '10277', 'customer_name': 'Morgenstern Gesundkost', 'freight': Decimal('125.77'), 'ship_name': 'Morgenstern Gesundkost', 'ship_country': 'Germany'},
            {'order_id': '10278', 'customer_name': 'Berglunds snabbköp', 'freight': Decimal('92.69'), 'ship_name': 'Berglunds snabbköp', 'ship_country': 'Sweden'},
            {'order_id': '10279', 'customer_name': 'Lehmanns Marktstand', 'freight': Decimal('25.83'), 'ship_name': 'Lehmanns Marktstand', 'ship_country': 'Germany'},
            {'order_id': '10280', 'customer_name': 'Berglunds snabbköp', 'freight': Decimal('8.98'), 'ship_name': 'Berglunds snabbköp', 'ship_country': 'Sweden'},
            {'order_id': '10281', 'customer_name': 'Römerich', 'freight': Decimal('2.94'), 'ship_name': 'Römerich', 'ship_country': 'Germany'},
            {'order_id': '10282', 'customer_name': 'Romero y tomillo', 'freight': Decimal('12.69'), 'ship_name': 'Romero y tomillo', 'ship_country': 'Spain'},
            {'order_id': '10283', 'customer_name': 'LILA-Supermercado', 'freight': Decimal('84.81'), 'ship_name': 'LILA-Supermercado', 'ship_country': 'Venezuela'},
            {'order_id': '10284', 'customer_name': 'Lehmanns Marktstand', 'freight': Decimal('76.56'), 'ship_name': 'Lehmanns Marktstand', 'ship_country': 'Germany'},
            {'order_id': '10285', 'customer_name': 'QUICK-Stop', 'freight': Decimal('76.83'), 'ship_name': 'QUICK-Stop', 'ship_country': 'Germany'},
            {'order_id': '10286', 'customer_name': 'QUICK-Stop', 'freight': Decimal('229.24'), 'ship_name': 'QUICK-Stop', 'ship_country': 'Germany'},
            {'order_id': '10287', 'customer_name': 'Ricardo Adocicados', 'freight': Decimal('12.76'), 'ship_name': 'Ricardo Adocicados', 'ship_country': 'Brazil'},
            {'order_id': '10288', 'customer_name': 'Reggiani Caseifici', 'freight': Decimal('7.45'), 'ship_name': 'Reggiani Caseifici', 'ship_country': 'Italy'},
            {'order_id': '10289', 'customer_name': 'BSBEV', 'freight': Decimal('22.77'), 'ship_name': 'BSBEV', 'ship_country': 'UK'},
            {'order_id': '10290', 'customer_name': 'Comércio Mineiro', 'freight': Decimal('79.70'), 'ship_name': 'Comércio Mineiro', 'ship_country': 'Brazil'},
            {'order_id': '10291', 'customer_name': 'Que Delícia', 'freight': Decimal('6.40'), 'ship_name': 'Que Delícia', 'ship_country': 'Brazil'},
            {'order_id': '10292', 'customer_name': 'Tradição Hipermercados', 'freight': Decimal('1.35'), 'ship_name': 'Tradição Hipermercados', 'ship_country': 'Brazil'},
            {'order_id': '10293', 'customer_name': 'Tortuga Restaurante', 'freight': Decimal('21.18'), 'ship_name': 'Tortuga Restaurante', 'ship_country': 'Mexico'},
            {'order_id': '10294', 'customer_name': 'Rattlesnake Canyon Grocery', 'freight': Decimal('147.26'), 'ship_name': 'Rattlesnake Canyon Grocery', 'ship_country': 'USA'},
            {'order_id': '10295', 'customer_name': 'Vin et alcools Chevalier', 'freight': Decimal('1.15'), 'ship_name': 'Vin et alcools Chevalier', 'ship_country': 'France'},
            {'order_id': '10296', 'customer_name': 'LILA-Supermercado', 'freight': Decimal('0.02'), 'ship_name': 'LILA-Supermercado', 'ship_country': 'Venezuela'},
            {'order_id': '10297', 'customer_name': 'Blondel père et fils', 'freight': Decimal('5.74'), 'ship_name': 'Blondel père et fils', 'ship_country': 'France'},
            {'order_id': '10298', 'customer_name': 'Hungry Owl All-Night Grocers', 'freight': Decimal('168.22'), 'ship_name': 'Hungry Owl All-Night Grocers', 'ship_country': 'Ireland'},
            {'order_id': '10299', 'customer_name': 'Ricardo Adocicados', 'freight': Decimal('29.76'), 'ship_name': 'Ricardo Adocicados', 'ship_country': 'Brazil'},
            {'order_id': '10300', 'customer_name': 'Magazzini Alimentari Riuniti', 'freight': Decimal('17.68'), 'ship_name': 'Magazzini Alimentari Riuniti', 'ship_country': 'Italy'},
        ]
        
        for order_data in sample_orders:
            Order.objects.create(**order_data)
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully loaded {len(sample_orders)} sample orders')
        ) 