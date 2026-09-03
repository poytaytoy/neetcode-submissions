impl Solution {
    
    
    pub fn trap(height: Vec<i32>) -> i32 {
        if height.len() <= 2 {
            return 0;
        }

        let mut max_height_cache = vec![0; height.len()];
        let mut curr_max = 0;

        for i in (0..height.len()).rev() {
            max_height_cache[i] = curr_max;
            curr_max = curr_max.max(height[i]);
        }

        let mut left_max = 0;
        let mut water = 0;

        for i in 0..height.len() {
            let water_level = left_max.min(max_height_cache[i]);

            if water_level > height[i] {
                water += water_level - height[i];
            }

            left_max = left_max.max(height[i]);
        }

        water
    }
}
