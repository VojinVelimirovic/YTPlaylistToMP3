import pytube
import os

options = range(3)
counter = 0
desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') + '\\'


def make_folder():
    global destination
    global counter
    if os.path.exists(destination):
        destination = destination.removesuffix(f' ({counter})')
        counter += 1
        destination += f' ({counter})'
        make_folder()
    else:
        os.mkdir(destination)


def get_format():
    global downloadFormat
    while True:
        try:
            downloadFormat = int(input("\t1. MP3\n\t2. MP4\n\nEnter a choice (1 - 2): "))
        except ValueError:
            continue
        if downloadFormat == 1 or downloadFormat == 2:
            break
    return downloadFormat


while True:
    choice_made = False
    choice = int(input("Main Menu:\n\n\t"
                       "1. Download song\n\t"
                       "2. Download playlist\n\n"
                       "Enter a choice (1 - 2): "))
    for option in options:
        if choice == option:
            choice_made = True
    if choice_made:
        break

if choice == 1:
    video = pytube.YouTube(input("Video link:"))

    downloadFormat = get_format()

    destination = desktop_path
    print(f'Downloading: {video.title}...')
    if downloadFormat == 1:
        video.streams.filter(only_audio=True).first().download(output_path=destination)
        base, ext = os.path.splitext(video)
        new_file = base + '.mp3'
        os.rename(video, new_file)
    elif downloadFormat == 2:
        video.streams.filter().first().download(output_path=destination)

    print(video.title + " has successfully been downloaded onto your desktop.")


elif choice == 2:
    playlist = pytube.Playlist(input("Playlist link: "))

    downloadFormat = get_format()

    destination = desktop_path + playlist.title
    make_folder()
    out_files = []
    print(f'Downloading: {playlist.title}...')
    if downloadFormat == 1:
        for video in playlist.videos:
            out_files.append(video.streams.filter(only_audio=True).first().download(output_path=destination))
        for out_file in out_files:
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
    elif downloadFormat == 2:
        for video in playlist.videos:
            out_files.append(video.streams.first().download(output_path=destination))

    print(playlist.title + " has successfully been downloaded onto your desktop.")
