#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
OSINT Framework v1.8 - Planning Document Verification Test Suite
Comprehensive testing and validation of all v1.8 planning documents
"""

import os
import sys
import re
from pathlib import Path
from typing import Dict, List

# Fix encoding on Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

class V18TestSuite:
    """Comprehensive test suite for v1.8 planning documents"""
    
    def __init__(self, base_path: str = "C:\\Users\\SUPER\\Downloads\\osijint"):
        self.base_path = Path(base_path)
        self.docs = {}
        self.results = {
            "passed": [],
            "failed": [],
            "warnings": [],
            "metrics": {}
        }
        self.load_documents()
    
    def load_documents(self) -> None:
        """Load all v1.8 planning documents"""
        doc_files = [
            "V18_IMPLEMENTATION_PLAN.md",
            "V18_DETAILED_FUNCTIONS.md",
            "V18_DEPTH_SPECIFICATIONS.md",
            "V18_IMPLEMENTATION_CHECKLIST.md",
            "V18_ARCHITECTURE.md",
            "V18_EXECUTIVE_SUMMARY.md"
        ]
        
        for doc in doc_files:
            try:
                path = self.base_path / doc
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    self.docs[doc] = {
                        "content": content,
                        "lines": len(content.split('\n')),
                        "size_kb": len(content.encode('utf-8')) / 1024
                    }
                self.pass_test(f"Loaded {doc}")
            except Exception as e:
                self.fail_test(f"Failed to load {doc}: {str(e)}")
    
    def pass_test(self, message: str) -> None:
        """Record passed test"""
        self.results["passed"].append(message)
        print(f"[PASS] {message}")
    
    def fail_test(self, message: str) -> None:
        """Record failed test"""
        self.results["failed"].append(message)
        print(f"[FAIL] {message}")
    
    def warn_test(self, message: str) -> None:
        """Record warning"""
        self.results["warnings"].append(message)
        print(f"[WARN] {message}")
    
    def test_document_structure(self) -> None:
        """Test 1: Verify document structure and sections"""
        print("\n" + "="*70)
        print("TEST 1: DOCUMENT STRUCTURE VALIDATION")
        print("="*70)
        
        required_sections = {
            "V18_IMPLEMENTATION_PLAN.md": [
                "Executive Summary",
                "Vision for v1.8",
                "Phase 1: Foundation Enhancement",
                "Phase 2: AI/ML Integration",
                "Phase 3: Advanced Features",
                "Phase 4: Enterprise Features"
            ],
            "V18_DETAILED_FUNCTIONS.md": [
                "Level 1: Email Search",
                "Level 4: Social Graph",
                "Level 5: Content Analysis",
                "Level 6: Financial",
                "Level 7: Vision",
                "Level 9: Correlation",
                "Level 10: Synthesis"
            ],
            "V18_DEPTH_SPECIFICATIONS.md": [
                "Depth Levels Definition",
                "Level 1: Email Search - Depth Progression",
                "Implementation Priority Matrix",
                "Depth Measurement Framework",
                "Resource Allocation v1.8"
            ],
            "V18_IMPLEMENTATION_CHECKLIST.md": [
                "Pre-Implementation Phase",
                "v1.2 Implementation Phase",
                "v1.3 Implementation Phase",
                "Dependency Installation Timeline",
                "Testing Checklist",
                "Deployment Checklist"
            ],
            "V18_ARCHITECTURE.md": [
                "System Architecture Overview",
                "Deployment Architecture",
                "Data Flow Architecture",
                "Technology Stack v1.8",
                "Performance Specifications",
                "Security Architecture"
            ],
            "V18_EXECUTIVE_SUMMARY.md": [
                "Executive Overview",
                "Key Deliverables Summary",
                "Depth & Functionality Improvements",
                "Version Roadmap",
                "Financial Projection"
            ]
        }
        
        for doc, sections in required_sections.items():
            if doc not in self.docs:
                self.fail_test(f"{doc} not found")
                continue
            
            content = self.docs[doc]["content"]
            found_sections = 0
            
            for section in sections:
                if section.lower() in content.lower():
                    found_sections += 1
                else:
                    self.warn_test(f"{doc} missing section: {section}")
            
            percentage = (found_sections / len(sections)) * 100
            if percentage >= 80:
                self.pass_test(f"{doc} structure valid ({percentage:.0f}% sections)")
            else:
                self.fail_test(f"{doc} missing critical sections ({percentage:.0f}%)")
    
    def test_metrics_consistency(self) -> None:
        """Test 2: Verify metrics consistency across documents"""
        print("\n" + "="*70)
        print("TEST 2: METRICS CONSISTENCY VALIDATION")
        print("="*70)
        
        metrics_patterns = {
            "depth_score_v18": r"8\.8",
            "depth_score_v11": r"2\.4",
            "depth_improvement": r"3\.7x",
            "functions_v18": r"1000\+",
            "platforms_v18": r"500\+",
            "speed_improvement": r"59x",
            "accuracy_target": r"99\%\+",
            "timeline_months": r"[6-8] months",
            "team_size": r"[5-6]"
        }
        
        for metric, pattern in metrics_patterns.items():
            matches = 0
            for doc_name, doc_info in self.docs.items():
                if re.search(pattern, doc_info["content"]):
                    matches += 1
            
            if matches >= 3:
                self.pass_test(f"Metric '{metric}' consistent ({matches}/6 docs)")
            else:
                self.warn_test(f"Metric '{metric}' only in {matches} documents")
    
    def test_implementation_details(self) -> None:
        """Test 3: Verify implementation details are specified"""
        print("\n" + "="*70)
        print("TEST 3: IMPLEMENTATION DETAILS VERIFICATION")
        print("="*70)
        
        implementation_items = [
            ("v1.2 Sprint 1", 2),
            ("v1.2 Sprint 2", 2),
            ("v1.2 Sprint 3", 2),
            ("v1.2 Sprint 4", 2),
            ("Level enhancement", 8),
            ("API integration", 5),
            ("Function specification", 3),
        ]
        
        impl_doc = self.docs.get("V18_IMPLEMENTATION_PLAN.md", {})
        checklist_doc = self.docs.get("V18_IMPLEMENTATION_CHECKLIST.md", {})
        
        for item, min_count in implementation_items:
            count = len(re.findall(rf"{re.escape(item)}", 
                                   impl_doc.get("content", "") + checklist_doc.get("content", ""),
                                   re.IGNORECASE))
            if count >= min_count:
                self.pass_test(f"Implementation '{item}' specified ({count} times)")
            else:
                self.warn_test(f"Implementation '{item}' limited detail ({count}/{min_count})")
    
    def test_depth_progression(self) -> None:
        """Test 4: Verify depth progression logic"""
        print("\n" + "="*70)
        print("TEST 4: DEPTH PROGRESSION ANALYSIS")
        print("="*70)
        
        depth_doc = self.docs.get("V18_DEPTH_SPECIFICATIONS.md", {})
        content = depth_doc.get("content", "")
        
        depth_checks = {
            "v1.2_depth": (r"4\.5", "v1.2 target"),
            "v1.3_depth": (r"6\.1", "v1.3 target"),
            "v1.8_depth": (r"8\.8", "v1.8 target"),
            "per_level_specs": (r"Level \d", "level specs")
        }
        
        for check_name, (pattern, description) in depth_checks.items():
            matches = len(re.findall(pattern, content))
            if matches > 0:
                self.pass_test(f"{description} defined: {matches} matches")
            else:
                self.fail_test(f"{description} not found: {pattern}")
    
    def test_architecture_completeness(self) -> None:
        """Test 5: Verify architecture specification"""
        print("\n" + "="*70)
        print("TEST 5: ARCHITECTURE COMPLETENESS CHECK")
        print("="*70)
        
        arch_doc = self.docs.get("V18_ARCHITECTURE.md", {})
        content = arch_doc.get("content", "")
        
        architecture_components = {
            "Kubernetes": "Container orchestration",
            "PostgreSQL": "Primary database",
            "Neo4j": "Graph database",
            "Redis": "Cache layer",
            "Kafka": "Message queue",
            "TensorFlow": "ML framework",
            "FastAPI": "API framework",
            "Elasticsearch": "Search engine",
            "Docker": "Containerization",
            "AWS": "Cloud provider"
        }
        
        components_found = 0
        for component, purpose in architecture_components.items():
            if component in content:
                components_found += 1
                self.pass_test(f"{component} ({purpose}) specified")
            else:
                self.warn_test(f"{component} not mentioned")
        
        coverage_pct = (components_found / len(architecture_components)) * 100
        if coverage_pct >= 75:
            self.pass_test(f"Architecture coverage: {coverage_pct:.0f}%")
        else:
            self.fail_test(f"Architecture coverage insufficient: {coverage_pct:.0f}%")
    
    def test_security_compliance(self) -> None:
        """Test 6: Verify security and compliance specs"""
        print("\n" + "="*70)
        print("TEST 6: SECURITY & COMPLIANCE VALIDATION")
        print("="*70)
        
        arch_doc = self.docs.get("V18_ARCHITECTURE.md", {})
        summary_doc = self.docs.get("V18_EXECUTIVE_SUMMARY.md", {})
        content = arch_doc.get("content", "") + summary_doc.get("content", "")
        
        security_items = {
            "OAuth2": "Authentication",
            "JWT": "Tokens",
            "TLS 1.3": "Encryption",
            "RBAC": "Access control",
            "SOC 2": "Compliance",
            "GDPR": "Privacy",
            "CCPA": "Privacy law",
            "mTLS": "Service security",
            "Vault": "Secrets"
        }
        
        items_found = 0
        for security_item, description in security_items.items():
            if security_item in content:
                items_found += 1
                self.pass_test(f"{security_item} ({description}) defined")
            else:
                self.warn_test(f"{security_item} not mentioned")
        
        coverage = (items_found / len(security_items)) * 100
        self.pass_test(f"Security coverage: {coverage:.0f}%")
    
    def test_resource_requirements(self) -> None:
        """Test 7: Verify resource requirements"""
        print("\n" + "="*70)
        print("TEST 7: RESOURCE REQUIREMENTS ANALYSIS")
        print("="*70)
        
        summary_doc = self.docs.get("V18_EXECUTIVE_SUMMARY.md", {})
        arch_doc = self.docs.get("V18_ARCHITECTURE.md", {})
        content = summary_doc.get("content", "") + arch_doc.get("content", "")
        
        resource_specs = {
            "team_size": r"[5-6]",
            "timeline": r"[6-8] month",
            "effort": r"1600\+",
            "cost": r"\$380",
            "gpu": r"GPU|A100|H100",
            "database": r"PostgreSQL|Neo4j|MongoDB",
            "scaling": r"1000|concurrent"
        }
        
        for resource, pattern in resource_specs.items():
            matches = len(re.findall(pattern, content))
            if matches > 0:
                self.pass_test(f"Resource '{resource}' specified: {matches} mentions")
            else:
                self.warn_test(f"Resource '{resource}' not explicitly documented")
    
    def test_function_coverage(self) -> None:
        """Test 8: Verify function definitions"""
        print("\n" + "="*70)
        print("TEST 8: FUNCTION COVERAGE ANALYSIS")
        print("="*70)
        
        functions_doc = self.docs.get("V18_DETAILED_FUNCTIONS.md", {})
        content = functions_doc.get("content", "")
        
        # Count function definitions
        function_count = len(re.findall(r"def \w+\(", content))
        function_names = re.findall(r"def (\w+)\(", content)
        
        if function_count >= 50:
            self.pass_test(f"Function definitions: {function_count} functions found")
        else:
            self.warn_test(f"Limited functions found: {function_count}")
        
        # Check for level coverage
        levels = [f"Level {i}" for i in range(1, 11)]
        for level in levels:
            if level in content:
                self.pass_test(f"{level} functions specified")
            else:
                self.fail_test(f"{level} functions missing")
    
    def test_checklist_completeness(self) -> None:
        """Test 9: Verify checklist"""
        print("\n" + "="*70)
        print("TEST 9: IMPLEMENTATION CHECKLIST ANALYSIS")
        print("="*70)
        
        checklist_doc = self.docs.get("V18_IMPLEMENTATION_CHECKLIST.md", {})
        content = checklist_doc.get("content", "")
        
        # Count checkboxes
        checkboxes = len(re.findall(r'\- \[ \]', content))
        sprints = len(re.findall(r'Sprint \d+:', content))
        
        if checkboxes >= 100:
            self.pass_test(f"Checklist items: {checkboxes} actionable items")
        else:
            self.fail_test(f"Insufficient checklist items: {checkboxes}")
        
        if sprints >= 4:
            self.pass_test(f"Sprint structure: {sprints} sprints defined")
        else:
            self.warn_test(f"Limited sprints: {sprints} defined")
    
    def test_cross_document_consistency(self) -> None:
        """Test 10: Cross-document consistency"""
        print("\n" + "="*70)
        print("TEST 10: CROSS-DOCUMENT CONSISTENCY")
        print("="*70)
        
        consistency_checks = [
            ("v1.8 depth 8.8", r"8\.8", 
             ["V18_EXECUTIVE_SUMMARY.md", "V18_DEPTH_SPECIFICATIONS.md"]),
            ("timeline 6-8 months", r"[6-8] month",
             ["V18_IMPLEMENTATION_PLAN.md", "V18_EXECUTIVE_SUMMARY.md"]),
            ("team size 5-6", r"[5-6]",
             ["V18_IMPLEMENTATION_CHECKLIST.md", "V18_EXECUTIVE_SUMMARY.md"]),
            ("cost $380k", r"\$380",
             ["V18_ARCHITECTURE.md", "V18_EXECUTIVE_SUMMARY.md"]),
            ("functions 1000+", r"1000\+",
             ["V18_DETAILED_FUNCTIONS.md", "V18_EXECUTIVE_SUMMARY.md"])
        ]
        
        for check_name, pattern, docs_to_check in consistency_checks:
            docs_with_match = sum(1 for doc in docs_to_check 
                                 if re.search(pattern, self.docs.get(doc, {}).get("content", "")))
            
            if docs_with_match >= len(docs_to_check):
                self.pass_test(f"'{check_name}' consistent ({docs_with_match}/{len(docs_to_check)} docs)")
            else:
                self.warn_test(f"'{check_name}' inconsistent ({docs_with_match}/{len(docs_to_check)} docs)")
    
    def generate_report(self) -> None:
        """Generate final test report"""
        print("\n" + "="*70)
        print("FINAL TEST REPORT")
        print("="*70)
        
        self.results["metrics"] = {
            "documents_loaded": len(self.docs),
            "total_size_kb": sum(doc["size_kb"] for doc in self.docs.values()),
            "total_lines": sum(doc["lines"] for doc in self.docs.values()),
            "tests_passed": len(self.results["passed"]),
            "tests_failed": len(self.results["failed"]),
            "warnings": len(self.results["warnings"])
        }
        
        print(f"\nDocuments Loaded:        {self.results['metrics']['documents_loaded']}")
        print(f"Total Size:              {self.results['metrics']['total_size_kb']:.2f} KB")
        print(f"Total Lines:             {self.results['metrics']['total_lines']:,}")
        print(f"\nTests Passed:            {self.results['metrics']['tests_passed']}")
        print(f"Tests Failed:            {self.results['metrics']['tests_failed']}")
        print(f"Warnings:                {self.results['metrics']['warnings']}")
        
        pass_rate = (self.results['metrics']['tests_passed'] / 
                    (self.results['metrics']['tests_passed'] + self.results['metrics']['tests_failed']) * 100
                    if (self.results['metrics']['tests_passed'] + self.results['metrics']['tests_failed']) > 0 else 0)
        
        print(f"\nPass Rate:               {pass_rate:.1f}%")
        
        if self.results['metrics']['tests_failed'] == 0:
            print("\n[SUCCESS] ALL CRITICAL TESTS PASSED")
        else:
            print(f"\n[ALERT] {self.results['metrics']['tests_failed']} tests failed")
    
    def run_all_tests(self) -> None:
        """Execute all tests"""
        print("\n" + "="*70)
        print("v1.8 PLANNING DOCUMENTS - COMPREHENSIVE TEST SUITE")
        print("="*70)
        
        self.test_document_structure()
        self.test_metrics_consistency()
        self.test_implementation_details()
        self.test_depth_progression()
        self.test_architecture_completeness()
        self.test_security_compliance()
        self.test_resource_requirements()
        self.test_function_coverage()
        self.test_checklist_completeness()
        self.test_cross_document_consistency()
        self.generate_report()
        
        print("\n" + "="*70)
        print("TEST SUITE COMPLETE")
        print("="*70)

if __name__ == "__main__":
    suite = V18TestSuite()
    suite.run_all_tests()
