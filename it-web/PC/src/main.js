import App from "./App"
import "./index.css"
import "@/assets/reset.css"
import router from "@/router/index"
import { createApp } from "vue"

const app = createApp(App)
app.use(router)
app.mount("#app")
