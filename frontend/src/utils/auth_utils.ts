export interface IAuthUser {
  username: string;
  password: string;
  is_loaded: boolean;
}

export interface IRegisterUser extends IAuthUser {}
export interface ILoginUser extends IAuthUser {}
