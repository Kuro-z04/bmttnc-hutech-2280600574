class RailFenceCipher:
    def __init__(self):
        pass

    def rail_fence_encrypt(self, plain_text, key):
        if not plain_text or key < 1:
            raise ValueError("plain_text must not be empty and key must be at least 1")

        # Khởi tạo mảng rails
        rail = [''] * key
        row, step = 0, 1

        # Đặt các ký tự vào các rail theo mô hình zigzag
        for char in plain_text:
            rail[row] += char
            if row == 0:
                step = 1
            elif row == key - 1:
                step = -1
            row += step

        # Kết hợp các rail để tạo văn bản mã hóa
        return ''.join(rail)

    def rail_fence_decrypt(self, cipher_text, key):
        if not cipher_text or key < 1:
            raise ValueError("cipher_text must not be empty and key must be at least 1")

        n = len(cipher_text)
        # Tạo mảng để đánh dấu vị trí các ký tự trong mô hình zigzag
        rail = [['\n' for _ in range(n)] for _ in range(key)]
        row, col, step = 0, 0, 1

        # Đánh dấu vị trí các ký tự trong mô hình zigzag
        for i in range(n):
            rail[row][col] = '*'
            if row == 0:
                step = 1
            elif row == key - 1:
                step = -1
            row += step
            col += 1

        # Điền các ký tự từ cipher_text vào các vị trí đã đánh dấu
        index = 0
        for i in range(key):
            for j in range(n):
                if rail[i][j] == '*' and index < n:
                    rail[i][j] = cipher_text[index]
                    index += 1

        # Đọc lại các ký tự theo mô hình zigzag để giải mã
        result = []
        row, col, step = 0, 0, 1
        for i in range(n):
            result.append(rail[row][col])
            if row == 0:
                step = 1
            elif row == key - 1:
                step = -1
            row += step
            col += 1

        return ''.join(result)
