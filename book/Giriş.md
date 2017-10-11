# Giriş

Alqoritmlər və digər müxtəlif məsələlərdən danışmazdan qabaq, istərdik ki, sizə bünövrə təşkil edən ilkin məlumatları verək.
Bunlardan ilki dəyişənlər(variables) mövzusudur.

## 1.1 Dəyişənlər(variables)
Dəyişənlərin tərifinə keçməzdən öncə, gəlin onları hər hansı riyazi bərabərliklə əlaqələndirək. Hər birimiz, uşaq yaşlarımızdan riyazi bərabərliklərin bir çoxunu görmüşük. Misal üçün aşağıdakına diqqət yetirək:
`x^2 + 2y - 2 = 1`

Bu bərabərliyin istifadə yeri hal-hazırda bizə maraqlı deyil. Bizə maraqlı olan hissə budur ki, bərabərlikdə müəyyən "ad"lardan istifadə olunub (x və y), və bu adlar özündə məlumat saxlayır(ehtiva edir). Başqa cür desək, x və y müəyyən məlumatın saxlanılma(eyni zamanda göstərilmə) şəklidir. Eynilə, kompüter elmlərində də, biz məlumatı saxlamaq üçün dəyişənlərə ehtiyac duyuruq.

## 1.2 Məlumat tipləri(data types)
Yuxarıdakı bərabərlikdə, biz x və y-in yerinə hər hansı real ədəd(0.23, 5.5) və yaxud sadəcə 0 və 1 gözləyirik.
Bərabərliyi həll etmək üçün bu x və y-i onların ala biləcəyi(qəbul edə biləcəyi) hər hansı dəyərə bərabərləşdirməliyik və bu işin adına kompüter elmlərində data tipləri deyilir. Başqa cür izah edəsi olsaq, data tip əvvəlcədən müəyyən olunmuş datadır.
Data tiplərdən bəzilərinə misal çəkə bilərik: integer, floating point, string və.s

Biraz teorik danışası olsaq, kompüter yaddaşı 0 və 1-lərlə doludur. Biz hər hansı məsələni həll etməkdən ötəri, bu 0,1-lərdən birbaşa istifadə etmirik, bu çox çətin olardı. İstifadəçilərin həyatını asanlaşdırmaq məqsədilə, proqramlaşdırma dilləri və kompilyatorlar bizə data tipləri təqdim edirlər. Məsələn, integer 2 bayt(bytes), float 4 bayt yer götürür və.s
Bu o deməkdir ki, biz yaddaşda 2 baytı(16 bit) birləşdirib adına integer deyirik. Eynilə 4 baytı(32 bit) birləşdirib adına float deyirik.
Data tipləri, kodlaşdırma əziyyətini azaldır.
Ən üst səviyyədə data tipləri 2 yerə ayrılır:
* Sistem tərəfindən əvvəlcədən təyin olunmuş data tiplər(həmçinin Primitiv data tiplər adlanırlar).
* İstifadəçi tərəfindən təyin olunmuş data tiplər.

## Sistem tərəfindən təyin olunmuş data tiplər(system-defined)
Sistem tərəfindən təyin olunmuş(təqdim olunan) data tiplərinə Primitiv data tiplər də deyilir.
Demək olar ki, bütün proqramlaşdırma dillərində təqdim olunan primit data tiplərdən bəzilərinə misal olaraq: int, float, char, double, bool və.s
Hər primitiv data tipinə ayrılan bit sayı, proqramlaşdırma dilindən, kompilyatordan və istifadə olunan əməliyyat sistemindən asılı olaraq fərqlilik təşkil edə bilər. Eyni tip üçün hər proqramlaşdırma dili, müxtəlif bit ölçüsü istifadə edə bilər.

Məsələn, deyək ki, bir proqramlaşdırma dilində int tipi 2 bayt(16 bit) yer tutur, bu o deməkdir ki, həmin tipin ala biləcəyi dəyər,-32,768  +32,767 (-2^15 +2^15-1) aralığında olacaqdır. Yox əgər, 4 bayt(32 bit) yer tutursa o zaman bu dəyər -2,147,483,648 ilə +2,147,483,647 aralığına düşəcək. Eyni hal, digər tiplər üçün də doğrudur.

## İstifadəçi tərəfindən elan olunan tiplər(user-defined)
Bəzən elə olur ki, sistem tərəfindən verilən tiplər yetərsiz qalır və bu zaman biz öz tiplərimizi elan edirik.
İstifadəçi tərəfindən təyin olunan tip üçün sinifləri(class) misal göstərə bilərik.
Məsələn, aşağıdakı kod nümunəsində biz bir çox sistem tipini "NewType" adlı istifadəçi tipində birləşdiririk:

