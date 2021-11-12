# Python-Noise-Generator
Repozytorium zawiera implementację algorytmu szumu, zbliżoną działaniem do szumu Perlinowskiego. Graficzna reprezentacja projektu zostałą zrealizowana przy wykorzystaniu biblioteki pygame.


## Ogólny opis funkcjonalności projektu
Program składa się z trzech plików *.py (Pygame_perlin_noise, perlin_rendering, button), przy czym każdy z nich spełnia odpowiednią funkcjonalność:

- <b>Pygame_perlin_noise.py</b>
  jest to główny plik programu, zawierający pętlę obsługującą komunikację GUI z użytkownikiem, oraz cały mechanizm obsługi tej komunikacji
- <b>button.py</b>
  plik zawiera jedynie klasę przycisku, pozwalającą na jego szybsze zdefiniowanie i wdrożenie do programu głównego
- <b>perlin_rendering.py</b>
  plik zawierający główną klasę programu, odpowiedzialną za obsługę algorytmu szumu oraz jego odpowiednie prezentowanie użytkownikowi
  
  
## Dokładniejszy opis działania kluczowych fragmentów programu

<b>poruszanie się po menu</b>

Po uruchomieniu programu ukażę się nam jego menu wraz z głównym ekranem wyświetlającym wyniki (interpretacja wyników omówiona jest w następnym podpunkcie)
Do naszej dyspozycji otrzymujemy trzy funkcjonalne przyciski (submit, create oraz exit), przy czym działanie przycisku exit jest dość wymowne. Na lewo od przycisku znajdują się dwa input-boxy (ocvates i bias). Liczby koło napisów opisują aktualny zadany stan parametrów. W celu zmienienia parametrów należy kliknąć myszą i wprowadzić odpowiedni parametr. Program zabezpieczony jest przed wprowadzaniem niepoprawnych danych (przyjmowane są wyłącznie cyfry oraz kropki oznaczające rozdzielenie części zmienno od stałoprzecinkowej liczby). Zmienna <b>octaves</b> powinna być liczbą naturalną z przedziału około 1-10, natomiast liczba Bias może być liczbą całkowitą, preferowany przedział 10^(-3) - 10.

<b>Sposób reprezentacji danych</b>
