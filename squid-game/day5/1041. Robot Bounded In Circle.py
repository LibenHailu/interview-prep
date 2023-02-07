class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x,y,dx,dy = 0,0,0,1
        for instruction in instructions:
            if instruction == 'G':
                x, y = x + dx, y + dy
            elif instruction == 'L':
                dx, dy = -1 * dy, dx
            else:
                dx, dy = dy, -1 * dx
        
        return (x,y) == (0,0) or (dx,dy) != (0,1)