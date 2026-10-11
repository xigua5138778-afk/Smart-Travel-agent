// 类型定义

export interface Location {
  longitude: number
  latitude: number
}

export interface Attraction {
  name: string           // ① 景点名称
  address: string        // ② 地址（展示用）
  location: Location     // ③ 坐标 —— 嵌套了上面那个接口
  visit_duration: number // ④ 建议游览时长
  description: string    // ⑤ 景点描述
  category?: string      // ⑥ 分类，可选
  rating?: number        // ⑦ 评分，可选
  image_url?: string     // ⑧ 图片地址，可选
  ticket_price?: number  // ⑨ 门票价格，可选
}       //前五个是必填，后四个带 ? 是可选。

export interface Meal {
  type: 'breakfast' | 'lunch' | 'dinner' | 'snack'
  name: string
  address?: string
  location?: Location
  description?: string
  estimated_cost?: number
}

export interface Hotel {
  name: string
  address: string
  location?: Location
  price_range: string
  rating: string
  distance: string
  type: string
  estimated_cost?: number
}

export interface Budget {
  total_attractions: number
  total_hotels: number
  total_meals: number
  total_transportation: number
  total: number
}

export interface DayPlan {
  date: string
  day_index: number
  description: string
  transportation: string
  accommodation: string
  hotel?: Hotel
  attractions: Attraction[]
  meals: Meal[]
}

export interface WeatherInfo {
  date: string
  day_weather: string
  night_weather: string
  day_temp: number
  night_temp: number
  wind_direction: string
  wind_power: string
}

export interface TripPlan {
  city: string
  start_date: string
  end_date: string
  days: DayPlan[]
  weather_info: WeatherInfo[]
  overall_suggestions: string
  budget?: Budget
}

export interface TripFormData {     // 描述"表单要寄给后端的包裹"长什么样
  city: string
  start_date: string
  end_date: string
  travel_days: number
  transportation: string
  accommodation: string
  preferences: string[]
  free_text_input: string
  dietary_preference?: string
}

export interface TripPlanResponse {
  success: boolean
  message: string
  data?: TripPlan
}

