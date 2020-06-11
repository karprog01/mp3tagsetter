import argparse
import eyed3
from colors import bcolors

def main():
    parser = argparse.ArgumentParser(description='Set tags to mp3 file')
    parser.add_argument(
        'filename',
        type=str,
        help='MP3 file name'
    )
    parser.add_argument(
        '--cover',
        type=str,
        default='cover.jpg',
        help='Cover image file name'
    )
    args = parser.parse_args()

    try:
        audio = eyed3.load(args.filename)
    except IndexError:
        print(bcolors.FAIL + 'ERROR:' + bcolors.ENDC + ' MP3 file not specified')
        exit()
    except FileNotFoundError:
        print(bcolors.FAIL + 'ERROR:' + bcolors.ENDC + ' File ' + file_name + ' not found')
        exit()

    try:
        cover = open(args.cover, 'rb').read()
    except FileNotFoundError:
        print(bcolors.FAIL + 'ERROR:' + bcolors.ENDC + ' Cover ' + args.cover + ' not found')
        exit()

    artist_name = args.filename.split(' - ')[0]
    title = args.filename.split(' - ')[1][:-4]

    audio.tag.artist = artist_name
    audio.tag.title = title
    audio.tag.images.set(3, cover, 'image/jpeg')

    audio.tag.save()

    print(bcolors.OKGREEN + 'SUCCESS:' + bcolors.ENDC + ' File ' + args.filename + ' updated')
    print('- ' + bcolors.OKBLUE + 'New artist:' + bcolors.ENDC + ' ' + audio.tag.artist)
    print('- ' + bcolors.OKBLUE + 'New title:' + bcolors.ENDC + ' ' + audio.tag.title)
    print('- ' + bcolors.OKBLUE + 'New cover:' + bcolors.ENDC + ' ' + args.cover)

if __name__ == '__main__':
    main()