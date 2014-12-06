from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import FormParser, MultiPartParser,FileUploadParser
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile


class FileUploadView(APIView):
	# parser_classes = (FormParser, MultiPartParser,FileUploadParser,)
	parser_classes = (FileUploadParser,)

	def post(self, request, format=None):

		print type(request)
		print request.data
		file_obj = request.data['file']
		# <class 'django.core.files.uploadedfile.InMemoryUploadedFile'>
		filename = file_obj.name
		path = default_storage.save(filename, ContentFile(file_obj.read()))
		# DANGER, IF FILE IS TOO BIG




		return Response(status=204)









