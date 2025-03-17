class TranspositionCipher:
    def __init__(self):
        pass
    
    def encrypt(self, text, key):
        encrypted_text = ''
        for col in range(key):
            pointer = col
            while pointer < len(text):
                encrypted_text += text[pointer]
                pointer += key
        return encrypted_text
    
    
    
    def decrypt(self,text, key):
        num_cols = (len(text) + key - 1) // key 
        num_rows = key  
        num_shaded_cells = (num_cols * num_rows) - len(text)  

        decrypted_text = [''] * num_cols
        index = 0

        for row in range(num_rows):
            for col in range(num_cols):
                if col == num_cols - 1 and row >= num_rows - num_shaded_cells:
                    continue  
                decrypted_text[col] += text[index]
                index += 1

        return ''.join(decrypted_text)