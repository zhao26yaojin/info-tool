package com.zhl.soccer.model.qo;

import lombok.Data;
import java.lang.Long;
import java.lang.String;

@Data
public class TeamTeamQo {

	private Long id;

	private String name;

	private Long tournamentId;

}