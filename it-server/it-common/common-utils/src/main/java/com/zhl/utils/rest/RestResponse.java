package com.zhl.utils.rest;

import lombok.Data;
import java.lang.Long;
import java.io.Serializable;
import java.lang.String;

@Data
public class RestResponse<T> implements Serializable {

	private static final Long serialVersionUID = 1L;

	private int code;

	private String message;

	private T result;

	public static <T> RestResponse<T> ok(T result){
		return new RestResponse<T>(ResultCode.SUCCESS, result);
	}

	RestResponse(ResultCode resultCode, T result){
		this.result = result;

		this.code = resultCode.getCode();

		this.message = resultCode.getMessage();
	}

}