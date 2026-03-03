# ECD Deduplicator
This tool is used to remove duplicate songs downloaded using the [Encore Chart Downloader](https://github.com/trebletoxin/encore-downloader)

Using the tool requires scanning songs in Clone Hero before running. 
Use the badsongs.txt file from Clone Hero, and the directory that you downloaded charts to using the Encore Chart Downloader.

The removal will always remove the contents of downloaded chart folders in the directory you select. This leaves the parent folder so that the Encore Chart Downloader wont re-download the chart on subsequent runs.

If charts are "duplicate" and both reside in the directory used in the downloader. They will not be removed. This is performed this way as some charts are "instrumental" versions and you may want a certain variant over the other.

## GUI for Windows

A GUI executable has been built for Windows.

![GUI Photo](https://raw.githubusercontent.com/trebletoxin/ecd-deduplicator/refs/heads/main/src/img/GUI-Photo.png)

### GUI Usage

Download the latest version from the [releases](https://github.com/trebletoxin/ecd-deduplicator/releases).

Select the badsongs.txt file from Clone Hero
Select the folder you used with the Encore Chart Downloader

Hit start!

## Command Line Options for python

```
  -chf CLONE_HERO_FOLDER, --clone-hero-folder CLONE_HERO_FOLDER
                        Clone Hero songs folder to output charts to. This option is required
  -bsf BADSONGS_TXT_FILE, --badsongs-txt-file 
                        badsongs.txt file from Clone Hero documents.
```
### CLI Usage

To download, hit "Code" at the top right, then download as a zip and extract it.

#### Linux CLI
`python3 ./deduplicator.py -chf /path/to/your/ECDsongs -bsf /home/yourusername/.clonehero/badsongs.txt`

#### Windows CLI
`py deduplicator.py -chf "C:\Users\username\Documents\Clone Hero\badsongs.txt" -bsf "C:\path\to\your\ECDsongs"`

#### MacOS CLI
macOS is not tested, but should work assuming you get a python environment setup and working. If issues are found, create an issue to get it corrected.

## Credit

[chriskiehl](https://github.com/chriskiehl) - [Gooey](https://github.com/chriskiehl/Gooey) - Simple GUI builder for python projects.

