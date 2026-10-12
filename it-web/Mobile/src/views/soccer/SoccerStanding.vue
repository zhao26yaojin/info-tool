<template>
	<div>
		<u-form :model="standingStandingQuery">
		</u-form>
		<u-button @click="onGetStandingStandingList">Query</u-button>
		<u-form ::model="standingStandingList">
			<u-form-item label="id" prop="id">
				<u-input v-model="id">
				</u-input>
			</u-form-item>
			<u-form-item label="id" prop="teamId">
				<u-input v-model="teamId">
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
			<u-form-item label="名称" prop="name">
				<u-input v-model="name">
				</u-input>
			</u-form-item>
		</u-form>
	</div>
</template>
<script setup>
import { onLoad } from "@dcloudio/uni-app"
import { getStandingList as getStandingStandingList } from "@/api/fb/standing"
import { reactive } from "vue"

const standingStandingQuery = reactive({})
const standingStandingList = reactive([])
const onGetStandingStandingList = () => {
	const { result } = getStandingStandingList(standingStandingQuery)

	standingStandingList.splice(0, standingStandingList.length)

	if (result && result.length > 0) {
		standingStandingList.push({spread: result})
	}

}
onLoad(() => onGetStandingStandingList())

</script>
<style scoped>

</style>
