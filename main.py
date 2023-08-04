from cryptography.fernet import Fernet
import sys

def generate_key():
    # 64 바이트(512비트) 길이의 랜덤 키 생성
    return Fernet.generate_key()

def encrypt_message(key, message):
    # 키를 사용하여 암호화 객체 생성
    fernet = Fernet(key)
    # 메시지를 바이트로 인코딩
    encoded_message = message.encode()
    # 메시지를 암호화
    encrypted_message = fernet.encrypt(encoded_message)
    return encrypted_message

def decrypt_message(key, encrypted_message):
    # 키를 사용하여 암호화 객체 생성

    fernet = Fernet(key)
    # 메시지를 복호화
    decrypted_message = fernet.decrypt(encrypted_message)
    # 복호화된 바이트를 문자열로 디코딩
    return decrypted_message.decode()


def main():
    action = input("\n\n\n1) 암호화   |   2) 복호화   |   3) 프로그램 종료\n\n> ")
    if action.lower() == "1":
        message = input("암호화할 메시지를 입력하세요: ")
        key = generate_key()
        encrypted_message = encrypt_message(key, message)
        print("암호 키:", key.decode())
        print("암호화된 메시지:", encrypted_message.decode())
    elif action.lower() == "2":
        encrypted_message = input("복호화할 암호화된 메시지를 입력하세요: ").encode()
        key_input = input("복호화를 위한 암호 키를 입력하세요: ")
        decrypted_message = decrypt_message(key_input.encode(), encrypted_message)
        print("복호화된 메시지:", decrypted_message)
    elif action.lower() == "3":
        sys.exit()
    else:
        print("암호화 또는 복호화를 선택해주세요.")

while True:
    if __name__ == "__main__":
        main()
