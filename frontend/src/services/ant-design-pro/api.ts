// @ts-ignore
/* eslint-disable */
import { request } from '@umijs/max';

/** 获取当前的用户 GET /account/auth */
export async function currentUser(options?: { [key: string]: any }) {
  return request<{ data: API.CurrentUser; }>('/account/auth', {
    method: 'GET',
    ...(options || {}),
  });
}

/** 登录接口 POST /account/auth */
export async function login(body: API.LoginParams, options?: { [key: string]: any }) {
  return request<API.LoginResult>('/account/auth', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    data: body,
    ...(options || {}),
  });
}

/** 注册接口 PUT /account/auth */
export async function register(body: API.LoginParams, options?: { [key: string]: any }) {
  return request<API.LoginResult>('/account/auth', {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    data: body,
    ...(options || {}),
  });
}