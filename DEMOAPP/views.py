from django.shortcuts import render
from django.http import HttpResponse
#from .models import Post, Hobby
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from DEMOPROJECT import settings

from django.core.files.storage import FileSystemStorage

#added from James Shrestha
#from .forms import MidiForm
#from .models import MIDI

#from music_app import settings

from django.core.files.storage import FileSystemStorage

from keras.models import load_model
model=load_model('./model/best_model.h5')

my_media_root = settings.MEDIA_ROOT

from music21 import *
import numpy as np

unique_notes = ['7.11.2',
 'B-6',
 'B3',
 'C#5',
 'F3',
 'G#3',
 '6.11',
 '8.11',
 'B-3',
 'C6',
 '9.11.2',
 'F#5',
 'F5',
 '11.1',
 '10.0',
 '7.9.1',
 '11.3.6',
 '3.7',
 '0.2.4',
 '9.11.2.5',
 '0.2.5',
 'D1',
 'G2',
 '1.4.7.9',
 '8.0.3',
 'D7',
 '0.3',
 'E-7',
 '4.6.10.0',
 '10.2',
 '2.5',
 '9.11.3',
 '4.8',
 '6.9.1',
 '5.8.11.1',
 '7.9.10',
 '9.0.3',
 'E-2',
 '10.1.5',
 'C5',
 '2.8',
 '7.8.0',
 '1.5',
 '9.1',
 '7.9.0',
 '11.2.4',
 '0.3.4',
 '9.0.3.5',
 '0.3.5',
 'C2',
 'D6',
 '1',
 '1.3.7.8',
 '7.9',
 '4.5',
 'E2',
 'B6',
 '8.10',
 'B-4',
 'A5',
 '9.0',
 '6.9.0.2',
 '3.5.10',
 '11.1.6',
 '4.7.10',
 '9.1.3',
 '3',
 '11.1.4.7',
 '2',
 '0.3.6.9',
 '11.0.4',
 '10.2.5',
 '7.10.1',
 '10.1.4',
 '9.0.2',
 '10.3.4',
 'F#2',
 '5.8.0',
 '2.5.7',
 '3.6.8',
 '4.7.9',
 '4.6.11',
 '7.10.0',
 '10.1.4.5',
 'E4',
 '3.6.9.11',
 '8.11.1',
 '5.8.10.11',
 '0',
 '4.7.11',
 '5.6.10',
 '5.6.9.0',
 '9.0.4',
 '11.0',
 '3.7.8',
 '0.1.5',
 '5.7.11',
 '7.0',
 'F#3',
 '11.1.4',
 '8.10.1',
 '3.7.10',
 '3.8',
 'C#6',
 '0.1',
 '8.10.1.4',
 '4.6.9',
 '2.6.10',
 '8.0.1',
 '0.3.6',
 '6.8.1',
 '0.6',
 'E7',
 '5.7.11.1',
 'A6',
 '10.0.4',
 '5.6.9',
 '10.0.3',
 '5.9.0',
 '4.8.11',
 'B1',
 'A1',
 '7.10.0.3',
 '6.9.0',
 '2.5.8.11',
 'B5',
 'D2',
 '7.11.1',
 '3.4',
 '8.11.2.4',
 '0.4.8',
 'G5',
 '6.9.11',
 '8.9',
 '5.7.10',
 '6.8.0',
 '5.7.0',
 '5.8',
 'B-1',
 '2.4.9',
 'C#7',
 '1.3.8',
 'C3',
 '4.6.10',
 'F2',
 '0.3.7',
 '1.4.8',
 '11.3',
 '7.10.2',
 '2.5.8',
 '4.5.10',
 '2.5.9',
 '1.4.5',
 'F#1',
 'E-3',
 '1.3.6',
 '2.6.9',
 '2.7',
 '3.6.10',
 '6',
 '0.2.7',
 '1.3',
 'G#6',
 'G#4',
 '7.9.11',
 'E5',
 '5.9.11',
 '0.4',
 '9.2',
 '8.11.3',
 '4',
 '0.2.6',
 'C7',
 '1.4.7.10',
 '7.11',
 'E-5',
 '8.0.2',
 '8.1',
 '7',
 '6.10',
 '0.5',
 'B4',
 'F7',
 'C#4',
 '8',
 '8.11.2',
 '6.10.1',
 '11.1.5',
 '3.7.9',
 '11.0.2',
 'A3',
 '11.2.4.7',
 '10.0.5',
 'C#3',
 'A4',
 '6.9',
 'E3',
 '1.6',
 '3.5',
 '5.8.11',
 '1.3.6.9',
 'B2',
 '0.4.6',
 '2.4',
 'D4',
 'B-5',
 '9.10.2',
 '5.7',
 '1.4.7',
 '2.4.8',
 'F#6',
 '1.3.5.8',
 '0.4.5',
 'G#5',
 '3.9',
 '10.2.4',
 '8.10.2',
 '10.0.2.5',
 'G1',
 '1.3.7',
 '6.10.0',
 'G#1',
 '3.5.8.11',
 '11.2.6',
 '7.9.2',
 '3.5.8',
 'G#2',
 '0.2',
 '6.8',
 '5',
 '8.0',
 '3.6.9',
 '0.3.6.8',
 'G6',
 '1.2.6',
 '2.4.6',
 '11.4',
 '11.2.5',
 '4.7',
 '9',
 '1.7',
 '2.5.8.10',
 '11',
 'F1',
 '2.6.8',
 '3.5.9',
 '10.0.4.5',
 '8.10.3',
 '4.6.9.0',
 '7.10.1.3',
 '10.1.3',
 '4.5.9',
 '8.11.0',
 '6.8.11',
 '1.5.8',
 '4.5.8',
 'C4',
 '9.1.4',
 'D3',
 '10.1.4.6',
 'E6',
 '2.6',
 'G4',
 'E-4',
 '4.9',
 '2.5.8.9',
 '5.8.10',
 'E-6',
 '2.4.7',
 '1.4',
 'F#4',
 '10.3',
 '6.7',
 '4.6',
 'C#2',
 '9.11',
 '5.10',
 '11.2',
 '3.6.8.11',
 '1.4.6',
 '5.9',
 'D5',
 '0.4.7',
 '4.7.10.0',
 'G3',
 'F6',
 '7.8',
 '9.10',
 '10.1',
 'F4',
 '3.7.11',
 '5.11',
 '9.11.4',
 '6.7.9',
 'B-2',
 '6.7.11',
 'A2',
 '7.10',
 '4.10',
 '3.6',
 '1.5.9',
 '10',
 '11.2.5.7',
 '3.8.9']

