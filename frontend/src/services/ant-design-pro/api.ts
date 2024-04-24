// @ts-ignore
/* eslint-disable */
import { request } from '@umijs/max';

/** 获取当前的用户 GET /api/currentUser */
export async function currentUser(options?: { [key: string]: any }) {
  return request<{ data: API.CurrentUser; }>('/account/auth', {
    method: 'GET',
    ...(options || {}),
  });
}

/** 登录接口 POST user/login */
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


/** 获取用户列表 GET /api/rule */
export async function listUsers(
  params: {
    // query
    pageSize?: number;
    current?: number;
  },
  options?: { [key: string]: any },
) {
  return request<API.UserList>('/user/list', {
    method: 'GET',
    params: {
      ...params,
    },
    ...(options || {}),
  });
}


