import secrets
import string


def create_password(length=0, mode='', complexity=None):

    def create_XKCD(words_num):
        with open('/usr/share/dict/words') as f:
            words = [word.strip() for word in f]
            password = ' '.join(secrets.choice(words) for i in range(int(words_num)))
        return str(password)

    def create_common_password(length, complexity):
        alphabet = {
            "digit": string.digits,
            "digit_alpha": string.ascii_letters + string.digits,
            "complex": string.ascii_letters + string.digits + string.punctuation
        }
        password = ''.join(secrets.choice(alphabet.get(complexity)) for i in range(int(length)))
        return str(password)
    if mode == 'XKCD_password':
        return create_XKCD(length)
    elif mode == 'common_password' and complexity:
        return create_common_password(length, complexity)
    return 'Error: Unknown request'

