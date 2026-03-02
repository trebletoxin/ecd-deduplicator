import os, sys, re, platform, shutil
from pathlib import Path
from gooey import Gooey, GooeyParser

@Gooey(
	program_name="Encore Chart Downloader De-Duplicator", 
	default_size=(800, 500),
	header_bg_color="#D3D3D3",
	footer_bg_color="#D3D3D3",
	body_bg_color="#FFFFFF",
	navigation_bg_color="#D3D3D3",
	show_stop_warning=True
)
def main():
	argParser = GooeyParser(description="Removes duplicates from Encore Chart Downloader, using Clone Hero\'s badsongs.txt file")
	req_group = argParser.add_argument_group("Required Arguments")
	req_group.add_argument("-bsf", "--badsongs-txt-file", help="Grab the badsongs.txt file from clone hero documents", widget="FileChooser", gooey_options={'full_width': True}, required=True)
	req_group.add_argument("-chf", "--clone-hero-folder", help="Select the directory you used with Encore Chart Downloader", widget="DirChooser", gooey_options={'full_width': True}, required=True)
	args = argParser.parse_args()
	
	import codecs
	
	if sys.stdout.encoding != 'UTF-8':
		sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
	if sys.stderr.encoding != 'UTF-8':
		sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')
	
	if not os.path.isdir(args.clone_hero_folder):
		print("Clone Hero folder does not exist! Please provide a valid existing path with clone-hero-folder", flush=True)
		sys.exit(1)

	print(f"De-duping charts inside folder {args.clone_hero_folder}", flush=True)
	print(f"Using {args.badsongs_txt_file}", flush=True)

	if platform.system() == "Windows":
		pattern = re.compile(r"^(?P<dir1>\w:.*)\((?P<dir2>\w:.*)\)$")
	else:
		pattern = re.compile(r"^(?P<dir1>\/.*)\((?P<dir2>\/.*)\)$")
	
	start_marker = "ERROR: These folders contain charts that another song has (duplicate charts)!"
	dupliacte_section = []
	is_capturing = False
	with open(args.badsongs_txt_file, "r", encoding='utf-8') as f:
		for line in f:
			if start_marker in line:
				is_capturing = True
				continue

			if is_capturing:
				if not line.strip():
					break
				match = pattern.match(line)
				dupliacte_section.append([match.group('dir1'),match.group('dir2')])

	results = [Path(line[0]).resolve() if line[0].startswith(args.clone_hero_folder.lower()) else Path(line[1]).resolve() for line in dupliacte_section if line[0].startswith(args.clone_hero_folder.lower()) ^ line[1].startswith(args.clone_hero_folder.lower())]

	for line in results:
		for filename in os.listdir(line):
			file_path = os.path.join(line, filename)
			try:
				if os.path.isfile(file_path):
					os.unlink(file_path)
				elif os.path.isdir(file_path):
					shutil.rmtree(file_path)
			except Exception as e:
				print(f'Failed to delete {file_path}. Reason: {e}', flush=True)
		print(f"Removed contents of {line}", flush=True)

if __name__ == '__main__':
	main()