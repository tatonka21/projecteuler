#include "prime_utils.hpp"
#include <cmath>

// This function returns a boolean value indicating whether the input "n" is a primer number or not.
bool is_prime(size_t n) {
    if (n == 0 or n == 1) return false;
    if (n == 2) return true;
    if (n % 2 == 0) return false;

    for (size_t i = 3; i <= (size_t) sqrt((double) n); i++) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}
