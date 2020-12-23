#import swagger_server.test.analysis_test
#import swagger_server.test.location_test

import location_test
import analysis_test

def run_tests():
    print("Running Analysis Tests:")
    analysis_test.run_tests()

    print("Running Location Tests:")
    location_test.run_tests()


run_tests()