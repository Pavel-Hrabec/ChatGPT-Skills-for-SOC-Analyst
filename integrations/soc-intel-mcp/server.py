"""SOC Intel MCP server, tested against the explicitly pinned SDK 1.x release."""
import argparse
from mcp.server.fastmcp import FastMCP
from mcp.types import ToolAnnotations
from intel import IntelClient


def create_server(port=8765):
    server=FastMCP('SOC Intel',host='127.0.0.1',port=port)
    client=IntelClient()
    annotations=ToolAnnotations(readOnlyHint=True,destructiveHint=False,
                                idempotentHint=True,openWorldHint=True)
    submission_annotations=ToolAnnotations(readOnlyHint=False,destructiveHint=False,
                                           idempotentHint=False,openWorldHint=True)

    @server.tool(annotations=annotations)
    def lookup_hash(sha256:str)->dict:
        """Retrieve existing VirusTotal, ThreatFox and MalwareBazaar reports for a SHA256.

        Sends the hash to configured providers; never uploads or executes a file.
        Missing credentials and provider errors are returned as separate states.
        """
        return client.lookup('sha256',sha256)

    @server.tool(annotations=annotations)
    def lookup_ip(ip:str)->dict:
        """Retrieve existing reports for a permitted public IP.

        Rejects non-global addresses. Sends the address to configured providers;
        this is not a scan or proof of present maliciousness.
        """
        return client.lookup('ip',ip)

    @server.tool(annotations=annotations)
    def lookup_domain(domain:str)->dict:
        """Retrieve existing reports for a domain permitted for external disclosure.

        The domain is sent to configured providers; no DNS resolution, URL visit,
        active scan, download or file upload is performed.
        """
        return client.lookup('domain',domain)

    @server.tool(annotations=annotations)
    def lookup_url(url:str)->dict:
        """Retrieve existing VirusTotal, URLhaus and urlscan.io reports for a public URL.

        Rejects URL queries, fragments, userinfo, private hosts and unusual ports.
        Sends the URL to configured providers; does not visit or submit it for a scan.
        """
        return client.lookup_url(url)

    @server.tool(annotations=submission_annotations)
    def submit_urlscan(url:str, visibility:str='private', authorized:bool=False)->dict:
        """Submit an explicitly authorized public URL for a new remote website scan.

        This contacts the site from urlscan.io and discloses the URL to that provider.
        Defaults to private visibility. Requires URLSCAN_API_KEY and authorized=True.
        Never infer authorization merely from finding a URL inside an email.
        """
        return client.submit_urlscan(url,visibility,authorized)

    @server.tool(annotations=annotations)
    def get_urlscan_result(scan_id:str)->dict:
        """Read the result of a urlscan.io scan by UUID, including screenshot and report links.

        A 404 may mean the scan is still processing. Screenshot/DOM links may not exist.
        """
        return client.get_urlscan_result(scan_id)

    @server.tool(annotations=annotations)
    def lookup_resolutions(indicator:str)->dict:
        """Read up to ten historical VirusTotal DNS resolutions for a public IP or domain.

        Requires a configured VirusTotal key. Never performs live DNS or visits the host.
        """
        return client.lookup_resolutions(indicator)

    @server.tool(annotations=annotations)
    def lookup_cve(cve:str)->dict:
        """Read public CISA KEV and FIRST EPSS context for one exact CVE.

        Includes retrieval dates and distinguishes missing data from failures.
        This does not validate applicability or exploitation on an asset.
        """
        return client.lookup_cve(cve)

    return server


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--transport',choices=('stdio','streamable-http'),default='stdio')
    parser.add_argument('--port',type=int,default=8765)
    args=parser.parse_args()
    if not 1<=args.port<=65535: parser.error('Port must be between 1 and 65535')
    create_server(args.port).run(transport=args.transport)


if __name__=='__main__': main()

