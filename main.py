from pkg.plugin.context import register, handler, llm_func, BasePlugin, APIHost, EventContext
from pkg.plugin.events import *
import random

# 食物列表
food = [
    "豆浆油条",
    "鸡蛋灌饼",
    "皮蛋瘦肉粥",
    "牛肉面",
    "黄焖鸡米饭",
    "麻辣香锅",
    "寿司拼盘",
    "意大利面",
    "蔬菜沙拉",
    "牛排套餐"
]

"""
当用户输入"早上/中午/晚上吃什么"时，回复推荐食物
"""

class MealRecommendPlugin(BasePlugin):

    # 插件加载时触发
    def __init__(self, host: APIHost):
        pass

    # 异步初始化
    async def initialize(self):
        pass

    # 当收到个人消息时触发
    @handler(PersonNormalMessageReceived)
    async def person_message_handler(self, ctx: EventContext):
        msg = ctx.event.text_message.strip()  # 去除首尾空格
        
        if msg == "早上吃什么":
            meal_time = "早上"
        elif msg == "中午吃什么":
            meal_time = "中午"
        elif msg == "晚上吃什么":
            meal_time = "晚上"
        else:
            return  # 不是询问餐食的消息，直接返回
            
        # 随机选择食物
        selected_food = random.choice(food)
        
        # 输出调试信息
        self.ap.logger.debug("推荐{}食物: {}".format(meal_time, selected_food))
        
        # 回复消息
        ctx.add_return("reply", ["普拉娜建议{}吃{}哦".format(meal_time, selected_food)])
        
        # 阻止该事件默认行为（向接口获取回复）
        ctx.prevent_default()

    # 当收到群消息时触发
    @handler(GroupNormalMessageReceived)
    async def group_message_handler(self, ctx: EventContext):
        msg = ctx.event.text_message.strip()  # 去除首尾空格
        
        if msg == "早上吃什么":
            meal_time = "早上"
        elif msg == "中午吃什么":
            meal_time = "中午"
        elif msg == "晚上吃什么":
            meal_time = "晚上"
        else:
            return  # 不是询问餐食的消息，直接返回
            
        # 随机选择食物
        selected_food = random.choice(food)
        
        # 输出调试信息
        self.ap.logger.debug("推荐{}食物: {}".format(meal_time, selected_food))
        
        # 回复消息
        ctx.add_return("reply", ["普拉娜建议{}吃{}哦".format(meal_time, selected_food)])
        
        # 阻止该事件默认行为（向接口获取回复）
        ctx.prevent_default()

    # 插件卸载时触发
    def __del__(self):
        pass