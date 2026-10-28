package com.zhl.soccer.model.entity;

import lombok.Data;
import java.lang.Long;
import java.lang.String;

@Data
public class FbTournament {

	private Long id;

	private String name;

	private String sourceId;

	private String logo;

}