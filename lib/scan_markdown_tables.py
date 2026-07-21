#!/usr/bin/env python3
"""
Scan markdown files in wiki/pdf2md/ for table structure issues.
Identifies potentially misaligned tables by analyzing pipe character patterns.
"""

import os
import json
import re
from pathlib import Path
from collections import defaultdict

def count_table_metrics(md_file):
    """
    Analyze a markdown file for table structure metrics.
    Returns dict with table statistics.
    """
    with open(md_file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    lines = content.split('\n')

    # Find potential table lines (contain pipes)
    table_metrics = {
        'file': md_file,
        'total_lines': len(lines),
        'lines_with_pipes': 0,
        'max_cells_per_line': 0,
        'potential_table_blocks': [],
        'wide_table_risk': False,  # >10 cells = wide table = likely alignment issues
        'inconsistent_cell_counts': False,
    }

    # Track consecutive lines with pipes (potential table blocks)
    current_block = []
    block_cell_counts = []
    all_blocks = []

    for i, line in enumerate(lines):
        pipe_count = line.count('|')

        if pipe_count >= 2:  # At least 2 pipes = potential table cell
            table_metrics['lines_with_pipes'] += 1
            cell_count = max(0, pipe_count - 1)  # cells = pipes - 1 typically
            table_metrics['max_cells_per_line'] = max(table_metrics['max_cells_per_line'], cell_count)

            current_block.append({
                'line_num': i + 1,
                'content': line[:100],  # First 100 chars
                'cell_count': cell_count,
                'pipe_count': pipe_count
            })
            block_cell_counts.append(cell_count)
        else:
            # End of potential table block
            if current_block:
                all_blocks.append({
                    'start_line': current_block[0]['line_num'],
                    'end_line': current_block[-1]['line_num'],
                    'lines': len(current_block),
                    'cell_counts': block_cell_counts,
                    'cell_count_variance': max(block_cell_counts) - min(block_cell_counts) if block_cell_counts else 0,
                    'max_cells': max(block_cell_counts) if block_cell_counts else 0,
                })
                current_block = []
                block_cell_counts = []

    # Don't forget last block
    if current_block:
        all_blocks.append({
            'start_line': current_block[0]['line_num'],
            'end_line': current_block[-1]['line_num'],
            'lines': len(current_block),
            'cell_counts': block_cell_counts,
            'cell_count_variance': max(block_cell_counts) - min(block_cell_counts) if block_cell_counts else 0,
            'max_cells': max(block_cell_counts) if block_cell_counts else 0,
        })

    table_metrics['potential_table_blocks'] = all_blocks

    # Detect issues
    if table_metrics['max_cells_per_line'] > 10:
        table_metrics['wide_table_risk'] = True

    # Check for inconsistent cell counts within blocks
    for block in all_blocks:
        if block['cell_count_variance'] > 2:  # More than 2 cell variance = likely misalignment
            table_metrics['inconsistent_cell_counts'] = True
            break

    return table_metrics

def main():
    pdf2md_dir = Path('/home/ivanh/hyphae/hyphae-work/sr132/envirostor-wiki/wiki/pdf2md')

    results = {
        'scan_timestamp': '2026-07-06',
        'scan_directory': str(pdf2md_dir),
        'files_scanned': 0,
        'files_with_tables': 0,
        'files_with_wide_tables': 0,
        'files_with_inconsistent_cells': 0,
        'by_severity': {
            'critical': [],  # Wide tables + inconsistent cells
            'high': [],      # Wide tables only
            'medium': [],    # Inconsistent cells only
            'low': [],       # Has tables but well-formed
        },
        'detailed_results': []
    }

    # Scan all markdown files
    for root, dirs, files in os.walk(pdf2md_dir):
        for file in files:
            if file.endswith('.md'):
                md_file = os.path.join(root, file)
                metrics = count_table_metrics(md_file)

                results['files_scanned'] += 1

                if metrics['lines_with_pipes'] > 0:
                    results['files_with_tables'] += 1
                    results['detailed_results'].append(metrics)

                    # Categorize by severity
                    if metrics['wide_table_risk'] and metrics['inconsistent_cell_counts']:
                        results['by_severity']['critical'].append({
                            'file': os.path.relpath(md_file, pdf2md_dir),
                            'max_cells': metrics['max_cells_per_line'],
                            'blocks': len(metrics['potential_table_blocks']),
                        })
                        results['files_with_wide_tables'] += 1
                        results['files_with_inconsistent_cells'] += 1
                    elif metrics['wide_table_risk']:
                        results['by_severity']['high'].append({
                            'file': os.path.relpath(md_file, pdf2md_dir),
                            'max_cells': metrics['max_cells_per_line'],
                            'blocks': len(metrics['potential_table_blocks']),
                        })
                        results['files_with_wide_tables'] += 1
                    elif metrics['inconsistent_cell_counts']:
                        results['by_severity']['medium'].append({
                            'file': os.path.relpath(md_file, pdf2md_dir),
                            'max_cells': metrics['max_cells_per_line'],
                            'blocks': len(metrics['potential_table_blocks']),
                        })
                        results['files_with_inconsistent_cells'] += 1
                    else:
                        results['by_severity']['low'].append({
                            'file': os.path.relpath(md_file, pdf2md_dir),
                            'max_cells': metrics['max_cells_per_line'],
                            'blocks': len(metrics['potential_table_blocks']),
                        })

    # Save results
    output_file = '/home/ivanh/hyphae/hyphae-work/sr132/envirostor-wiki/raw/markdown_table_metrics.json'
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)

    # Print summary
    print(f"\n{'='*70}")
    print(f"MARKDOWN TABLE STRUCTURE ANALYSIS")
    print(f"{'='*70}")
    print(f"Files scanned: {results['files_scanned']}")
    print(f"Files with tables: {results['files_with_tables']}")
    print(f"Files with wide tables (>10 cells): {results['files_with_wide_tables']}")
    print(f"Files with inconsistent cell counts: {results['files_with_inconsistent_cells']}")
    print(f"\nSEVERITY BREAKDOWN:")
    print(f"  🔴 CRITICAL (wide + inconsistent): {len(results['by_severity']['critical'])}")
    print(f"  🟠 HIGH (wide tables only): {len(results['by_severity']['high'])}")
    print(f"  🟡 MEDIUM (inconsistent cells only): {len(results['by_severity']['medium'])}")
    print(f"  🟢 LOW (well-formed): {len(results['by_severity']['low'])}")

    print(f"\n📊 CRITICAL FILES (require attention):")
    for entry in sorted(results['by_severity']['critical'], key=lambda x: x['max_cells'], reverse=True)[:10]:
        print(f"   {entry['file']}")
        print(f"      → {entry['max_cells']} cells max, {entry['blocks']} table blocks")

    print(f"\n✅ Results saved to: {output_file}")
    return results

if __name__ == '__main__':
    main()
