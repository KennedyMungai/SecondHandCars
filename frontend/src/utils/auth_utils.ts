export interface IAuthUser {
  email: string;
  password: string;
}

export interface IRegisterUser extends IAuthUser {}
export interface ILoginUser extends IAuthUser {}
