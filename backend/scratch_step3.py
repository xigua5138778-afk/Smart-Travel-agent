from app.models.schemas import TripRequest                    # ← 补上这个 import
from app.agents.trip_planner_agent import MultiAgentTripPlanner

# ① 先造一个"请求对象"
req = TripRequest(
    city="北京",
    start_date="2026-10-01",
    end_date="2026-10-03",
    travel_days=3,
    transportation="公共交通",
    accommodation="经济型酒店",
    preferences=["历史文化"],
    free_text_input="想吃点路边摊",          # 顺便也填上
    dietary_preference="清淡少油",           # ← 这才是新字段
)

# # ② 再造空壳、调用
p = MultiAgentTripPlanner.__new__(MultiAgentTripPlanner)
# q = p._build_planner_query(req, "景点文字", "天气文字", "酒店文字")
# print(q)



print('=== 用例① 非 JSON ===')
plan = p._parse_response("这不是JSON，我随便说点什么", req)
print('返回类型:', type(plan).__name__, '| 城市:', plan.city, '| 天数:', len(plan.days))
print('第一个景点名:', plan.days[0].attractions[0].name if plan.days and plan.days[0].attractions else '(无)')

print()
print('=== 用例② 合法 JSON 但缺字段 ===')
plan2 = p._parse_response('```json\n{"city": "北京"}\n```', req)
print('返回类型:', type(plan2).__name__, '| 城市:', plan2.city, '| 天数:', len(plan2.days))
print('第一个景点名:', plan2.days[0].attractions[0].name if plan2.days and plan2.days[0].attractions else '(无)')