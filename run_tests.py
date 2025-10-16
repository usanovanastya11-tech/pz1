#!/usr/bin/env python3
"""
Main test runner for CI/CD
"""
import sys
import os

def run_all_tests():
    """Run all test suites"""
    print("🚀 Starting test suite...")
    
    # Run unit tests
    print("\n📋 Running unit tests...")
    from tests.test_units import test_greet, test_farewell, test_multiply, test_calculate_stats, test_validate_email
    test_greet()
    test_farewell()
    test_multiply()
    test_calculate_stats()
    test_validate_email()
    
    # Run integration tests
    print("\n🔄 Running integration tests...")
    from tests.test_integration import test_module_imports, test_greet_farewell_flow
    test_module_imports()
    test_greet_farewell_flow()
    
    print("\n🎉 All tests completed successfully!")
    return True

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
    from tests.test_units import test_power
    test_power()
