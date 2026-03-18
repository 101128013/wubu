"""
OSINT Level 3: Domain Lookup - ENHANCED
Real WHOIS queries, DNS resolution, and infrastructure analysis
"""

import json
import requests
import socket
import subprocess
from datetime import datetime
from typing import Dict, Optional, List

class Level3DomainLookup:
    def __init__(self, email: str = "nickfoy.design@gmail.com", output_file: str = "level_3_results.json"):
        self.email = email
        self.domain = email.split("@")[1] if "@" in email else email
        self.output_file = output_file
        self.results = {
            "level": 3,
            "timestamp": datetime.now().isoformat(),
            "domain": self.domain,
            "whois_data": [],
            "dns_records": {},
            "ip_addresses": [],
            "ssl_certificate": {},
            "registrar_info": {},
            "reputation": {}
        }
    
    def query_whois_api(self) -> Dict:
        """Query WHOIS using free API"""
        try:
            response = requests.get(
                f"https://www.whoisxmlapi.com/api/gateway?apikey=demo&domain={self.domain}&outputFormat=json",
                timeout=10
            )
            if response.status_code == 200:
                data = response.json()
                return {
                    "registrant": data.get('registrant', {}).get('name'),
                    "registrar": data.get('registrar', {}).get('name'),
                    "created": data.get('createdDate'),
                    "expires": data.get('expiresDate'),
                    "updated": data.get('updatedDate')
                }
        except:
            pass
        return {}
    
    def query_dns_records(self) -> Dict:
        """Query all DNS records"""
        dns_data = {}
        try:
            # A records
            try:
                a_records = socket.gethostbyname_ex(self.domain)
                dns_data['A_records'] = a_records[2]
                self.results['ip_addresses'].extend(a_records[2])
            except:
                pass
            
            # MX records
            try:
                result = subprocess.run(['nslookup', '-type=MX', self.domain], 
                                      capture_output=True, text=True, timeout=5)
                if result.returncode == 0:
                    dns_data['MX_records'] = result.stdout
            except:
                pass
            
            # NS records
            try:
                result = subprocess.run(['nslookup', '-type=NS', self.domain],
                                      capture_output=True, text=True, timeout=5)
                if result.returncode == 0:
                    dns_data['NS_records'] = result.stdout
            except:
                pass
            
            # TXT records (SPF, DMARC)
            try:
                result = subprocess.run(['nslookup', '-type=TXT', self.domain],
                                      capture_output=True, text=True, timeout=5)
                if result.returncode == 0:
                    dns_data['TXT_records'] = result.stdout
            except:
                pass
        except Exception as e:
            dns_data['error'] = str(e)
        
        return dns_data
    
    def check_ssl_certificate(self) -> Dict:
        """Check SSL certificate details"""
        ssl_info = {}
        try:
            import ssl
            context = ssl.create_default_context()
            with socket.create_connection((self.domain, 443), timeout=5) as sock:
                with context.wrap_socket(sock, server_hostname=self.domain) as ssock:
                    cert = ssock.getpeercert()
                    ssl_info = {
                        'subject': cert.get('subject', []),
                        'issuer': cert.get('issuer', []),
                        'version': cert.get('version'),
                        'serial_number': cert.get('serialNumber')
                    }
        except:
            ssl_info['status'] = 'Unable to retrieve'
        
        return ssl_info
    
    def check_domain_reputation(self) -> Dict:
        """Check domain reputation"""
        reputation = {}
        try:
            # VirusTotal check
            response = requests.get(
                f"https://www.virustotal.com/api/v3/domains/{self.domain}",
                timeout=10
            )
            if response.status_code == 200:
                data = response.json()
                reputation['virustotal'] = {
                    'malicious': data.get('data', {}).get('attributes', {}).get('malicious_votes'),
                    'undetected': data.get('data', {}).get('attributes', {}).get('undetected_votes')
                }
        except:
            pass
        
        return reputation
    
    def run(self) -> Dict:
        """Execute Level 3 lookup"""
        print(f"[*] Level 3: Domain Lookup - {self.domain}")
        
        # WHOIS lookup
        self.results['whois_data'] = self.query_whois_api()
        
        # DNS queries
        self.results['dns_records'] = self.query_dns_records()
        
        # SSL certificate
        self.results['ssl_certificate'] = self.check_ssl_certificate()
        
        # Reputation check
        self.results['reputation'] = self.check_domain_reputation()
        
        with open(self.output_file, 'w') as f:
            json.dump(self.results, f, indent=2)
        
        print(f"[+] Level 3 Complete")
        return self.results


if __name__ == "__main__":
    lookup = Level3DomainLookup()
    lookup.run()
