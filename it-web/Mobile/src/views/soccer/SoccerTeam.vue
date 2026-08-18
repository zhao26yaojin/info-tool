<template>
	<div>
		<u-form :model="fbTeamFbTeamQuery">
		</u-form>
		<u-button @click="onGetFbTeamFbTeamList">Query</u-button>
		<u-form ::model="fbTeamFbTeamList">
			<u-form-item label="id" prop="id">
				<u-input v-model="id">
				</u-input>
			</u-form-item>
			<u-form-item label="名称" prop="name">
				<u-input v-model="name">
				</u-input>
			</u-form-item>
			<u-form-item label="id" prop="country_id">
				<u-input v-model="country_id">
				</u-input>
			</u-form-item>
		</u-form>
	</div>
</template>
<script setup>
import { onLoad } from "@dcloudio/uni-app"
import { getFbTeamList as getFbTeamFbTeamList } from "@/api/sp/fbTeam"
import { reactive } from "vue"

const fbTeamFbTeamQuery = reactive({})
const fbTeamFbTeamList = reactive([])
const onGetFbTeamFbTeamList = () => {
	const { result } = getFbTeamFbTeamList(fbTeamFbTeamQuery)

	fbTeamFbTeamList.splice(0, fbTeamFbTeamList.length)

	if (result && result.length > 0) {
		fbTeamFbTeamList.push({spread: result})
	}

}
onLoad(() => onGetFbTeamFbTeamList())

</script>
<style scoped>

</style>
