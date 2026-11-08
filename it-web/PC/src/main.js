import App from "./App"
import "./index.css"
import { createPinia } from "pinia"
import "@/assets/reset.css"
import router from "@/router/index"
import { createApp } from "vue"

const app = createApp(App)
app.use(createPinia())
app.use(router)
app.mount("#app")
