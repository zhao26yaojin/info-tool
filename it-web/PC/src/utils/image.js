const IMGPROXY_BASE_URL = import.meta.env.VITE_IMGPROXY_BASE_URL

// 将库中存储的 s3://bucket/key 引用转换为 imgproxy 缩略图 URL
// 固定尺寸, 所有设备共用同一个 URL 以提高缓存命中; 页面上按需用 CSS 缩小显示
export const imgUrl = (ref, size = 48) => {
	if (!ref) return ''
	return `${IMGPROXY_BASE_URL}/insecure/rs:fit:${size}:${size}/plain/${ref}@png`
}