frequent_notes = ['0', '1', '2', '4', '5', '3', '6', '7', '9', '10', '11', '8', '0.4', '4.7', '5.9', '7.10', '2.5', '4.9', '9.1', '10.2', '9.0', '7.11', '6.9', '6.11', '1.4', '0.3', '3.6', 'G3', '11.2', 'D3', 'B3', 'C3', 'C4', 'E3', '7.11.2', '7.0', 'B5', 'G4', 'B-4', 'C#5', 'E5', 'G5', 'B-5', 'C#6', 'G6', 'E6', 'B4', 'F5', 'F6', 'D6', 'D5', 'F#5', 'A5', 'C6', 'F#6', 'E-5', 'E-6', '3.7', '5.7', 'F4', 'G#5', 'G#6', 'B-6', '11.2.6', 'B2', 'D4', 'F#3', '6.10.1', 'F#2', 'B-3', 'C#3', 'B-2', '9.1.4', 'A2', 'A3', 'C#4', '4.8.11', 'E2', 'G#3', 'G#2', 'G2', '2.6.9', 'D2', 'G1', '5.9.0', 'F2', 'F3', '0.4.7', 'C2', '4.7.11', '11.3.6', 'B1', 'E-3', 'E4', '11.4', '1.6', '8.11', '10.1', '5.8', '0.6', 'G#1', 'C5', '0.2.6', 'C7', '9.2', 'A6', '11.3', 'A4', '0.5', '5.11', '4.10', '2.5.9', '10.2.5', '0.3.6', '2.7', '1.7', 'A1', 'F#4', '2.8', '2.5.7', 'C#7', '7.10.1', '8.11.2', 'E-4', '1.4.7', 'G#4', '3.6.9', '5.8.11', '9.0.4', '9.0.2', '5.10', 'E-2', '3.7.10', '7.10.2', 'B-1', '0.2', '8.0', '1.4.7.10', '0.3.5', '1.5', '10.1.5', '7.10.0', 'C#2', '1.5.8', '6.10', '3.8', '8.1', '3.9', '0.3.7', '5.8.0', '4.8', '2.6', '6.9.1', '3.6.8', '8.0.3', '10.3', '6.8', '1.4.8', '1.3', '8.11.3', '10.1.3', '7.9', '4.7.9', '2.4', '7.9.1', '2.4.8', '11.2.4']

