use std::{
    cmp::Reverse,
    collections::{BinaryHeap, HashMap, HashSet},
};

/// Given an integer array nums, return true if any value appears at least twice in the array,
/// and return false if every element is distinct.
/// [EASY] https://leetcode.com/problems/contains-duplicate
/// ```
/// use neetcode::arrays::contains_duplicate;
/// assert!(!contains_duplicate(vec!(1, 2, 3, 4, 5)));
/// assert!(contains_duplicate(vec!(1, 2, 3, 3)));
/// assert!(!contains_duplicate(vec!(1)));
/// assert!(!contains_duplicate(vec!()));
/// ```
pub fn contains_duplicate(nums: Vec<i32>) -> bool {
    let mut unique = HashSet::with_capacity(nums.len());
    for num in nums {
        if !unique.insert(num) {
            return true;
        }
    }
    false
}

/// Given two strings s and t, return true if t is an anagram of s, and false otherwise.
/// An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
/// typically using all the original letters exactly once.
/// [EASY] https://leetcode.com/problems/valid-anagram
/// ```
/// use neetcode::arrays::is_anagram;
/// assert!(is_anagram("anagram".to_string(), "nagaram".to_string()));
/// assert!(!is_anagram("rat".to_string(), "car".to_string()));
/// assert!(!is_anagram("aaab".to_string(), "abbb".to_string()));
/// ```
pub fn is_anagram(s: String, t: String) -> bool {
    if s.len() != t.len() {
        return false;
    }

    let mut diff: HashMap<char, i32> = HashMap::new();
    for (s_char, t_char) in s.chars().zip(t.chars()) {
        *diff.entry(s_char).or_default() += 1;
        *diff.entry(t_char).or_default() -= 1;
    }

    diff.values().all(|&count| count == 0)
}

/// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
/// You may assume that each input would have exactly one solution, and you may not use the same element twice.
/// You can return the answer in any order.
/// [EASY] https://leetcode.com/problems/two-sum
/// ```
/// use neetcode::arrays::two_sum;
/// assert_eq!(two_sum(vec![2,7,11,15], 9), vec![0, 1]);
/// assert_eq!(two_sum(vec![3,2,4], 6), vec![1, 2]);
/// assert_eq!(two_sum(vec![3,3], 6), vec![0, 1]);
/// ```
pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
    let mut checked = HashMap::with_capacity(nums.len()); // num to i
    for (id_a, num_a) in nums.into_iter().enumerate() {
        let num_b = target - num_a;
        if let Some(id_b) = checked.get(&num_b) {
            return vec![*id_b, id_a as i32];
        }
        checked.insert(num_a, id_a as i32);
    }
    unreachable!()
}

/// Given an array of strings strs, group the anagrams together. You can return the answer in any order.
/// An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
/// typically using all the original letters exactly once.
/// [MEDIUM] https://leetcode.com/problems/group-anagrams
/// ```
/// use neetcode::arrays::group_anagrams;
/// let input = vec!["eat".to_string(), "tea".to_string(), "tan".to_string(), "ate".to_string(), "nat".to_string(), "bat".to_string()];
/// let output = group_anagrams(input);
/// // As the order of groups and order of strings inside each group doesn't matter, we have to check existence of each group manually.
/// assert!(output.contains(&vec!["eat".to_string(), "tea".to_string(), "ate".to_string()]));
/// assert!(output.contains(&vec!["tan".to_string(), "nat".to_string()]));
/// assert!(output.contains(&vec!["bat".to_string()]));
/// ```
pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
    let mut unique: HashMap<Vec<u8>, Vec<String>> = HashMap::new();
    for str in strs {
        let mut letters = vec![0; 26];
        str.bytes().for_each(|b| letters[b as usize - 97] += 1);

        unique.entry(letters).or_default().push(str);
    }

    unique.into_values().collect()
}

/// Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
/// [MEDIUM] https://leetcode.com/problems/top-k-frequent-elements
/// ```
/// use neetcode::arrays::top_k_frequent;
/// assert_eq!(top_k_frequent(vec![1,1,1,2,2,3], 2), [1, 2]);
/// assert_eq!(top_k_frequent(vec![1], 1), vec![1]);
/// ```
pub fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
    let mut count = HashMap::new();
    nums.into_iter()
        .for_each(|x| *count.entry(x).or_insert(0) += 1);

    let mut unique_nums: Vec<_> = count.keys().collect();
    let k = unique_nums.len().min(k as usize);
    // quickselect (Hoare's algorithm) with inversed sort gives us vector
    // unique_nums[..k-1] >= unique_nums[k-1] >= unique_nums[k..]
    unique_nums.select_nth_unstable_by(k - 1, |a, b| count[a].cmp(&count[b]).reverse());

    unique_nums.into_iter().map(|x| *x).take(k).collect()
}
pub fn top_k_frequent_heap(nums: Vec<i32>, k: i32) -> Vec<i32> {
    let mut count: HashMap<i32, i32> = HashMap::new();
    nums.into_iter()
        .for_each(|x| *count.entry(x).or_default() += 1);

    let k = count.len().min(k as usize);
    let mut min_heap = BinaryHeap::with_capacity(k + 1);
    for (num, counter) in count {
        min_heap.push(Reverse((counter, num)));
        if min_heap.len() == k + 1 {
            min_heap.pop();
        }
    }

    let mut top_k = vec![0; k];
    for i in (0..k).rev() {
        top_k[i] = min_heap.pop().unwrap().0 .1;
    }

    top_k
}

