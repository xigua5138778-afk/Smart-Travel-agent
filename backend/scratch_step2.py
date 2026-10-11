from typing import List, Optional
from pydantic import BaseModel,Field,model_validator



class TripRequest(BaseModel):
    """旅行规划请求"""
    city: str = Field(..., description="目的地城市", example="北京")
    start_date: str = Field(..., description="开始日期 YYYY-MM-DD",example="2025-06-01")
    end_date: str = Field(..., description="结束日期 YYYY-MM-DD", example="2025-06-03")
    travel_days: int = Field(..., description="旅行天数", ge=1, le=30, example=3)
    transportation: str = Field(..., description="交通方式", example="公共交通")
    accommodation: str = Field(..., description="住宿偏好", example="经济型酒店")
    preferences: List[str] = Field(default=[], description="旅行偏好标签", example=["历史文化", "美食"])
    free_text_input: Optional[str] = Field(default="", description="额外要求", example="希望多安排一些博物馆")

    @model_validator(mode= 'after')
    def check_days(self):
        if self.start_date > self.end_date:
            print(self.start_date)
            raise ValueError(f"结束日期({self.end_date})不能早于开始日期({self.start_date})")
        return  self


    class Config:
        json_schema_extra = {
            "example": {
                "city": "北京",
                "start_date": "2025-06-01",
                "end_date": "2025-06-03",
                "travel_days": 3,
                "transportation": "公共交通",
                "accommodation": "经济型酒店",
                "preferences": ["历史文化", "美食"],
                "free_text_input": "希望多安排一些博物馆"
            }
        }

# 用例①：天数为负
# TripRequest(city="湘潭", start_date="2025-06-03", end_date="2025-06-02", travel_days=-1, transportation="公共交通",accommodation="经济型酒店")

# # 用例②：故意不写 city
# TripRequest(start_date="2025-06-03", end_date="2025-06-02", travel_days=1, transportation="公共交通",accommodation="经济型酒店")

#
# # 用例③：类型错误
TripRequest(city="", start_date="2025-06-03", end_date="2025-06-02", travel_days=3, transportation="骑骆驼",accommodation="经济型酒店")