```
class Newtype:
    def __init__(self, datainput1, datainput2, datainput3):
        self.data1 = datainput1
        self.data2 = datainput2
        self.data3 = datainput3
```  

## 1.3 Data Sructures(veri tipləri)
Yuxarıdakı müzakirəmizə əsasən, dəyişənlərimizdə artıq məlumatları saxladıq, bundan sonra bizə bu məlumatları effektiv surətdə emal edib(manipulyasiya) istifadə edən mexanizm gərəklidir. Data Structure, məlumatın kompüterdə saxlanılması və təşkil edilməsi yoludur.
Data Structure, məlumatın saxlanılıb, təşkil olunub, emal olunması üçün xüsusi formatdır.
Ümumi data strukturlarına arrays, files, linked lists, stacks, queues, trees, graphs və.s daxildir.
Elementlərinin necə təşkil olunmasından asılı olaraq, data strukturları 2 qrupa ayrılır:
* Linear(xətti) data structures: Bu zaman elementlər, ardıcıllıq üzrə əldə edilir(accessed), lakin elementləri ardıcıl saxlamaq məcburi deyil. Nümunə olaraq: Linked Lists, Stacks və Queues.
* Non-linear(qeyri-xətti) data structures: Bu zaman elementlər, qarışıq(ardıcıl olmayaraq) saxlanılır və əldə edilir.


## 1.4 Mücərrəd məlumat tipləri (Abstract Data Types, ADTs)
ADT-ləri izah etməzdən əvvəl, gəlin system-defined data tiplərinə bir də nəzər yetirək. Biz bilirik, susmaya görə, bütün primitiv data tipləri(int, float və.s) toplama və çıxma kimi əməlləri dəstəkləyirlər. Primitiv data tipləri üçün bu kimi əməliyyatları, sistem təşkil edir. İstifadəçi tərəfindən hazırlanan data tipləri üçün isə, biz həm də əməliyyatları elan etməliyik(əvvəlcədən qəlibini hazırlamalıyıq).
Daha sonra, istifadə etməyə qərar versək, artıq əməliyyatı faktiki olaraq icrasını yazmalıyıq(implementation). Bu o deməkdir ki, istifadəçi data tipləri öz əməliyyatları ilə birlikdə elan olunur(qeydə alınır).

Eyni məsələni data structures üçün qeyd etməyə çalışaq. Problemlərin həllini asanlaşdırmaq məqsədilə, biz, data strukturlarını, onların faktiki əməliyyatları ilə birləşdiririk və buna ADT deyirik. ADT-lər 2 hissədən ibarət olur:

* Datanın elanı(Declaration of datas)
* Əməliyyatın elanı(Declaration of operations)

Tez-tez istifadə olunan ADT-lərə misal olaraq, Linked Lists, Stacks, Queues, Priority Queues, Binary Trees, Dictionaries, Hash Tables, Graphs və.s göstərmək olar. Məsələn, Stack datanı data structures-da saxlayanda LİFO(Last-in-First-out) mexanizmindən istifadə edir. Stack-ə daxil olunan ən son element, ən birinci olaraq oranı tərk edir(silinir). Stack üçün bəzi əməliyyatları göstərək:
Stack-in yaradılması, elementin stack-ə salınması(itələnməsi,pushing), elementin stack-dən çıxarılması(silinməsi), stack-ın hazırki(yeni) başını aşkarlamaq, stack-in element sayını tapmaq və.s

ADT-ni elan etdikdə(define) faktiki icra detalları ilə bağlı narahat olmayın(implementation details). İcra detalları, yalnız ADT-dən istifadə etməyə başladıqda, bizə tam aydın olaraq görsənir. Müxtəlif işlər üçün, müxtəlif ADT-lər istifadə olunur. Hətta, bəziləri, yalnız müəyyən dar çərçivədə məsələni həll etməkdən ötəri istifadə olunur.

## 1.5 Alqoritm nədir?
Gəlin, səhər yeməyi üçün, qayğanaq hazırlanması məsələsinin üzərində düşünək. Bu məqsədlə biz özümüz aşağıdakı addımıları atırıq:
* Tava tapırıq.
* Daha sonra yağ axtarırıq:
      a. Yağ varmı?
        a1. Əgər varsa, tavaya quyuruq.
        a2. Əgər yoxdursa, almalıyıqmı?
            b1. Yox, almırıq, daha qayğanaq lazım olmadı
            b2. Hə gedib alırıq.
* Tavanı qaz peçinin üzərinə qoyuruq və.s

