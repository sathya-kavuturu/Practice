// https://leetcode.com/problems/container-with-most-water/

// You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

// Find two lines that together with the x-axis form a container, such that the container contains the most water.

// Return the maximum amount of water a container can store.

// Notice that you may not slant the container.



// Example 1:


// Input: height = [1,8,6,2,5,4,8,3,7]
// Output: 49
// Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
// Example 2:

// Input: height = [1,1]
// Output: 1
 

// Constraints:

// n == height.length
// 2 <= n <= 105
// 0 <= height[i] <= 104


function mostWaterBruteForce(height){
    let maxArea =0;
    if(height.length == 0 || height.length ==1){
        return 0;
    }
    for(let a=0; a<height.length; a++){
        for(let b= a+1; b<height.length; b++){
            // area= height*width
            let area = Math.min(height[a],height[b])*(b-a); 
            if (area>maxArea){
                maxArea = area;
            }
        }
    }

    return maxArea;
}

function mostWater(height){
    let p1 = 0;
    let p2 = height.length-1;
    let maxArea = 0;
    while(p1<p2){
        let area = Math.min(height[p1], height[p2])*(p2-p1);
        maxArea = Math.max(maxArea, area);
        if(height[p1] <= height[p2]){
            p1++;
        }else{
            p2--;
        }
    } 
    return maxArea;
}

//console.log(mostWaterBruteForce([1,8,6,2,5,4,8,3,7]))
//console.log(mostWaterBruteForce([7,1,2,3,9]))
console.log(mostWater([7,1,2,3,9]))
