# app.py

from flask import Flask, jsonify, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from api_integrations import virus_total_scan, abuse_ipdb_check

app = Flask(__name__)
limiter = Limiter(app, key_func=get_remote_address)

# Rate limits (10 requests per minute)
vt_rate_limit = limiter.limit("10 per minute")
abipdb_rate_limit = limiter.limit("10 per minute")

# Pagination settings
page_size = 10

@app.route('/api/virus-total-scan', methods=['GET'])
@vt_rate_limit
def virus_total_scan_api():
    url = request.args.get('url')
    page = int(request.args.get('page', 1))
    offset = (page - 1) * page_size
    # Assuming you have a list of URLs to scan
    urls = [...]  # list of URLs
    scanned_urls = urls[offset:offset+page_size]
    results = []
    for url in scanned_urls:
        result = virus_total_scan(url)
        results.append(result)
    return jsonify(results)

@app.route('/api/abuse-ipdb-check', methods=['GET'])
@abipdb_rate_limit
def abuse_ipdb_check_api():
    ip = request.args.get('ip')
    page = int(request.args.get('page', 1))
    offset = (page - 1) * page_size
    # Assuming you have a list of IPs to check
    ips = [...]  # list of IPs
    checked_ips = ips[offset:offset+page_size]
    results = []
    for ip in checked_ips:
        result = abuse_ipdb_check(ip)
        results.append(result)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True, port=3002)