Burada sıralanan addımlar, problemin(məsələnin) həlli üçün ardıcıllıqla icra etdiyimiz addımlardır.
Alqoritm üçün formal tərif vermək lazım olsa:
`Alqoritm, verilmiş məsələni həll etmək üçün icra olunan addımlardır`

Ənənəvi alqoritm dərslərində, müəyyən bir alqoritmin dəyərliliyini(lazımlılığını) ölçmək üçün 2 kriteriya əsas götürülür:
* Düzgünlülük (alqoritm verilmiş problemi sonlu addımlar çərçivəsində düzgün həll edirmi?).
* Effektivlik (alqoritm icra olunan zaman nə qədər vaxt və yaddaş(RAM) aparır).

> QEYD: Biz alqoritmin hər addımını sübut etməli deyilik. Əksinə bizə yekun nəticə maraqlıdır.

## 1.6 Nəyə görə alqoritmlərin analizi vacibdir?
Deyək ki, biz şərti A məntəqəsindən B məntəqəsinə getməliyik. Bu yolu qət etmək üçün bizə uyğun olan bir neçə seçim var: avtobusla, maşınla, velosipedlə həttə təyyarə ilə gedə bilərik.
Eyni ilə bir problemi, məsələni həll etmək üçün bir neçə alqoritm mövcud ola bilər(məsələn, sıralama məsələsi üçün bir çox alqoritm mövcuddur, insertion sort, selection sort, quick sort və.s)
Alqoritmləri analiz etmək, bizə vaxt və yaddaş cəhətdən ən uyğun alqoritmi seçməyə kömək edir.

## 1.7 Alqoritmləri analiz etməyin məqsədi nədir?
Alqoritmlərin analizinin(öyrənilməsinin) məqsədi, onları öz aralarında əsasən işləmə vaxtı(əvvəldən sonra qədər keçən vaxt) cəhətdən müqayisə etməkdir. Lakin, alqortimləri öyrənərkən(analiz edərkən) digər göstəricilərə də əhəmiyyət verilə bilər, məsələn. programlaşdırma əziyyəti(development effort), yaddaş problemi və.s

## 1.8 İşləmə vaxtı analizi nədir?(Running Time Analysis)
Bir şeyi qeyd etmək lazımdır ki, standart olaraq alqoritm üçün giriş məlumatı gərəklidir və bu giriş məlumatın həcmi(input size) və tipi müxtəlif ola bilər. İşləmə vaxtı analizinin əsas məqsədi, müəyyən bir alqoritmin, giriş məlumatının həcmi artdıqca özünü necə apardığını aşkarlamaqdır. Daha dəqiq desək, bu analizin nəticəsində, biz aşkarlayırıq ki, alqoritmin işləmə vaxtı giriş məlumat həcmindən nə dərəcədə asılılıq göstərir.
Aşağıdakılar ümumi giriş məlumat tipləridir:
* Massiv həcmi(size of an array)
* Matrisin elementlərinin sayı
* Qrafın uc və kənarları

## 1.9 Alqoritmləri necə müqayisə etməli?
Alqoritmləri müqayisə etmək üçün, bizə müəyyən bir ölçü növləri(meyar) gərəklidir.
Bunlar nə ola bilər?
* İcra olunma vaxtı? - Bu tip müqayisə əslində, doğru deyil. Çünki, CPU,RAM və.s göstəricilərdən asılı olaraq, bir kompüterdə az vaxt aparan alqoritm, digərində çox vaxt apara bilər və beləcə bizim müqayisəmizə mənfi təsir göstərə bilər.
* Kodda icra olunanların sayı?(number of statements) - Bu da düzgün müqayisə meyarı deyil, çünki sətr sayı, operator sayı və.s proqramlaşdırma dilləri arasında fərqlilik göstərə bilər. Həmçinin, hər proqramçının özünə məxsus proqramlaşdırma üsulları(stili) var ki, bunlar da fərqlidir.

## 1.10 Böyümə sürəti(dərəcəsi) nədir? (Rate of Growth)
Girdiyə bağlı olaraq, əməliyyat müddətinin artdığı sürətə böyümə sürəti deyilir(Rusca: скорость, с которой увеличивается время работы в зависимости от ввода, называется скоростью роста).
Gəlin elə təsəvvür edək ki, biz həm maşın, həm də velosiped almaq fikrindəyik. Bu zaman yolüstü dostumuzla qarşılaşırıq və o bizdən soruşur ki, nə almağa gedirik? Çox böyük ehtimal biz maşın almaq üçün getdiyimizi deyəcik, çünki maşın daha bahalıdır.
Ümumiləşdirəsi olsaq, bizim ümumi xərcimiz:
`Ümumi məbləğ = maşının_pulu + velosipedin_pulu`
Lakin, qəbul edirik ki, velosipedin pulu maşına nəzərən nəzərə çarpmır və biz təqribən belə bir şey əldə edirik:
`Ümumi məbləğ ≈ maşının_pulu`

