import uni from "@dcloudio/vite-plugin-uni"
import { defineConfig, loadEnv } from "vite"

const config = defineConfig(({ mode, command }) => {
	const env = loadEnv(mode, process.cwd())
	const { VITE_APP_ENV, VITE_APP_BASE_URL, VITE_BASE_API } = env

	return {
		base: VITE_APP_ENV == "test" ? "./": "/",
		plugins: [uni() ],
		server: {
			port: 3031,
			proxy: {
				[VITE_BASE_API]: {
					target: `${VITE_APP_BASE_URL}`,
					rewrite: path => path.replace(new RegExp("^" + VITE_BASE_API), "")
				}
			}
		}
	}
})
export default config