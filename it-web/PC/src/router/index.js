import Home from "@/pages/home"
import { createRouter, createWebHashHistory } from "vue-router"

const constRoutes = [
	{
		path: "/",
		component: Home,
		name: "home",
		children: [
			{
				path: "soccer/team",
				component: () => import("@/views/soccer/SoccerTeam")
			},
			{
				path: "soccer/standing",
				component: () => import("@/views/soccer/SoccerStanding")
			},
			{
				path: "index",
				component: () => import("@/views/Index")
			}
		],
		redirect: "index"
	}
]
const router = createRouter({
	history: createWebHashHistory(),
	routes: constRoutes
})
export {constRoutes, router as default}