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
		<el-table :data="standingList" :border="false">
			<el-table-column align="center" type="index" width="50">
			</el-table-column>
			<el-table-column label="球队" align="center" min-width="120px">
				<template #default="{ row }">
					<div style="display: flex; align-items: center; justify-content: center">
						<span style="display: flex">
							<el-image v-if="row.teamLogo" :src="imgUrl(row.teamLogo)" fit="contain" style="width: 24px; height: 24px" lazy>
							</el-image>
						</span>
						<span style="margin-left: 8px">{{ row.teamName }}</span>
					</div>
				</template>
			</el-table-column>
			<el-table-column prop="matches" label="场次" min-width="60px" align="center">
			</el-table-column>
			<el-table-column prop="wins" label="胜" min-width="60px" align="center">
			</el-table-column>
			<el-table-column prop="draws" label="平" min-width="60px" align="center">
			</el-table-column>
			<el-table-column prop="losses" label="负" min-width="60px" align="center">
			</el-table-column>
			<el-table-column prop="goalsFor" label="进球" min-width="60px" align="center">
			</el-table-column>
			<el-table-column prop="goalsAgainst" label="失球" min-width="60px" align="center">
			</el-table-column>
			<el-table-column prop="goalDifference" label="净胜球" min-width="60px" align="center">
			</el-table-column>
			<el-table-column prop="points" label="积分" min-width="60px" align="center">
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
	onGetTournamentList()

	onGetStandingList()
})

</script>
<style scoped>
.frame {
	width: 800px;
	margin: auto;
	padding-top: 30px;
	padding-bottom: 30px;
}

.form-inline {
}


</style>