/// Given an integer array nums, return an array answer such that each element at index i of the answer
/// is the product of all the numbers in the original array except the one at i
/// Note: Please solve it without division and in O(n).
/// [MEDIUM] https://leetcode.com/problems/product-of-array-except-self
/// ```
/// use neetcode::arrays::product_except_self;
/// assert_eq!(product_except_self(vec![1,2,3,4]), vec![24,12,8,6]);
/// assert_eq!(product_except_self(vec![-1,1,0,-3,3]), vec![0,0,9,0,0]);
/// ```
pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
    let mut product = vec![1; nums.len()];
    let mut left = 1;
    let mut right = 1;

    for i in 0..nums.len() {
        let j = nums.len() - 1 - i;
        product[i] *= left;
        product[j] *= right;

        left *= nums[i];
        right *= nums[j];
    }

    product
}

/// Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
/// 1. Each row must contain the digits 1-9 without repetition.
/// 2. Each column must contain the digits 1-9 without repetition.
/// 3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
/// Note:
/// - A Sudoku board (partially filled) could be valid but is not necessarily solvable.
/// - Only the filled cells need to be validated according to the mentioned rules.
/// [MEDIUM] https://leetcode.com/problems/product-of-array-except-self
/// ```
/// use neetcode::arrays::is_valid_sudoku;
/// let mut board = vec![
///     vec!['5','3','.','.','7','.','.','.','.'],
///     vec!['6','.','.','1','9','5','.','.','.'],
///     vec!['.','9','8','.','.','.','.','6','.'],
///     vec!['8','.','.','.','6','.','.','.','3'],
///     vec!['4','.','.','8','.','3','.','.','1'],
///     vec!['7','.','.','.','2','.','.','.','6'],
///     vec!['.','6','.','.','.','.','2','8','.'],
///     vec!['.','.','.','4','1','9','.','.','5'],
///     vec!['.','.','.','.','8','.','.','7','9']
/// ];
/// assert!(is_valid_sudoku(board));
/// // Same as Example 1, except with the 5 in the top left corner being modified to 8.
/// // Since there are two 8's in the top left 3x3 sub-box, it is invalid
/// let board = vec![
///    vec!['8','3','.','.','7','.','.','.','.'],
///    vec!['6','.','.','1','9','5','.','.','.'],
///    vec!['.','9','8','.','.','.','.','6','.'],
///    vec!['8','.','.','.','6','.','.','.','3'],
///    vec!['4','.','.','8','.','3','.','.','1'],
///    vec!['7','.','.','.','2','.','.','.','6'],
///    vec!['.','6','.','.','.','.','2','8','.'],
///    vec!['.','.','.','4','1','9','.','.','5'],
///    vec!['.','.','.','.','8','.','.','7','9']
/// ];
/// assert!(!is_valid_sudoku(board));
/// ```
pub fn is_valid_sudoku(board: Vec<Vec<char>>) -> bool {
    let mut rows = HashSet::new();
    let mut cols = HashSet::new();
    let mut boxes = HashSet::new();

    for i in 0..9 {
        for j in 0..9 {
            let ch = board[i][j];
            if ch == '.' {
                continue;
            }

            let box_id = i / 3 * 3 + j / 3;
            if !rows.insert((i, ch)) || !cols.insert((j, ch)) || !boxes.insert((box_id, ch)) {
                return false;
            }
        }
    }

    true
}

/// Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
/// You must write an algorithm that runs in O(n) time.
/// [MEDIUM] https://leetcode.com/problems/longest-consecutive-sequence
/// ```
/// use neetcode::arrays::longest_consecutive;
/// assert_eq!(longest_consecutive(vec![100, 4, 200, 1, 3, 2]), 4); // longest [1, 2, 3, 4] (4 elems)
/// assert_eq!(longest_consecutive(vec![0,3,7,2,5,8,4,6,0,1]), 9); // longest [0, 1, 2, 3, 4, 5, 6, 7, 8] (9 elems)
/// ```
pub fn longest_consecutive(nums: Vec<i32>) -> i32 {
    let set: HashSet<i32> = nums.into_iter().collect();
    let mut max_seq = 0;

    for n in &set {
        if set.contains(&(n - 1)) {
            continue;
        }

        let mut seq = 1;
        let mut next = n + 1;
        while set.contains(&next) {
            seq += 1;
            next += 1;
        }

        max_seq = max_seq.max(seq);
    }

    max_seq
}
