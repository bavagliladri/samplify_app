from django.shortcuts import render
from django.http import FileResponse, JsonResponse
from .forms import UploadFileForm
import forest


def process_data(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            csv_files = request.FILES.getlist('csv_files')
            n = form.cleaned_data['integer_input']
            # Process the CSV files and integer input
            # You can use the lft and forest libraries here
            # For example:
            # result = lft.some_function(csv_files, integer_input)
            # return JsonResponse({'result': result})
            family_trees = forest.Forest(*csv_files)
            family_trees.make_sample(n)
            family_trees.export_sample(filename="sample")
            
            with open("sample/sample.csv", "rb") as f:
                response = FileResponse(f, as_attachment=True, filename="sample.csv")
                return response
    else:
        form = UploadFileForm()
    return render(request, 'upload_form.html', {'form': form})