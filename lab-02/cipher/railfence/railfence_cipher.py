class RailFenceCipher:
    def __init__(self, num_rails):
        self.num_rails = num_rails

    def encrypt(self, plain_text):
        rails = [[] for _ in range(self.num_rails)]
        rail_index = 0
        direction = 1  # 1: down, -1: up

        for char in plain_text:
            rails[rail_index].append(char)
            if rail_index == 0:
                direction = 1
            elif rail_index == self.num_rails - 1:
                direction = -1
            rail_index += direction

        cipher_text = ''.join(''.join(rail) for rail in rails)
        return cipher_text

    def decrypt(self, cipher_text):
        if not cipher_text or self.num_rails <= 1:
            return cipher_text

        # Tính độ dài mỗi rail
        rail_lengths = [0] * self.num_rails
        rail_index = 0
        direction = 1

        for _ in range(len(cipher_text)):
            rail_lengths[rail_index] += 1
            if rail_index == 0:
                direction = 1
            elif rail_index == self.num_rails - 1:
                direction = -1
            rail_index += direction

        # Chia cipher_text thành các rails
        rails = []
        start = 0
        for length in rail_lengths:
            rails.append(list(cipher_text[start:start + length]))
            start += length

        # Xây dựng lại plain_text
        plain_text = []
        rail_index = 0
        direction = 1

        # Tạo danh sách vị trí zigzag
        positions = []
        for _ in range(len(cipher_text)):
            positions.append(rail_index)
            if rail_index == 0:
                direction = 1
            elif rail_index == self.num_rails - 1:
                direction = -1
            rail_index += direction

        # Đặt ký tự từ rails vào đúng vị trí
        result = [''] * len(cipher_text)
        char_index = 0
        for rail in range(self.num_rails):
            for pos in range(len(positions)):
                if positions[pos] == rail and char_index < len(cipher_text):
                    result[pos] = rails[rail].pop(0)
                    char_index += 1

        return ''.join(result)