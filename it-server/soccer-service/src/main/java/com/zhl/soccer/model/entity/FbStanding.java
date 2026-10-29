package com.zhl.soccer.model.entity;

import lombok.Data;
import java.lang.Integer;
import java.lang.Long;
import java.lang.String;

@Data
public class FbStanding {

	private Long id;

	private Long teamId;

	private Long tournamentId;

	private String sourceId;

	private Integer matches;

	private Integer wins;

	private Integer draws;

	private Integer losses;

	private Integer goalsFor;

	private Integer goalsAgainst;

	private Integer goalDifference;

	private Integer points;

}