Bu real həyatdakı misalı, funksiya kimi göstərməyə çalışsaq, belə deyə bilərik ki, aşağı dərəcəsi olan əmsalları sadəcə gözardı edə bilərik. Daha dəqiq aşağıdakı funksiyaya baxaq:
`n^4 + 2n^2 + 100n + 500`

Yuxarıdakı dediklərimizi nəzərə alsaq, belə deyə bilərik ki, bizim üçün yuxarıdakı funksiyada ən əhəmiyyətli `n^4`-dür və bu faktiki böyümə dərəcəsidir.

## 1.11 Tez-tez istifadə olunan böyümə dərəcələri

Aşağıdakı cədvəldə, gələcək fəsillərdə, qarşılaşacağımız böyümə dərəcələri sıralanıb:


| Vaxt mürəkkəbliyi        | Adı        | Misal  |
| -------------          |:-------------:| -----:|
| 1                      | Sabit(constant)     | Bağlı listin önünə element əlavə etmək |
| logn                   | Loqarifmik          | Sıralanmış massivdə elementin tapılması |
| n                      | Xətti               | Sıralanmamış(qarışıq) massivdə elementin tapılması|
| nlogn                  | Xətti-loqarifmik    | Mergesort alqoritmi |
| n^2                    | Kvadratik           | Qrafda 2 node arasında ən qısa yolun tapılması |
| n^3                    | Kubik               | Matrisin vurulması |
| 2^n                    | Eksponensial        | Hanoi qüllələri problemi |


## 1.12 Analiz tipləri

Verilmiş alqoritmi analiz edə bilməmiz üçün, onun hansı halda ən az, hansı halda ən çox vaxt apardığını müəyyən etməliyik.
Daha dəqiq desək, hansı daxil olan məlumatda(input) ən az və ən çox vaxt alır.
Alqoritm üçün onun az vaxt aparması müsbət hal olduğu üçün, bunu ən yaxşı hal kimi qiymətləndirə bilərik. Alqoritmin ən çox vaxt apardığı hal, onun ən pis halıdır.
Alqoritmləri analiz etmək üçün, bizə xüsusi bir syntax lazımdır, bu da asimptotik analizin/işarələr sisteminin əsasıdır.

* Ən pis hal
        * Elə bir girdini(daxil olan, input) göstərir ki, bu zaman alqoritm çox vaxtda icra olunur.(slowest time to complete).
        * Elə input-dur ki, alqoritm onu emal edərkən ən çox vaxt gedir.
* Ən yaxşı hal
        * Elə bir girdini(daxil olan, input) göstərir ki, bu zaman alqoritm az vaxtda icra olunur.(fastest time to complete).
        * Elə input-dur ki, alqoritm onu emal edərkən ən az vaxt gedir.

Bundan əlavə alqoritm üçün orta halı da aşkarlamaq mümkündür.

* Orta hal

        * Orta hal, alqoritmanın işləmə vaxtı haqqında proqnoz verir

        * Alqoritmi bir neçə dəfə, müxtəlif input-larla icra edib, icra olunma vaxtını qeyd edirik. Ayrı-ayrı icra vaxtlarını toplayıb yekun vaxtı tapırıq. Daha sonra, bu vaxtı icra olunma sayına bölürük.
        
        * Orta hal, elə qəbul edir ki, daxil olan məlumatlar ixtiyaridir(random).

          `Aşağı sərhəd <= Orta vaxt <= Yuxarı sərhəd`

Verilmiş alqoritm üçün, biz ən pis, ən yaxşı və orta halı ifadələrlə(expressions) göstərə bilərik.
Gəlin elə qəbul edək ki, f(n) funksiyası verilmiş alqoritmi göstərir.
Bu zaman misal üçün qeyd edə bilərik:
          `f(n) = n^2 + 500, ən pis hal üçün`


          `f(n) = n + 100n + 500, ən yaxşı hal üçün`

## 1.13 Asimptotik işarələr sistemi(notation)

Yuxarıda da göstərdiyimiz kimi, ən yaxşı, ən pis və orta hal üçün biz yuxarı və aşağı həddi(sərhəddi) müəyyən etməliyik.
Bu yuxarı və aşağı həddi göstərmək üçün, bizim hansısa xüsusi syntax-a ehtiyacımız var. Aşağıdakı müzakirəmizdə bunun haqqında danışacıq.
Elə qəbul edirik ki, f(n) funksiyası verilmiş alqoritmi göstərir.
