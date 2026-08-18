import uviewPlus from "@/uview-plus"
import App from "./App"
import "@/assets/css/reset.css"
import { createSSRApp } from "vue"

const createApp = () => {
	const app = createSSRApp(App)

	app.use(uviewPlus)

	return {app: app }
}
export {createApp}