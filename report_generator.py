"""Report Generator"""
class ReportGenerator:
    def __init__(self, email="nickfoy.design@gmail.com"):
        self.email = email
    
    def generate_html(self):
        return f"<html><title>OSINT Report - {self.email}</title></html>"