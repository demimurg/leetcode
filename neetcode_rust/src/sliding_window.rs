use std::collections::HashMap;

/// You are given an array prices where prices[i] is the price of a given stock on the ith day.
/// You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
/// Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
/// [EASY] https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
/// ```rust
/// use neetcode::sliding_window::max_profit;
/// assert_eq!(max_profit(vec![7,1,5,3,6,4]), 5);
/// assert_eq!(max_profit(vec![7,6,4,3,1]), 0);
/// ```
pub fn max_profit(prices: Vec<i32>) -> i32 {
    let (mut max_profit, mut min_price) = (0, std::i32::MAX);
    for price in prices {
        min_price = min_price.min(price);
        max_profit = max_profit.max(price - min_price);
    }
    max_profit
}

/// Given a string s, find the length of the longest substring without repeating characters.
/// [MEDIUM] https://leetcode.com/problems/longest-substring-without-repeating-characters/
/// ```rust
/// use neetcode::sliding_window::length_of_longest_substring;
/// assert_eq!(length_of_longest_substring(String::from("abcabcbb")), 3);
/// assert_eq!(length_of_longest_substring(String::from("bbbbb")), 1);
/// assert_eq!(length_of_longest_substring(String::from("pwwkew")), 3);
/// ```
pub fn length_of_longest_substring(s: String) -> i32 {
    let mut hm: HashMap<char, usize> = HashMap::with_capacity(s.len());
    let mut max_len = 0;
    let mut start = 0;

    for (i, ch) in s.char_indices() {
        if let Some(j) = hm.get(&ch) {
            start = start.max(j + 1);
        }

        hm.insert(ch, i);
        max_len = max_len.max(i - start + 1);
    }

    max_len as i32
}

/// You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character.
/// You can perform this operation at most k times.
/// Return the length of the longest substring containing the same letter you can get after performing the above operations.
/// [MEDIUM] https://leetcode.com/problems/longest-repeating-character-replacement/
/// ```rust
/// use neetcode::sliding_window::character_replacement;
/// assert_eq!(character_replacement(String::from("ABAB"), 2), 4);
/// assert_eq!(character_replacement(String::from("AABABBA"), 1), 4);
/// ```
pub fn character_replacement(s: String, k: i32) -> i32 {
    let mut window: HashMap<u8, i32> = HashMap::new(); // character to count
    let mut max_substr = 0;
    let mut l = 0; // left pointer declaration, right - in loop
    let s = s.into_bytes();

    for r in 0..s.len() {
        *window.entry(s[r]).or_default() += 1;

        let mut window_len = (r - l + 1) as i32;
        while !window.values().any(|count| count + k >= window_len) {
            *window.entry(s[l]).or_default() -= 1;
            l += 1;
            window_len -= 1;
        }

        max_substr = max_substr.max(window_len);
    }

    max_substr
}

/// Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
/// In other words, return true if one of s1's permutations is the substring of s2.
/// [MEDIUM] https://leetcode.com/problems/permutation-in-string/
/// ```rust
/// use neetcode::sliding_window::check_inclusion;
/// assert_eq!(check_inclusion(String::from("ab"), String::from("eidbaooo")), true);
/// assert_eq!(check_inclusion(String::from("ab"), String::from("eidboaoo")), false);
/// assert_eq!(check_inclusion(String::from("adc"), String::from("dcda")), true);
/// ```
pub fn check_inclusion(s1: String, s2: String) -> bool {
    if s1.len() > s2.len() {
        return false;
    }

    let (s1, s2) = (s1.into_bytes(), s2.into_bytes());
    let (mut s1_count, mut s2_substr_count) = (HashMap::new(), HashMap::new());
    for i in 0..s1.len() {
        *s1_count.entry(s1[i]).or_insert(0) += 1;
        *s2_substr_count.entry(s2[i]).or_insert(0) += 1;
    }

    for i in s1.len()..s2.len() {
        if s1_count.eq(&s2_substr_count) {
            return true;
        }
        *s2_substr_count.entry(s2[i]).or_insert(0) += 1;

        let old_key = s2[i - s1.len()];
        *s2_substr_count.entry(old_key).or_insert(0) -= 1;
        if s2_substr_count[&old_key] == 0 {
            s2_substr_count.remove(&old_key);
        }
    }

    s1_count.eq(&s2_substr_count)
}
