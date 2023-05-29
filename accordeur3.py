import librosa
import numpy as np
import math

# Charger le fichier audio
audio_file = "La4.wav"
audio, sr = librosa.load(audio_file)

#On determine la fondamental du son -> retourne une liste de fréquences
f0 = librosa.yin(audio, fmin=50, fmax=2000)

#on arrondi les valeurs centiemes
f0_propre = [round(f, 2) for f in f0]

#on supprime les premieres valeurs car très souvent sources de problèmes
del f0_propre[0:10]

#Cette fonction détermine la note de la fréquence donnée en argument
def get_note_from_frequency(frequence):
    #Fréquence du la4 dite reference
    frequence_ref = 440
    note_ref = 69
    notes = ['Do', 'Do#', 'Ré', 'Ré#', 'Mi', 'Fa', 'Fa#', 'Sol', 'Sol#', 'La', 'La#', 'Si']

    # Calculer le numéro de note pour la fréquence donnée
    note_number = 12 * (np.log2(frequence / frequence_ref)) + note_ref

    #Index du la note dans notre liste 'notes'
    note_index = int(note_number) % 12

    #Octave de la fréquence donnée
    octave = int(note_number / 12) - 1

    #Va chercher la note associée à l'index calculé juste avant
    note_name = notes[note_index]

    #retourne la note joué plus l'octave corréspondant (ex: Mi5)
    return note_name + str(octave)

print(get_note_from_frequency(max(f0_propre)))