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
İstifadəçi tərəfindən təyin olunan tip üçün Java-dakı sinifləri(class) misal göstərə bilərik.
Məsələn, aşağıdakı kod nümunəsində biz bir çox sistem tipini "NewType" adlı istifadəçi tipində birləşdiririk:

```
class NewType(object):
    def __init__(self, datainput1, datainput2, datainput3):
        self.data1 = datainput1
        self.data2 = datainput2
        self.data3 = datainput3
```  
