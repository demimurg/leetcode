use std::{cmp::Ordering, collections::HashMap};

/// Given a sorted (in ascending order) integer array `nums` of `n` elements and a `target` value,
/// write a function to search `target` in `nums`. If `target` exists, then return its index, otherwise return `-1`.
/// [EASY] https://leetcode.com/problems/binary-search/
/// ```
/// use neetcode::binary_search::search;
/// assert_eq!(search(vec![-1,0,3,5,9,12], 9), 4);
/// assert_eq!(search(vec![-1,0,3,5,9,12], 2), -1);
/// assert_eq!(search(vec![-1,0,3,5,9,12], -1), 0);
/// assert_eq!(search(vec![5], -5), -1);
/// ```
pub fn search(nums: Vec<i32>, target: i32) -> i32 {
    let (mut l, mut r) = (0, nums.len() as i32 - 1);
    while l <= r {
        let i = (l + r) / 2;
        match nums[i as usize].cmp(&target) {
            Ordering::Greater => r = i - 1,
            Ordering::Less => l = i + 1,
            Ordering::Equal => return i as i32,
        }
    }
    -1
}

/// You are given an `m x n` integer matrix `matrix` with the following two properties:
/// * Each row is sorted in non-decreasing order.
/// * The first integer of each row is greater than the last integer of the previous row.
/// Given an integer `target`, return `true` if `target` is in `matrix` or `false` otherwise.
/// You must write a solution in `O(log(m * n))` time complexity.
/// [MEDIUM] https://leetcode.com/problems/search-a-2d-matrix/
/// ```
/// use neetcode::binary_search::search_matrix;
/// assert_eq!(search_matrix(vec![
///     vec![1, 3, 5, 7 ],
///     vec![10,11,16,20],
///     vec![23,30,34,60],
/// ], 3), true);
/// assert_eq!(search_matrix(vec![
///     vec![1, 3, 5, 7 ],
///     vec![10,11,16,20],
///     vec![23,30,34,60],
/// ], 13), false);
/// ```
pub fn search_matrix(matrix: Vec<Vec<i32>>, target: i32) -> bool {
    let (mut up, mut down, mut row_n) = (0, matrix.len() as i32 - 1, 0);
    while up <= down {
        row_n = up + (down - up) / 2;
        if matrix[row_n as usize][0] > target {
            down = row_n - 1;
        } else if *matrix[row_n as usize].last().unwrap() < target {
            up = row_n + 1;
        } else {
            break;
        }
    }
    if up > down {
        return false;
    }

    let row = &matrix[row_n as usize];
    let (mut l, mut r) = (0, row.len() as i32 - 1);
    while l <= r {
        let i = (l + r) / 2;
        match row[i as usize].cmp(&target) {
            Ordering::Greater => r = i - 1,
            Ordering::Less => l = i + 1,
            Ordering::Equal => return true,
        }
    }
    false
}

/// Koko loves to eat bananas. There are `N` piles of bananas, the `i`-th pile has `piles[i]` bananas. The guards have gone and will come back in `H` hours.
/// Koko can decide her bananas-per-hour eating speed of `K`. Each hour, she chooses some pile of bananas, and eats K bananas from that pile.
/// If the pile has less than `K` bananas, she eats all of them instead, and won’t eat any more bananas during this hour.
/// Koko likes to eat slowly, but still wants to finish eating all the bananas before the guards come back.
/// Return the minimum integer `K` such that she can eat all the bananas within `H` hours.
/// [MEDIUM] https://leetcode.com/problems/koko-eating-bananas/
/// ```
/// use neetcode::binary_search::min_eating_speed;
/// assert_eq!(min_eating_speed(vec![3,6,7,11], 8), 4);
/// assert_eq!(min_eating_speed(vec![30,11,23,4,20], 5), 30);
/// assert_eq!(min_eating_speed(vec![30,11,23,4,20], 6), 23);
/// ```
pub fn min_eating_speed(piles: Vec<i32>, hours_available: i32) -> i32 {
    let (mut from_speed, mut to_speed) = (1, *piles.iter().max().unwrap());
    let mut min_speed = to_speed;
    while from_speed <= to_speed {
        let speed = (from_speed + to_speed) / 2;
        let hours: i64 = piles
            .iter()
            .map(|&bananas| ((bananas + speed - 1) / speed) as i64)
            .sum();

        match hours.cmp(&(hours_available as i64)) {
            Ordering::Greater => from_speed = speed + 1,
            Ordering::Less | Ordering::Equal => {
                min_speed = min_speed.min(speed);
                to_speed = speed - 1;
            }
        }
    }
    min_speed
}

/// Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
/// For example, the array nums = [0,1,2,4,5,6,7] might become:
/// - [4,5,6,7,0,1,2] if it was rotated 4 times.
/// - [0,1,2,4,5,6,7] if it was rotated 7 times.
/// Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
/// Given the sorted rotated array nums of unique elements, return the minimum element of this array.
/// You must write an algorithm that runs in O(log n) time.
/// [MEDIUM] https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
/// ```
/// use neetcode::binary_search::find_min;
/// assert_eq!(find_min(vec![3,4,5,1,2]), 1);
/// assert_eq!(find_min(vec![4,5,6,7,0,1,2]), 0);
/// assert_eq!(find_min(vec![1,2,3,4,5]), 1);
/// assert_eq!(find_min(vec![2,3,4,5,1]), 1);
/// assert_eq!(find_min(vec![5,1,2,3,4]), 1);
/// assert_eq!(find_min(vec![1,2]), 1);
/// ```
pub fn find_min(nums: Vec<i32>) -> i32 {
    let (mut l, mut r) = (0, nums.len() - 1);
    if nums[l] < nums[r] {
        return nums[l];
    }

    while r - l > 1 {
        let m = (l + r) / 2;
        if nums[m] < nums[l] {
            r = m;
        } else if nums[m] > nums[r] {
            l = m;
        }
    }
    nums[r]
}

/// There is an integer array nums sorted in ascending order (with distinct values).
/// Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k
/// (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
/// For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
/// Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums,
/// or -1 if it is not in nums.
/// You must write an algorithm with O(log n) runtime complexity.
/// [MEDIUM] https://leetcode.com/problems/search-in-rotated-sorted-array/
/// ```
/// use neetcode::binary_search::search_rotated_array;
/// assert_eq!(search_rotated_array(vec![4,5,6,7,0,1,2], 0), 4);
/// assert_eq!(search_rotated_array(vec![4,5,6,7,0,1,2], 3), -1);
/// assert_eq!(search_rotated_array(vec![1], 0), -1);
/// ```
pub fn search_rotated_array(nums: Vec<i32>, target: i32) -> i32 {
    let (mut l, mut r) = (0, nums.len() - 1);

    while l <= r {
        let m = (l + r) / 2;
        if nums[m] == target {
            return m as i32;
        }

        if nums[l] <= nums[m] {
            if target < nums[l] || target > nums[m] {
                l = m + 1;
            } else {
                r = m - 1;
            }
        } else {
            if target < nums[m] || target > nums[r] {
                r = m - 1;
            } else {
                l = m + 1;
            }
        }
    }

    -1
}

/// Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.
/// Implement the TimeMap class:
/// - TimeMap() Initializes the object of the data structure.
/// - void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
/// - String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
/// ```
/// use neetcode::binary_search::TimeMap;
/// let mut time_map = TimeMap::new();
/// time_map.set("foo".to_string(), "bar".to_string(), 1);
/// assert_eq!(time_map.get("foo".to_string(), 1), "bar".to_string());
/// assert_eq!(time_map.get("foo".to_string(), 3), "bar".to_string());
/// time_map.set("foo".to_string(), "bar2".to_string(), 4);
/// assert_eq!(time_map.get("foo".to_string(), 4), "bar2".to_string());
/// assert_eq!(time_map.get("foo".to_string(), 5), "bar2".to_string());
/// ```
pub struct TimeMap {
    storage: HashMap<String, Vec<(i32, String)>>,
}
impl TimeMap {
    pub fn new() -> Self {
        TimeMap {
            storage: HashMap::new(),
        }
    }

    pub fn set(&mut self, key: String, value: String, timestamp: i32) {
        self.storage
            .entry(key)
            .or_default()
            .push((timestamp, value));
    }

    pub fn get(&self, key: String, timestamp: i32) -> String {
        let values = self.storage.get(&key);
        if values.is_none() {
            return String::new();
        }

        let values = values.unwrap();
        let mut nearest_value = String::new();
        let (mut l, mut r) = (0, values.len());
        while l < r {
            let m = (l + r) / 2;
            if values[m].0 <= timestamp {
                l = m + 1;
                nearest_value = values[m].1.clone();
            } else {
                r = m;
            }
        }

        nearest_value
    }
}
