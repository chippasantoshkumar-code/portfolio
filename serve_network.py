"""
=============================================================================
Multi-Device Local & LAN Web Server
Author: Santhosh Kumar Chippa
Purpose: Serves the portfolio on localhost AND across the local network
         (LAN/Wi-Fi) so it can be opened on phones, laptops, and other systems.
=============================================================================
"""

import http.server
import socketserver
import socket
import os

PORT = 8080

def get_local_ip():
    """Finds the local network IP address of this machine"""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Does not actually send data, just identifies routing interface
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Enable CORS and disable aggressive caching for local testing
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        super().end_headers()

if __name__ == "__main__":
    web_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(web_dir)

    local_ip = get_local_ip()

    print("\n" + "=" * 65)
    print("  SANTHOSH KUMAR CHIPPA - MULTI-DEVICE PORTFOLIO SERVER")
    print("=" * 65)
    print("\n[+] Server is ACTIVE and listening on all network interfaces!\n")
    print(f"  > On THIS computer:")
    print(f"    - Portfolio: http://localhost:{PORT}")
    print(f"    - Resume:    http://localhost:{PORT}/resume.html\n")
    print(f"  > On OTHER SYSTEMS (Phones, Laptops, Tablets on same Wi-Fi):")
    print(f"    - Portfolio: http://{local_ip}:{PORT}")
    print(f"    - Resume:    http://{local_ip}:{PORT}/resume.html\n")
    print("=" * 65)
    print("Press Ctrl + C in this window to stop the server anytime.\n")

    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("0.0.0.0", PORT), CustomHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped gracefully.")

