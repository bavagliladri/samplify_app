from django.shortcuts import render
from django.http import FileResponse, JsonResponse
from .forms import UploadFileForm
from .forest import Forest
from .language_family_tree import LanguageFamilyTree
from django.shortcuts import redirect


def process_data(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST)
        csv_files = request.FILES.getlist('csv_files')

        if form.is_valid() and csv_files:
            n = form.cleaned_data['integer_input']
            print("✅ Valid form. Received files:", csv_files)

            family_trees = Forest()
            for file in csv_files:
                family_tree = LanguageFamilyTree(fileobj=file.open('rb'))
                family_trees.append(family_tree)
                
            family_trees.make_sample(n)
            family_trees.export_sample(filename="sample")

            f = open("sample/sample.csv", "rb")
            return FileResponse(f, as_attachment=True, filename="sample.csv")
        else:
            print("❌ Error: form not valid or files not received.")
            print("Form errors:", form.errors)
    else:
        form = UploadFileForm()
    return render(request, 'upload_form.html', {'form': form})


def home(request):
    return redirect('process_data')