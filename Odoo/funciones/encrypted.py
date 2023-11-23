    def _compute_encrypted_credit_card_number(self):
        for record in self:
            if record.credit_card_number:
                number_to_encrypt = record.credit_card_number[:-4]
                encrypted_number = ''.join('*' for _ in number_to_encrypt)+record.credit_card_number[-4:]
                return encrypted_number