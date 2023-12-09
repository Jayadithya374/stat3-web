from django.shortcuts import render
from .forms import SMILESForm
from .logic import Prediction
# Create your views here.

def home(request):

    form = SMILESForm()
    if request.method == 'POST':
        form = SMILESForm(request.POST)

        if form.is_valid():

            SMILES = request.POST.get('SMILES')

            prediction = Prediction(SMILES)

            if prediction:
                prediction = "The molecule can potentially act as an inhibitor"
            else:
                prediction = "The molecule potentially *cannot* act as an inhibitor"

            return render(request,'home.html', {'form': form, 'smiles': SMILES, 'prediction': prediction})

    return render(request, 'home.html', {'form': form})

