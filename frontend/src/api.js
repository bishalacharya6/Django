// it will intercept and use automatic headers
// Settig axios request tokens. 

import { ACCESS_TOKEN } from "./constants"
import axios from axios

const api = axios.create({
    baseURL: import.meta.env.VITE_API_URL // Import anything that is specify in any env variabls. 
})

api.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem(ACCESS_TOKEN);
        if (token){
            config.headers.Authorization = `Bearer ${token}` //The way for using jwt token
        }
        return config
    },
    (error)=>{
        return Promise.reject(error)
    }
    
)

export default api