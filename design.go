package leetcode

import (
	"math"
	"math/rand"
)

// Given an integer array nums, design an algorithm to randomly shuffle the array.
// All permutations of the array should be equally likely as a result of the shuffling.
// https://leetcode.com/explore/interview/card/top-interview-questions-easy/98/design/670/

type Solution struct {
	original []int
}

func (s *Solution) Reset() []int {
	return s.original
}

func (s *Solution) Shuffle() []int {
	size := len(s.original)
	shuffled := make([]int, size)
	copy(shuffled, s.original)

	for i := 0; i < size; i++ {
		j := rand.Intn(size)
		shuffled[i], shuffled[j] = shuffled[j], shuffled[i]
	}

	return shuffled
}

// Design a values that supports push, pop, top, and retrieving the minimum element in constant time.
//
// Implement the MinStack class:
//
// MinStack() initializes the values object.
// void push(int val) pushes the element val onto the values.
// void pop() removes the element on the top of the values.
// int top() gets the top element of the values.
// int getMin() retrieves the minimum element in the values.
// https://leetcode.com/explore/interview/card/top-interview-questions-easy/98/design/562/

type MinStack struct {
	min    int
	values []int
}

func (s *MinStack) Push(val int) {
	if val < s.min {
		s.min = val
	}
	s.values = append(s.values, val)
}

func (s *MinStack) Pop() {
	last := len(s.values) - 1
	top := s.values[last]
	s.values = s.values[:last]

	if top == s.min {
		s.min = math.MaxInt
		for _, val := range s.values {
			if val < s.min {
				s.min = val
			}
		}
	}
}

func (s *MinStack) Top() int {
	return s.values[len(s.values)-1]
}

func (s *MinStack) GetMin() int {
	return s.min
}