x_note_to_int ={'7.11.2': 0,
 'B-6': 1,
 'B3': 2,
 'C#5': 3,
 'F3': 4,
 'G#3': 5,
 '6.11': 6,
 '8.11': 7,
 'B-3': 8,
 'C6': 9,
 'F#5': 10,
 'F5': 11,
 '7.9.1': 12,
 '11.3.6': 13,
 '3.7': 14,
 'G2': 15,
 '8.0.3': 16,
 '0.3': 17,
 '4.8': 18,
 '10.2': 19,
 '2.5': 20,
 '6.9.1': 21,
 'E-2': 22,
 '10.1.5': 23,
 'C5': 24,
 '2.8': 25,
 '1.5': 26,
 '9.1': 27,
 '11.2.4': 28,
 '0.3.5': 29,
 'C2': 30,
 'D6': 31,
 '1': 32,
 '7.9': 33,
 'E2': 34,
 'B-4': 35,
 'A5': 36,
 '9.0': 37,
 '3': 38,
 '2': 39,
 '10.2.5': 40,
 '7.10.1': 41,
 '9.0.2': 42,
 'F#2': 43,
 '5.8.0': 44,
 '2.5.7': 45,
 '3.6.8': 46,
 '4.7.9': 47,
 '7.10.0': 48,
 'E4': 49,
 '0': 50,
 '4.7.11': 51,
 '9.0.4': 52,
 '7.0': 53,
 'F#3': 54,
 '3.7.10': 55,
 '3.8': 56,
 'C#6': 57,
 '0.3.6': 58,
 '0.6': 59,
 'A6': 60,
 '5.9.0': 61,
 '4.8.11': 62,
 'B1': 63,
 'A1': 64,
 'B5': 65,
 'D2': 66,
 'G5': 67,
 '5.8': 68,
 'B-1': 69,
 'C#7': 70,
 'C3': 71,
 'F2': 72,
 '0.3.7': 73,
 '1.4.8': 74,
 '11.3': 75,
 '7.10.2': 76,
 '2.5.9': 77,
 'E-3': 78,
 '2.6.9': 79,
 '2.7': 80,
 '6': 81,
 '1.3': 82,
 'G#6': 83,
 'G#4': 84,
 'E5': 85,
 '0.4': 86,
 '9.2': 87,
 '8.11.3': 88,
 '4': 89,
 '0.2.6': 90,
 'C7': 91,
 '1.4.7.10': 92,
 '7.11': 93,
 'E-5': 94,
 '8.1': 95,
 '7': 96,
 '6.10': 97,
 '0.5': 98,
 'B4': 99,
 'C#4': 100,
 '8': 101,
 '8.11.2': 102,
 '6.10.1': 103,
 'A3': 104,
 'C#3': 105,
 'A4': 106,
 '6.9': 107,
 'E3': 108,
 '1.6': 109,
 '5.8.11': 110,
 'B2': 111,
 '2.4': 112,
 'D4': 113,
 'B-5': 114,
 '5.7': 115,
 '1.4.7': 116,
 '2.4.8': 117,
 'F#6': 118,
 'G#5': 119,
 '3.9': 120,
 'G1': 121,
 'G#1': 122,
 '11.2.6': 123,
 'G#2': 124,
 '0.2': 125,
 '6.8': 126,
 '5': 127,
 '8.0': 128,
 '3.6.9': 129,
 'G6': 130,
 '11.4': 131,
 '4.7': 132,
 '9': 133,
 '1.7': 134,
 '11': 135,
 '10.1.3': 136,
 '1.5.8': 137,
 'C4': 138,
 '9.1.4': 139,
 'D3': 140,
 'E6': 141,
 '2.6': 142,
 'G4': 143,
 'E-4': 144,
 '4.9': 145,
 'E-6': 146,
 '1.4': 147,
 'F#4': 148,
 '10.3': 149,
 'C#2': 150,
 '5.10': 151,
 '11.2': 152,
 '5.9': 153,
 'D5': 154,
 '0.4.7': 155,
 'G3': 156,
 'F6': 157,
 '10.1': 158,
 'F4': 159,
 'B-2': 160,
 'A2': 161,
 '7.10': 162,
 '4.10': 163,
 '3.6': 164,
 '10': 165,
 '5.11': 166}
