# Accordeur-in-Python
### Here is a single Python script that you can use to find what is the note playing in an audio 

## Voici une explication de la fonction get_note_from_frequency(frequence)
```
def get_note_from_frequency(frequence):

    frequence_ref = 440

    note_ref = 69

    notes = ['Do', 'Do#', 'Ré', 'Ré#', 'Mi', 'Fa', 'Fa#', 'Sol', 'Sol#', 'La', 'La#', 'Si']

    note_number = 12 * (np.log2(frequence / frequence_ref)) + note_ref

    note_index = int(note_number) % 12

    octave = int(note_number / 12) - 1

    note_name = notes[note_index]

    return note_name + str(octave)
 ```  
  
### Etapes par étapes :  
* La ligne `frequence_ref = 440` définit la fréquence de référence La4 en Hz. C'est la fréquence à partir de laquelle les autres notes sont calculées.
* La ligne `note_ref = 69` définit le numéro de référence de la note La4 selon le standard MIDI. Le standard MIDI attribue le numéro 69 à la note A4.
* La ligne `notes = ...` est une liste contenant les noms des notes de la gamme chromatique.
* La ligne `note_number...` calcule le numéro de note correspondant à la fréquence donnée. Cela se fait en utilisant la formule : `note_number = 12 * (log2(frequence / frequence_ref)) + note_ref`.
  - `np.log2(frequence / frequence_ref)` calcule le logarithme en base 2 du rapport entre la fréquence donnée et la fréquence de référence.
   - `12 * (np.log2(frequence / frequence_ref))` multiplie ce logarithme par 12 pour obtenir un nombre correspondant à un nombre de demi-tons par rapport à la note de référence.
   - `+ note_ref` ajoute le numéro de référence de la note La4 pour obtenir le numéro de note complet.

* La ligne `octave = ...` calcule l'octave de la note correspondante à partir du note_number. Cela se fait en utilisant la formule : `octave = int(note_number / 12) - 1`.
    - `int(note_number / 12)` divise le note_number par 12 et prend la partie entière, ce qui donne le numéro de l'octave.
    - on soustrait 1 pour ajuster l'indice de l'octave (l'octave -1 correspond à l'octave précédente).

* La ligne `note_index = ...` calcule l'indice de la note correspondante dans la liste note_names. Cela se fait en utilisant la formule : `note_index = int(note_number % 12)`.
      - `int(note_number % 12)` prend le reste de la division de note_number par 12, ce qui donne un nombre entre 0 et 11 correspondant à l'indice de la note dans la liste note_names.

* La ligne `note_name = ...` récupère le nom de la note correspondant à l'indice note_index dans la liste note_names.
* Enfin, la fonction retourne le nom de la note concaténé avec la valeur de l'octave convertie en chaîne de caractères.


### Sources : 
* https://fr.wikipedia.org/wiki/Note_de_musique
* https://fr.wikipedia.org/wiki/Logarithme_binaire
* https://librosa.org/doc/latest/index.html
* https://numpy.org/
* https://www.w3schools.com/
* https://www.dcode.fr/logarithme
