#!/usr/bin/env python3

import argparse
import sys
import logging
from pathlib import Path

from src.scanner import NetworkScanner
from src.vulnerability import VulnerabilityAssessment
from src.network import NetworkAnalyzer
from src.utils import setup_logging, load_config

def main():
    parser = argparse.ArgumentParser(
        description="Cybersecurity Toolkit - Advanced security testing and analysis tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --scan-network 192.168.1.0/24
  %(prog)s --port-scan example.com --ports 1-1000
  %(prog)s --ssl-check example.com:443
        """
    )

    parser.add_argument(
        "--scan-network",
        help="Perform network discovery scan on specified CIDR range",
        metavar="CIDR"
    )

    parser.add_argument(
        "--port-scan",
        help="Perform port scanning on target host",
        metavar="TARGET"
    )

    parser.add_argument(
        "--ports",
        help="Port range to scan (default: 1-1000)",
        metavar="RANGE",
        default="1-1000"
    )

    parser.add_argument(
        "--ssl-check",
        help="Check SSL/TLS certificate of target",
        metavar="HOST:PORT"
    )

    parser.add_argument(
        "--subdomain-enum",
        help="Enumerate subdomains for target domain",
        metavar="DOMAIN"
    )

    parser.add_argument(
        "--check-headers",
        help="Check security headers of target URL",
        metavar="URL"
    )

    parser.add_argument(
        "--password-strength",
        help="Evaluate password strength",
        metavar="PASSWORD"
    )

    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose output"
    )

    parser.add_argument(
        "--config",
        help="Path to configuration file",
        metavar="FILE",
        default="config/config.yaml"
    )

    parser.add_argument(
        "--output",
        help="Output file for results",
        metavar="FILE"
    )

    args = parser.parse_args()

    setup_logging(verbose=args.verbose)
    logger = logging.getLogger(__name__)

    try:
        config = load_config(args.config)
        logger.info("Configuration loaded successfully")

        if args.scan_network:
            logger.info(f"Starting network scan on {args.scan_network}")
            scanner = NetworkScanner(config)
            results = scanner.scan_network(args.scan_network)
            print_results("Network Scan Results", results, args.output)

        elif args.port_scan:
            logger.info(f"Starting port scan on {args.port_scan}")
            scanner = NetworkScanner(config)
            results = scanner.port_scan(args.port_scan, args.ports)
            print_results("Port Scan Results", results, args.output)

        elif args.ssl_check:
            logger.info(f"Checking SSL certificate for {args.ssl_check}")
            analyzer = NetworkAnalyzer(config)
            results = analyzer.check_ssl(args.ssl_check)
            print_results("SSL Check Results", results, args.output)

        elif args.subdomain_enum:
            logger.info(f"Enumerating subdomains for {args.subdomain_enum}")
            analyzer = NetworkAnalyzer(config)
            results = analyzer.enumerate_subdomains(args.subdomain_enum)
            print_results("Subdomain Enumeration Results", results, args.output)

        elif args.check_headers:
            logger.info(f"Checking security headers for {args.check_headers}")
            analyzer = NetworkAnalyzer(config)
            results = analyzer.check_security_headers(args.check_headers)
            print_results("Security Headers Check Results", results, args.output)

        elif args.password_strength:
            logger.info("Evaluating password strength")
            assessment = VulnerabilityAssessment(config)
            results = assessment.evaluate_password(args.password_strength)
            print_results("Password Strength Results", results, args.output)

        else:
            parser.print_help()
            sys.exit(0)

    except KeyboardInterrupt:
        logger.info("Operation cancelled by user")
        sys.exit(130)
    except Exception as e:
        logger.error(f"Error during execution: {str(e)}", exc_info=args.verbose)
        sys.exit(1)

def print_results(title, results, output_file=None):
    print(f"\n{'='*60}")
    print(f"{title}")
    print(f"{'='*60}\n")
    print(results)

    if output_file:
        with open(output_file, 'w') as f:
            f.write(f"{title}\n")
            f.write(f"{'='*60}\n")
            f.write(str(results))
        print(f"\nResults saved to {output_file}")

if __name__ == "__main__":
    main()
