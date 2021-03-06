# Python-Noise-Generator
Repozytorium zawiera implementację algorytmu szumu, zbliżoną działaniem do szumu Perlinowskiego. Graficzna reprezentacja projektu zostałą zrealizowana przy wykorzystaniu biblioteki Pygame.


## Opis funkcji programu oraz kompilacja

<b>Elementy składowe: </b>

Program składa się z trzech plików *.py (perlin_render, noise, button) oraz jednej mapy w postaci pliku "map.png", przy czym każdy z nich spełnia odpowiednią funkcjonalność:

- <b>perlin_render.py</b>
  jest to główny plik programu, zawierający pętlę obsługującą komunikację GUI z użytkownikiem, oraz cały mechanizm obsługi tej komunikacji
- <b>button.py</b>
  plik zawiera jedynie klasę przycisku, pozwalającą na jego szybsze zdefiniowanie i wdrożenie do programu głównego
- <b>noise.py</b>
  plik zawierający główną klasę programu, odpowiedzialną za obsługę algorytmu szumu oraz jego odpowiednie prezentowanie użytkownikowi
  
 <b>Kompilacja:</b>
 
 Program został napisany w Pythonie 3
 
 do poprawnej kompilacji wymaga on posiadania:
 - biblioteki Pygame
 - biblioteki PIL (wykorzystywanej do edycji pliku *.png)
 - biblioteki numpy
 
 Plikiem głównym ("main") programu jest plik "perlin_rder.py".
  
## Dokładniejszy opis działania kluczowych fragmentów programu

<b>Poruszanie się po menu</b>

Po uruchomieniu programu pojawi się nam jego menu wraz z głównym ekranem wyświetlającym wyniki (interpretacja wyników omówiona jest w następnym podpunkcie).
Do naszej dyspozycji otrzymujemy trzy funkcjonalne przyciski (submit, create oraz exit), przy czym działanie przycisku exit jest dość wymowne. Na lewo od przycisku znajdują się dwa input-boxy (ocvates oraz bias). Liczby koło napisów opisują aktualny zadany stan parametrów. W celu zmienienia parametrów należy kliknąć myszą w pole i wprowadzić odpowiedni parametr. Program zabezpieczony jest przed wprowadzaniem niepoprawnych danych (przyjmowane są wyłącznie cyfry oraz kropki oznaczające rozdzielenie części zmienno od stałoprzecinkowej liczby). Zmienna <b>octaves</b> powinna być liczbą naturalną z przedziału około 1-10, natomiast liczba <b>Bias</b> może być liczbą całkowitą, preferowany przedział 10^(-3) - 10. 

Po wprowadzeniu nowych parametrów, wystarczy nacisnąć przycisk submit, który wygeneruje dla nas szum o zadanych wcześniej parametrach. Przycisk <b>create</b> natomiast odpowiada za wygenerowanie nowego "seeda" czyli zestawu zmiennych losowych z przedziału (0,1) na podstawie których tworzona jest sekwencja wynikowa algorytmu.

*utworzenie nowego zestawu zmiennych losowych spowoduje reprezentację wyniku dla wcześniej określonych parametrów co widać na stanie licznika parametru.

<img width="350" alt="input view" src="https://raw.githubusercontent.com/homosum1/Python-Noise-Generator/main/screenshots/inputting_variables.png">      <img width="350" alt="input view" src="https://raw.githubusercontent.com/homosum1/Python-Noise-Generator/main/screenshots/noise_example.png">

<b>Sposób reprezentacji wyników</b>

Wynik działania algorytmu przedstawiany jest w postaci wykresu, reprezentowanego w programie przez plik map.png, który nadpisywany jest w trakcie pracy algorytmu.

Algorytm szumu pozwala nam na zamianę zmiennych losowych w pozornie "naturalnie" wyglądające układy - jest to w implementacji Perlina tak zwany szum gradientowy.
W jaki sposób obserwujemy wyniki? Jak widać po uruchomieniu programu widzimy wykres o stałej wartości y. Dzieje się tak dlatego, że początkowo ilość oktaw ustawiona jest na 1. Zatem interpolacja liniowa w naszym algorytmie odbywa się względem tylko jednego punktu, co w rezultacie daje nam całkowicie wypłaszczony wykres. Zmiana liczby oktaw na wyższą spowoduje, że wykres zacznie przypominać "naturalnie wyglądające pasmo górskie", co jest skutkiem wykonywania coraz większej ilości przybliżeń między punktami i wyliczanie na ich podstawie, nowych punktów o zbliżonej wartości.

Zmiana parametru bias na skrajnie mały skutkować będzie natomiast powrotem wyglądu wykresu do tego jaki otrzymalibyśmy podczas reprezentacji zmiennych wygenerowanych losowo, dzieje się tak dlatego, że zmienna ta stanowi mianownik w ilorazie na podstawie którego wyznaczana jest skala z każdym kolejnym wyznaczeniem oktawy. Mechanizm działania dobrze ilustrują poniższe grafiki.

<img width="350" alt="input view" src="https://raw.githubusercontent.com/homosum1/Python-Noise-Generator/main/screenshots/low_bias_2.png">     <img width="350" alt="input view" src="https://raw.githubusercontent.com/homosum1/Python-Noise-Generator/main/screenshots/low_bias_1.png"> 
