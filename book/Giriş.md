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