note_to_int = {value : key for (key, value) in x_note_to_int.items()}

#added end

# Create your views here.
"""
posts = [
    {
        'name': 'Kise Ryota',
        'hobby': 'Basketball',
        'age': 21
    },
    {
        'name': 'Sakamichi',
        'hobby': 'Cycling',
        'age': 15
    }
]"""


#def home(request):
#    context = {
#        'posts': Post.objects.all()
#    }
#    #add context when you want to access posts like , context
#    return render(request, 'DEMOAPP/home.html', context)

#class PostListView(ListView):
#    model = Post
#    template_name = "DEMOAPP/home.html"#<app>/<model>_<viewtype>.html
#    context_object_name = 'posts'
#    ordering = ['-date_posted']

#class PostDetailView(DetailView):
#    model = Post
def home(request):
    return render(request, 'DEMOAPP/home.html', {'title': 'Home'})

def about(request):
    return render(request, 'DEMOAPP/about.html', {'title': 'About'})


#def predictMusic(request):
#    print(request)
 #   print(request.POST.dict())
  #  fileObj = request.FILES['filePath']
   # fs=FileSystemStorage()
    #filePathName=fs.save(fileObj.name,fileObj)

    #return render(request,'DEMOAPP/home.html')

#to save files only from the form
"""
def predictMusic(request):
    if request.method == 'POST' and request.FILES['filePath']:
       myfile = request.FILES['filePath']
       fs = FileSystemStorage()
       filename = fs.save(myfile.name, myfile)
       uploaded_file_url = fs.url(filename)
       return render(request, 'DEMOAPP/home.html', {
           'uploaded_file_url': uploaded_file_url
       })
    return render(request, 'DEMOAPP/home.html')
"""


def predictMusic(request):
    if request.method == 'POST' and request.FILES['filePath']:
       myfile = request.FILES['filePath']
       fs = FileSystemStorage()
       filename = fs.save(myfile.name, myfile)
       print(request.FILES)
       midi_path = my_media_root + "/" + str(request.FILES['filePath'])
       print(midi_path)
       notes = read_midi(midi_path)
       print(notes.shape)
       print(len(notes))
       notes_ = [note for note in notes]
       print(len(notes_))
       print(notes_[:7])
       new_music = filter_notes(notes_)
       input = prepare_input_sequence(new_music)
       prediction = compose(input)
       print(prediction)

       convert_to_midi(prediction)

       context = {
        'displaydlink' : True
       }
       return render(request, 'DEMOAPP/upload.html', context)
    else:
       return render(request, 'DEMOAPP/home.html')


