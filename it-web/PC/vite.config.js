import vue from "@vitejs/plugin-vue"
import AutoImport from "unplugin-auto-import/vite"
import path from "path"
import { ElementPlusResolver } from "unplugin-vue-components/resolvers"
import { defineConfig, loadEnv } from "vite"
import Components from "unplugin-vue-components/vite"

const config = defineConfig(({ mode, command }) => {
	const env = loadEnv(mode, process.cwd())
	const { VITE_APP_ENV, VITE_APP_BASE_URL, VITE_BASE_API } = env

	return {
		base: VITE_APP_ENV == "test" ? "./": "/",
		plugins: [
			vue(),
			AutoImport({resolvers: [ElementPlusResolver() ] }),
			Components({resolvers: [ElementPlusResolver() ] })
		],
		resolve: {
			extensions: [
				".js",
				".vue"
			],
			alias: {
				"@": path.resolve(__dirname, "./src")
			}
		},
		server: {
			port: 3030,
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