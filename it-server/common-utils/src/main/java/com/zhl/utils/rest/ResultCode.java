package com.zhl.utils.rest;

import lombok.AllArgsConstructor;
import java.lang.String;

@AllArgsConstructor
public enum ResultCode {

	SUCCESS(200, "执行成功"),

	ERROR(500, "内部异常");

	private int code;

	private String message;

	public int getCode(){
		return this.code;
	}

	public String getMessage(){
		return this.message;
	}

}