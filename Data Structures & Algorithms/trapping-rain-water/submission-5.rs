impl Solution {
    
    fn rain_water_trapped(potential_water: i32, accum_water: i32, height: Vec<i32>, max_height_cache: Vec<i32>, index: usize, max_height: i32) -> i32{

        if index + 1 == height.len(){
            if (height[index] >= max_height){
                return accum_water + potential_water; 
            }

            return accum_water; 
        }

        let index_value = height[index]; 
        

        if max_height > height[index]{
            let new_potential_water = potential_water + (max_height - height[index]); 
            return Self::rain_water_trapped(new_potential_water, accum_water, height, max_height_cache, index + 1, max_height); 
        } else {
            let new_max_height = height[index].min(max_height_cache[index]);

            return Self::rain_water_trapped(0, accum_water + potential_water, height, max_height_cache, index + 1, new_max_height);
            
        }
    }
    
    pub fn trap(height: Vec<i32>) -> i32 {
        if height.len() == 0 || height.len() == 1{
            return 0 
        }

        let mut max_height_cache: Vec<i32> = vec![0; height.len()]; 

        let mut curr_max = -1; 

        for i in (0..height.len()).into_iter().rev(){
            if i == height.len() - 1{ 
                max_height_cache[i] = -1;
                continue;  
            }

            curr_max = curr_max.max(height[i + 1]);
            max_height_cache[i] = curr_max;
        }

        let first_value = height[0].min(max_height_cache[0]); 

        Self::rain_water_trapped(0, 0, height, max_height_cache, 1, first_value)
    }
}
