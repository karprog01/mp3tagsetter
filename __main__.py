import urllib.error
from app.mp3tag import MP3File
from app.colors import BColors
from app.args import get_args


def main():
    args = get_args()

    try:
        file = MP3File(args.filename)
        file.load_meta(args.cover)
        file.save()
    except ValueError:
        print(BColors.FAIL + 'ERROR:' + BColors.ENDC + ' File must be of type mp3')
        exit()
    except urllib.error.HTTPError:
        print(BColors.FAIL + 'ERROR:' + BColors.ENDC + ' URL ' + args.cover + ' not found')
        exit()
    except IOError:
        print(BColors.FAIL + 'ERROR:' + BColors.ENDC + ' File ' + args.filename + ' not found')
        exit()

    print(BColors.OKGREEN + 'SUCCESS:' + BColors.ENDC + ' File ' + args.filename + ' updated')
    print('- ' + BColors.OKBLUE + 'New artist:' + BColors.ENDC + ' ' + file.audio.tag.artist)
    print('- ' + BColors.OKBLUE + 'New title:' + BColors.ENDC + ' ' + file.audio.tag.title)
    print('- ' + BColors.OKBLUE + 'New cover:' + BColors.ENDC + ' ' + args.cover)


if __name__ == '__main__':
    main()
