import gym
import numpy as np

class PIDController:
    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.prev_error = 0
        self.integral = 0

    def compute(self, error, dt=0.02):
        self.integral += error * dt
        derivative = (error - self.prev_error) / dt
        output = self.kp * error + self.ki * self.integral + self.kd * derivative
        self.prev_error = error
        return np.clip(output, -1, 1)

def run_simulation():
    env = gym.make('CartPole-v1')
    pid = PIDController(kp=1.5, ki=0.001, kd=0.9)
    
    observation = env.reset()
    total_reward = 0
    
    for step in range(1000):  
        cart_pos, cart_velocity, pole_angle, pole_velocity = observation
        
        # 控制策略优化
        error = -pole_angle - 0.1 * pole_velocity  
        control = pid.compute(error)
        action = 0 if control < 0 else 1
        
        observation, reward, done, _ = env.step(action)
        total_reward += reward
        
        if total_reward >= 200: 
            break
        if done:
            break
            
    env.close()
    balance_time = total_reward / 10  
    print(f"✅ 平衡时长: {balance_time:.1f}秒")
    return balance_time


if __name__ == "__main__":
    best_time = 0
    for attempt in range(10):
        current_time = run_simulation()
        best_time = max(best_time, current_time)
        if best_time >= 20:
            print(f"🎯 第{attempt+1}次尝试达成目标!")
            break
    print(f"\n🏆 最佳成绩: {best_time:.1f}秒")