<template>
	<div>
		<u-form :model="standingQuery">
		</u-form>
		<u-button @click="onGetStandingList">Query</u-button>
		<u-form ::model="standingList">
			<u-form-item label="id" prop="id">
				<u-input v-model="id">
				</u-input>
			</u-form-item>
			<u-form-item label="图标" prop="teamLogo">
				<u-input v-model="teamLogo">
				</u-input>
			</u-form-item>
			<u-form-item label="名称" prop="teamName">
				<u-input v-model="teamName">
				</u-input>
			</u-form-item>
			<u-form-item label="id" prop="tournamentId">
				<u-input v-model="tournamentId">
				</u-input>
			</u-form-item>
			<u-form-item label="爬虫源数据id（去重用）" prop="sourceId">
				<u-input v-model="sourceId">
				</u-input>
			</u-form-item>
			<u-form-item label="场次" prop="matches">
				<u-input v-model="matches">
				</u-input>
			</u-form-item>
			<u-form-item label="胜" prop="wins">
				<u-input v-model="wins">
				</u-input>
			</u-form-item>
			<u-form-item label="平" prop="draws">
				<u-input v-model="draws">
				</u-input>
			</u-form-item>
			<u-form-item label="负" prop="losses">
				<u-input v-model="losses">
				</u-input>
			</u-form-item>
			<u-form-item label="进球" prop="goalsFor">
				<u-input v-model="goalsFor">
				</u-input>
			</u-form-item>
			<u-form-item label="失球" prop="goalsAgainst">
				<u-input v-model="goalsAgainst">
				</u-input>
			</u-form-item>
			<u-form-item label="净胜球" prop="goalDifference">
				<u-input v-model="goalDifference">
				</u-input>
			</u-form-item>
			<u-form-item label="积分" prop="points">
				<u-input v-model="points">
				</u-input>
			</u-form-item>
		</u-form>
	</div>
</template>
<script setup>
import { onLoad } from "@dcloudio/uni-app"
import { getList as getStandingList } from "@/api/fb/standing"
import { reactive } from "vue"

const standingQuery = reactive({})
const standingList = reactive([])
const onGetStandingList = () => {
	const { result } = getStandingList(standingQuery)

	standingList.splice(0, standingList.length)

	if (result && result.length > 0) {
		standingList.push({spread: result})
	}

}
onLoad(() => onGetStandingList())

</script>
<style scoped>

</style>
