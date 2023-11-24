/// Given a string `s` containing just the characters '(', ')', '{', '}', '[' and ']',
/// determine if the input string is valid.
/// An input string is valid if:
/// 1. Open brackets must be closed by the same type of brackets.
/// 2. Open brackets must be closed in the correct order.
/// 3. Every close bracket has a corresponding open bracket of the same type.
/// [EASY] https://leetcode.com/problems/valid-parentheses/
/// ```
/// use neetcode::stack::is_valid;
/// assert!(is_valid("()".to_string()));
/// assert!(is_valid("()[]{}".to_string()));
/// assert!(!is_valid("(]".to_string()));
/// assert!(!is_valid("([)]".to_string()));
/// assert!(is_valid("{[]}".to_string()));
/// ```
pub fn is_valid(s: String) -> bool {
    let mut open_brackets = Vec::new();
    for b in s.bytes() {
        let failed_to_close = match b {
            b')' => open_brackets.pop().ne(&Some(b'(')),
            b'}' => open_brackets.pop().ne(&Some(b'{')),
            b']' => open_brackets.pop().ne(&Some(b'[')),
            _ => {
                open_brackets.push(b);
                false
            }
        };
        if failed_to_close {
            return false;
        }
    }
    open_brackets.is_empty()
}

/// Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
/// [MEDIUM] https://leetcode.com/problems/min-stack/
/// ```
/// use neetcode::stack::MinStack;
/// let mut min_stack = MinStack::new();
/// min_stack.push(-2);
/// min_stack.push(0);
/// min_stack.push(-3);
/// assert_eq!(min_stack.get_min(), -3);
/// min_stack.pop();
/// assert_eq!(min_stack.top(), 0);
/// assert_eq!(min_stack.get_min(), -2);
/// ```
pub struct MinStack {
    values: Vec<(i32, i32)>,
}

impl MinStack {
    pub fn new() -> Self {
        return MinStack { values: Vec::new() };
    }

    pub fn push(&mut self, val: i32) {
        let stored_min = self.values.last().unwrap_or(&(0, val)).1;
        self.values.push((val, val.min(stored_min)));
    }

    pub fn pop(&mut self) {
        self.values.pop();
    }

    pub fn top(&self) -> i32 {
        self.values.last().unwrap().0
    }

    pub fn get_min(&self) -> i32 {
        self.values.last().unwrap().1
    }
}

/// You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
/// Evaluate the expression. Return an integer that represents the value of the expression.
/// [MEDIUM] https://leetcode.com/problems/evaluate-reverse-polish-notation/
/// ```rust
/// use neetcode::stack::eval_rpn;
/// assert_eq!(eval_rpn(vec!["2".to_string(), "1".to_string(), "+".to_string(), "3".to_string(), "*".to_string()]), 9);
/// assert_eq!(eval_rpn(vec!["4".to_string(), "13".to_string(), "5".to_string(), "/".to_string(), "+".to_string()]), 6);
/// ```
pub fn eval_rpn(tokens: Vec<String>) -> i32 {
    let mut numbers: Vec<i32> = Vec::new();
    for tok in tokens {
        if let Ok(n) = tok.parse::<i32>() {
            numbers.push(n);
            continue;
        }

        let b = numbers.pop().unwrap();
        let a = numbers.pop().unwrap();
        match tok.as_str() {
            "+" => numbers.push(a + b),
            "-" => numbers.push(a - b),
            "*" => numbers.push(a * b),
            "/" => numbers.push(a / b),
            _ => (),
        }
    }
    *numbers.last().unwrap()
}

/// Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses
/// [MEDIUM] https://leetcode.com/problems/generate-parentheses/
/// ```
/// use neetcode::stack::generate_parenthesis;
/// let want = vec![
///    "((()))",
///    "(()())",
///    "(())()",
///    "()(())",
///    "()()()"
/// ];
/// let mut got = generate_parenthesis(3);
/// got.sort();
/// assert_eq!(got, want);
/// ```
pub fn generate_parenthesis(n: i32) -> Vec<String> {
    let mut result = Vec::new();
    let mut str = String::with_capacity(n as usize * 2);
    create(&mut result, &mut str, n, n);
    result
}
fn create(result: &mut Vec<String>, cur: &mut String, open: i32, close: i32) {
    if open == 0 && close == 0 {
        result.push(cur.clone());
        return;
    }

    if open > 0 {
        cur.push('(');
        create(result, cur, open - 1, close);
        cur.pop();
    }
    if close > open {
        cur.push(')');
        create(result, cur, open, close - 1);
        cur.pop();
    }
}

/// Given an array of integers temperatures represents the daily temperatures, return an array answer
/// such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
/// If there is no future day for which this is possible, keep answer[i] == 0 instead.
/// [MEDIUM] https://leetcode.com/problems/daily-temperatures/
/// ```
/// use neetcode::stack::daily_temperatures;
/// assert_eq!(daily_temperatures(vec![73, 74, 75, 71, 69, 72, 76, 73]), vec![1, 1, 4, 2, 1, 1, 0, 0]);
/// assert_eq!(daily_temperatures(vec![30, 40, 50, 60]), vec![1, 1, 1, 0]);
/// assert_eq!(daily_temperatures(vec![30, 60, 90]), vec![1, 1, 0]);
/// ```
pub fn daily_temperatures(temperatures: Vec<i32>) -> Vec<i32> {
    let mut result = vec![0; temperatures.len()];
    let mut stack = Vec::new();

    for (i, &temp) in temperatures.iter().enumerate() {
        while let Some(&j) = stack.last() {
            if temperatures[j] >= temp {
                break;
            }
            stack.pop();
            result[j] = (i - j) as i32;
        }
        stack.push(i);
    }

    result
}

/// There are n cars going to the same destination along a one-lane road. The destination is target miles away.
/// You are given two integer array position and speed, both of length n, where position[i] is the position of the ith car and speed[i] is the speed of the ith car (in miles per hour).
/// A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same speed. The faster car will slow down to match the slower car's speed. The distance between these two cars is ignored (i.e., they are assumed to have the same position).
/// A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single car is also a car fleet.
/// If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.
/// Return the number of car fleets that will arrive at the destination.
/// [MEDIUM] https://leetcode.com/problems/car-fleet/description/
/// ```
/// use neetcode::stack::car_fleet;
/// assert_eq!(car_fleet(12, vec![10,8,0,5,3], vec![2,4,1,1,3]), 3);
/// assert_eq!(car_fleet(10, vec![3], vec![3]), 1);
/// assert_eq!(car_fleet(100, vec![0,2,4], vec![4,2,1]), 1);
/// ```
pub fn car_fleet(target: i32, position: Vec<i32>, speed: Vec<i32>) -> i32 {
    let mut cars: Vec<_> = position.into_iter().zip(speed).collect();
    cars.sort_unstable_by(|a, b| b.0.cmp(&a.0)); // sort by position in descending order

    let mut fleets_num = 0;
    let mut fleet_arrive = 0_f32;
    for (position, speed) in cars {
        let car_arrive = (target - position) as f32 / speed as f32; // time to reach target for current car (without slow down)
        if car_arrive > fleet_arrive {
            // this car slower than current fleet, so it will create own fleet
            fleets_num += 1;
            fleet_arrive = car_arrive;
        }
    }

    fleets_num
}
