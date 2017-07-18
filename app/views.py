from django.shortcuts import render
import json
# Create your views here.
def home(request):
	data = json.loads(request.POST.get('data', '[]'))
	delete = request.POST.get('del', None)
	error = None

	if request.POST:
		if delete is not None:
			data = [e for e in data if e['email'] != delete]
		else:
			list_email = [e['email'] for e in data]
			if request.POST.get('email', '-') in list_email:
				error = "Email sudah digunakan"
			else:
				new = {'nama': request.POST.get('nama', '-'), 'email': request.POST.get('email', '-')}
				data.append(dict(new))

	return render(request, 'tpl.html', {'data': json.dumps(data), 'tabel': data, 'error': error})