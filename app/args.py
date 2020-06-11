import argparse


def get_args():
    parser = argparse.ArgumentParser(description='Set tags to mp3 file')
    parser.add_argument(
        'filename',
        type=str,
        help='MP3 file name'
    )
    parser.add_argument(
        'cover',
        type=str,
        help='Cover image url'
    )

    return parser.parse_args()