#added from James Shrestha
"""def predictMusic(request):
    if request.method == 'POST':
        form = MidiForm(request.POST, request.FILES)
        if form.is_valid():
            midi_path = my_media_root + '/midis/' + str(request.FILES['midi'])
            print(midi_path)
            notes = read_midi(midi_path)
            print(notes.shape)
            print(len(notes))
            notes_ = [note for note in notes]
            print(len(notes_))
            print(notes_[:7])
            new_music = filter_notes(notes_)
            input = prepare_input_sequence(new_music)
            prediction = compose(input)
            print(prediction)

            convert_to_midi(prediction)

            return HttpResponse('Successfull!!')
    else:
        form = MidiForm()
    return render(request, 'midi_music/model_form_upload.html/', {
        'form': form

    })
"""

# new music
def filter_notes(notes_):
    temp = []
    for note in notes_:
        if note in frequent_notes:
            temp.append(note)
    temp = np.array(temp)
    return temp


def prepare_input_sequence(new_music):
    input = new_music[0:32]
    input = np.array(input)
    temp = []
    for note in input:
        # assign unique integer to every note
        temp.append(x_note_to_int[note])
    input = temp
    input = np.array(input)
    return input


def compose(input):
    predictions = []
    for i in range(10):
        input = input.reshape(1, 32)  # 32 is no of time steps
        prob = model.predict(input)[0]
        y_pred = np.argmax(prob, axis=0)
        predictions.append(y_pred)
        input = np.insert(input[0], len(input[0]), y_pred)
        input = input[1:]
    predicted_notes = [note_to_int[i] for i in predictions]
    return predicted_notes


def read_midi(file):
    print("Loading Music File:", file)

    notes = []
    notes_to_parse = None

    # parsing a midi file
    midi = converter.parse(file)

    # grouping based on different instruments
    s2 = instrument.partitionByInstrument(midi)

    # Looping over all the instruments
    for part in s2.parts:

        # select elements of only piano
        if 'Piano' in str(part):

            notes_to_parse = part.recurse()

            # finding whether a particular element is note or a chord
            for element in notes_to_parse:

                # note
                if isinstance(element, note.Note):
                    notes.append(str(element.pitch))

                # chord
                elif isinstance(element, chord.Chord):
                    notes.append('.'.join(str(n) for n in element.normalOrder))

    return np.array(notes)


def convert_to_midi(prediction_output):
    offset = 0
    output_notes = []

    # create note and chord objects based on the values generated by the model
    for pattern in prediction_output:

        # pattern is a chord
        if ('.' in pattern) or pattern.isdigit():
            notes_in_chord = pattern.split('.')
            notes = []
            for current_note in notes_in_chord:
                cn = int(current_note)
                new_note = note.Note(cn)
                new_note.storedInstrument = instrument.Piano()
                notes.append(new_note)

            new_chord = chord.Chord(notes)
            new_chord.offset = offset
            output_notes.append(new_chord)

        # pattern is a note
        else:

            new_note = note.Note(pattern)
            new_note.offset = offset
            new_note.storedInstrument = instrument.Piano()
            output_notes.append(new_note)

        # increase offset each iteration so that notes do not stack
        offset += 1
    midi_stream = stream.Stream(output_notes)
    # fs = FileSystemStorage()
    # filePathName = fs.save('downloadable',midi_stream)
    midi_stream.write('midi', fp='media/test1.mid')

@login_required
def upload(request):
    return render (request, 'DEMOAPP/upload.html', {'title': 'Upload'})