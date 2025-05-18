import re

class EmailAddressParser:
    def __init__(self, email_addresses):
        self.email_addresses = email_addresses

    def parse(self):
        # Split on commas, spaces, or combinations with optional whitespace
        addresses = re.split(r'[,\s]+', self.email_addresses)
        
        # Filter valid email addresses and remove empty strings
        valid_emails = []
        email_pattern = re.compile(r'^[\w.-]+@[\w-]+\.[\w-]+$')
        for addr in addresses:
            if addr and email_pattern.match(addr):
                valid_emails.append(addr)
        
        # Remove duplicates and sort alphabetically
        unique_sorted = sorted(list(set(valid_emails)))
        return unique_sorted