import axios from "axios";
const login = axios.create({
    // baseURL :"https://agol-bvtwuypbsq-km.a.run.app/operations/",
    baseURL :"http://127.0.0.1:8000/operations",
})

export default login