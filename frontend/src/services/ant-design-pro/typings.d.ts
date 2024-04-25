// @ts-ignore
/* eslint-disable */

declare namespace API {

  type CurrentUser = {
    user_profile: {
      username?: string;
      avatar?: string;
      access?: string;
    };
  };

  type LoginParams = {
    name?: string;
    password?: string;
  };
  
  type RegisterParams = {
    name?: string;
    password?: string;
  };

  type LoginResult = {
    data: {
      user_token: string;
    };
    detail?: string;
  };

  type RegisterResult = {
    detail?: string;
  };

  type UserList = {
    data?: UserListItem[];
    success?: boolean;
  };
}