from django.shortcuts import render

# Create your views here.
#import os
#from decimal import Decimal, InvalidOperation
#import pandas as pd
#from django.conf import settings
#from django.shortcuts import render
#from django.contrib import messages
#from django.db import transaction
from .models import Element
#
#def s(request):
#    # مسیر فایل اکسل
#    file_path = os.path.join(settings.BASE_DIR,'qwe.xlsx')
#
#    created = 0
#    updated = 0
#    errors = []
#
#    try:
#        df = pd.read_excel(file_path, engine='openpyxl')
#    except Exception as e:
#        messages.error(request, f"خطا در خواندن فایل اکسل: {e}")
##        return render(request, 'elements_loaded.html')
#
#    with transaction.atomic():
#        for idx, row in df.iterrows():
#            try:#cell_value = df.iloc[2, 1]
#                symbol = str(row['نماد'])
#                atomic_number = int(row['عدد اتمی'])
#                atomic_mass = float(row['جرم اتمی'])
#                category = str(row['فلز/نافلز/شبه‌فلز'])
#                ntm = str(row['حالت در دمای معمولی'])
#                isotopes = str(row['ایزوتوپ‌ها'])
#                ionic_compounds = str(row['ترکیبات یونی'])
#                Applications = str(row['کاربردها'])
#                History = str(row['تاریخچه'])
#                discoverer = str(row['کاوشگر/کاشف'])
#                tod = str(row['زمان کشف'])
#                Safety = str(row['ایمنی'])
#                interesting_facts = str(row['دانستنی جالب'])
#                
#
#                
#                unc_raw = row.get('mass_uncertainty', None)
#                mass_uncertainty = None
#                if unc_raw is not None and str(unc_raw).strip() != '':
#                    mass_uncertainty = Decimal(str(unc_raw))
#
#                mass_reference = str(row.get('mass_reference', '') or '').strip()
#
#                # آپدیت یا ایجاد
#                try:
#                    el = Element.objects.get(atomic_number=atomic_number)
#                    el.symbol = symbol
#                    el.name = name
#                    el.atomic_mass = atomic_mass
#                    el.mass_uncertainty = mass_uncertainty
#                    el.mass_reference = mass_reference
#                    el.save()
#                    updated += 1
#                except Element.DoesNotExist:
#                    Element.objects.create(
#                        symbol = symbol,
#                        atomic_number = atomic_number,
#                        atomic_mass = atomic_mass,
#                        category = category,
#                        ntm = ntm,
#                        isotopes = isotopes,
#                        ionic_compounds = ionic_compounds,
#                        Applications = Applications,
#                        History = History,
#                        discoverer = discoverer,
#                        tod = tod,
#                        Safety = Safety,
#                        interesting_facts = interesting_facts,
#                    )
#                    created += 1
#
#            except (InvalidOperation, ValueError) as ve:
#                errors.append(f"ردیف {idx+2}: {ve}")
#            except Exception as e:
#                errors.append(f"ردیف {idx+2}: خطای غیرمنتظره: {e}")
#    a=Element.objects.all()
#    print(len(a))
#    return render(request, 'index1.html', {'a':a})


def s(request):
    return render(request, 'index1.html')

def i(request,symbol):
    e=Element.objects.get(symbol=symbol)
    print(e.tod)
    print(symbol)
    return render(request,'index23.html',{'e':e})