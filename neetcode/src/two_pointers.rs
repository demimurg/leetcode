use std::cmp::Ordering;

/// A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
/// it reads the same forward and backward. Alphanumeric characters include letters and numbers.
/// Given a string s, return true if it is a palindrome, or false otherwise.
/// [EASY] https://leetcode.com/problems/valid-palindrome/
/// ```rust
/// use neetcode::two_pointers::is_palindrome;
/// assert!(is_palindrome("A man, a plan, a canal: Panama".to_string()));
/// assert!(!is_palindrome("race a car".to_string()));
/// assert!(is_palindrome(" ".to_string()));
/// ```
pub fn is_palindrome(s: String) -> bool {
    let s = s.as_bytes();
    let (mut start, mut end) = (0_usize, s.len() - 1);

    while start < end {
        if !s[start].is_ascii_alphanumeric() {
            start += 1;
        } else if !s[end].is_ascii_alphanumeric() {
            end -= 1;
        } else if s[start].to_ascii_lowercase() != s[end].to_ascii_lowercase() {
            return false;
        } else {
            start += 1;
            end -= 1;
        }
    }

    true
}

/// Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
/// find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1]
/// and numbers[index2] where 1 <= index1 < index2 < numbers.length.
/// Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
/// The tests are generated such that there is exactly one solution. You may not use the same element twice.
/// Your solution must use only constant extra space.
/// ```rust
/// use neetcode::two_pointers::two_sum;
/// assert_eq!(two_sum(vec![2,7,11,15], 9), vec![1,2]);
/// assert_eq!(two_sum(vec![2,3,4], 6), vec![1,3]);
/// assert_eq!(two_sum(vec![-1,0], -1), vec![1,2]);
/// ```
pub fn two_sum(numbers: Vec<i32>, target: i32) -> Vec<i32> {
    let (mut l, mut r) = (0, numbers.len() - 1);
    loop {
        match (numbers[l] + numbers[r]).cmp(&target) {
            Ordering::Greater => r -= 1,
            Ordering::Less => l += 1,
            _ => return vec![l as i32+1, r as i32 +1],
        }
    }
}