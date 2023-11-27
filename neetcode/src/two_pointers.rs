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
/// [MEDIUM] https://leetcode.com/problems/two-sum/
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

/// Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
/// Notice that the solution set must not contain duplicate triplets.
/// ```rust
/// use neetcode::two_pointers::three_sum;
/// assert_eq!(three_sum(vec![-1,0,1,2,-1,-4]), vec![vec![-1,-1,2], vec![-1,0,1]]);
/// assert_eq!(three_sum(vec![0,0,0]), vec![vec![0,0,0]]);
/// assert_eq!(three_sum(vec![-2,0,0,2,2]), vec![vec![-2,0,2]]);
/// ```
pub fn three_sum(mut nums: Vec<i32>) -> Vec<Vec<i32>>{
    nums.sort_unstable();

    let mut res = Vec::new();
    for i in 0..nums.len()-2 {
        if nums[i] > 0 {
            // numbers after i will be bigger than 0, because of sort
            // so we never find pair with sum equals to -nums[i]
            break;
        }
        if i > 0 && nums[i] == nums[i-1] {
            // for same 1st number we will get same 2nd and 3rd, but we don't need duplicates
            continue;
        }

        let (mut l, mut r) = (i+1, nums.len() - 1);
        while l < r {
            match (nums[l] + nums[r]).cmp(&(-nums[i])) {
                Ordering::Less => l += 1,
                Ordering::Greater => r -= 1,
                _ => {
                    let triplet = vec![nums[i], nums[l], nums[r]];
                    if res.last().ne(&Some(&triplet)) {
                        res.push(triplet);
                    }
                    l += 1;
                    r -= 1;
                },
            }
        }
    }

    res
}

/// You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
/// Find two lines that together with the x-axis form a container, such that the container contains the most water.
/// Return the maximum amount of water a container can store.
/// Notice that you may not slant the container.
/// [MEDIUM] https://leetcode.com/problems/container-with-most-water/
/// ```rust
/// use neetcode::two_pointers::max_area;
/// assert_eq!(max_area(vec![1,8,6,2,5,4,8,3,7]), 49);
/// assert_eq!(max_area(vec![1,1]), 1);
/// ```
pub fn max_area(height: Vec<i32>) -> i32 {
    let (mut l, mut r) = (0, height.len()-1);
    let mut last_max = 0;

    while l < r {
        let cur = (r - l) as i32 * height[l].min(height[r]);
        last_max = cur.max(last_max);

        match height[l].cmp(&height[r]) {
            Ordering::Less => l += 1,
            Ordering::Greater =>  r -= 1,
            Ordering::Equal => {
                l += 1;
                r -= 1;
            },
        }
    }

    last_max
}
