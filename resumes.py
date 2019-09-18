import requests
import os


RESUME_CSV_FILENAME = os.environ.get('RESUME_CSV_FILENAME')
RESUME_FOLDER = os.environ.get('RESUME_FOLDER')


def save(url, destination_folder, new_filename):
	"""Given a URL for a PDF, save in a given folder."""

	r = requests.get(url, stream=True)

	path = destination_folder + '/'+ new_filename

	with open(path, 'wb') as fd:
		fd.write(r.content)


def process_url_csv(filename):
	"""Given a file name from resume report, download resumes."""

	for line in open(filename):

		resume_url = 'http://' + line.split(',')[2].rstrip()

		tokens = resume_url.split('.')
		no_mimetype = tokens[-2].split('/')[-1]
		mimetype = tokens[-1]
		new_filename = no_mimetype + "." + mimetype
		
		save(resume_url, RESUME_FOLDER, new_filename)

if __name__=="__main__":
	if not RESUME_FOLDER:
		print("No resume folder.")
		print("Set environment variable RESUME_FOLDER.")
		print("This should be the destination of where files will be placed.")
		print("Example: /users/mmahnken/Desktop/some-existing-folder/")
		

	if not RESUME_CSV_FILENAME:
		print("No resume csv filename.")
		print("Set environment variable RESUME_CSV_FILENAME.")
		print("Example: resumes.csv")
		print("This should be the name of the csv with the URLs to visit.")
		print("Assumes the URL is the third item on the line.    D: ")
		print("csv should be formatted like this:")
		print("firstname,lastname,resumeURL")
		
	if RESUME_CSV_FILENAME and RESUME_FOLDER:

		process_url_csv(RESUME_CSV_FILENAME)




