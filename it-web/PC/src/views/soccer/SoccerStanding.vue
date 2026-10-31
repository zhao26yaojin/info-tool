<template>
	<div class="frame">
		<el-form :inline="true" :model="standingQuery" class="form-inline">
			<el-form-item label="id">
				<el-select v-model="standingQuery.tournamentId" placeholder="tournamentId" clearable style="width: 160px">
					<el-option v-for="item in tournamentList" :key="item.id" :label="item.name" :value="item.id">
					</el-option>
				</el-select>
			</el-form-item>
			<el-form-item>
				<el-button type="primary" @click="onGetStandingList">Query</el-button>
			</el-form-item>
		</el-form>
		<el-table :data="standingList" border>
			<el-table-column prop="teamLogo" label="图标">
				<template #default="{ row }">
					<el-image v-if="row.teamLogo" :src="imgUrl(row.teamLogo)" fit="contain" style="width: 24px; height: 24px" lazy>
					</el-image>
				</template>
			</el-table-column>
			<el-table-column prop="teamName" label="名称">
			</el-table-column>
			<el-table-column prop="matches" label="场次">
			</el-table-column>
			<el-table-column prop="wins" label="胜">
			</el-table-column>
			<el-table-column prop="draws" label="平">
			</el-table-column>
			<el-table-column prop="losses" label="负">
			</el-table-column>
			<el-table-column prop="goalsFor" label="进球">
			</el-table-column>
			<el-table-column prop="goalsAgainst" label="失球">
			</el-table-column>
			<el-table-column prop="goalDifference" label="净胜球">
			</el-table-column>
			<el-table-column prop="points" label="积分">
			</el-table-column>
		</el-table>
	</div>
</template>
<script setup>
import { imgUrl } from "@/utils/image"
import { getList as getStandingList } from "@/api/fb/standing"
import { getList as getTournamentList } from "@/api/fb/tournament"
import { onMounted, reactive } from "vue"

const tournamentList = reactive([])
const onGetTournamentList = async () => {
	const { result } = await getTournamentList()

	tournamentList.splice(0, tournamentList.length)

	if (result && result.length > 0) {
		tournamentList.push(...result)
	}

}
const standingQuery = reactive({tournamentId: ''})
const standingList = reactive([])
const onGetStandingList = async () => {
	const { result } = await getStandingList(standingQuery)

	standingList.splice(0, standingList.length)

	if (result && result.length > 0) {
		standingList.push(...result)
	}

}
onMounted(() => {
	onGetStandingList()

	onGetTournamentList()
})

</script>
<style scoped>
.frame {
	width: 800px;
	margin: auto;
	padding-top: 30px;
}

.form-inline {
}


</style>
