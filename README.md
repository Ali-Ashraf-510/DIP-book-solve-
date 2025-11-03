# حلول أمثلة كتاب Digital Image Processing

> هذا المستودع يحتوي على حلول وتمارين من كتاب معالجة الصور الرقمية.

- الاسم: ضع اسمك هنا
- بيئة العمل: conda باسم `collage`

## المتطلبات
- Anaconda أو Miniconda مثبت على الجهاز
- Windows PowerShell (الأوامر أدناه مهيأة لـ PowerShell)

## إنشاء/استنساخ بيئة conda باسم collage بنفس إصدارات المكتبات
للحفاظ على نفس الإصدارات بالضبط، استخدم ملف تعريف البيئة `environment.yml`.

### 1) من جهازك الأصلي (تصدير البيئة الحالية)
إذا كانت البيئة لديك موجودة أصلًا باسم `collage` وتعمل بشكل صحيح:

```powershell
# فعّل البيئة الحالية
conda activate collage

# صدّر الحزم والإصدارات (بدون أرقام البناء) إلى ملف environment.yml في جذر المشروع
conda env export -n collage --no-builds > environment.yml
```

> ملاحظات:
> - خيار `--no-builds` يجعل الملف أكثر قابلية للنقل بين الأجهزة.
> - إذا كانت هناك حزم مثبّتة عبر pip داخل conda، فسيتم تضمينها تلقائيًا ضمن قسم `pip:` في الملف.

### 2) على أي جهاز آخر (إنشاء البيئة من الملف)
بعد نسخ المشروع الذي يحتوي على `environment.yml`:

```powershell
# أنشئ البيئة الجديدة باسم collage من ملف البيئة
conda env create -n collage -f environment.yml

# فعّل البيئة
conda activate collage
```

### 3) تحديث البيئة إذا تغيّر ملف environment.yml لاحقًا
```powershell
conda env update -n collage -f environment.yml
```

### 4) تلميحات PowerShell
- إذا لم يتعرّف PowerShell على أمر `conda`، شغّل مرة واحدة:

```powershell
conda init powershell
# ثم أغلق نافذة PowerShell وافتحها مجددًا
```

## تشغيل الأمثلة
بعد تفعيل البيئة `collage`، نفّذ أي ملف تمرين مباشرة:

```powershell
# أمثلة
python ex1/ex1.py
python ex4/ex4_opencv.py
python ex4/ex4_pillow.py
```

## هيكل المجلدات
```
ex1/
  ex1.py
ex2/
  ex2.py
ex3/
  ex3.py
ex4/
  ex4_opencv.py
  ex4_pillow.py
ex5/
  ex5.py
ex6/
  ex6.py
ex7/
  ex7.py
ex8/
  ex8.py
ex9/
  ex9.py
ex10/
  ex10.py
```

## ملاحظات
- بعض الأمثلة قد تعتمد على مكتبات مثل OpenCV وPillow وNumPy وغيرها. وجود ملف `environment.yml` يضمن تثبيت نفس الإصدارات التي تعمل عندك.
- إذا أردت مشاركة المشروع مع زملائك بنفس الإعدادات، تأكد من تضمين ملف `environment.yml` في المستودع وتحديثه عند إضافة/تغيير الحزم.
- إذا ظهرت رسالة `ModuleNotFoundError`، فتأكد أولًا من تفعيل البيئة `collage`.
