import Footer from '@/components/Footer';
import { register } from '@/services/ant-design-pro/api'; // 修改这里导入的注册接口
import {
    LockOutlined,
    UserOutlined,
} from '@ant-design/icons';
import {
    LoginForm, // 修改为 RegisterForm
    ProFormCheckbox,
    ProFormText,
} from '@ant-design/pro-components';
import { useEmotionCss } from '@ant-design/use-emotion-css';
import { FormattedMessage, history, SelectLang, useIntl, useModel, Helmet } from '@umijs/max';
import { Alert, message } from 'antd';
import Settings from '../../../../config/defaultSettings';
import React, { useState } from 'react';
import { flushSync } from 'react-dom';
import logo from "@/assets/images/logo.png";

const Lang = () => {
    const langClassName = useEmotionCss(({ token }) => {
        return {
            width: 42,
            height: 42,
            lineHeight: '42px',
            position: 'fixed',
            right: 16,
            borderRadius: token.borderRadius,
            ':hover': {
                backgroundColor: token.colorBgTextHover,
            },
        };
    });

    return (
        <div className={langClassName} data-lang>
            {SelectLang && <SelectLang />}
        </div>
    );
};

const LoginMessage: React.FC<{
    content: string;
}> = ({ content }) => {
    return (
        <Alert
            style={{
                marginBottom: 24,
            }}
            message={content}
            type="error"
            showIcon
        />
    );
};

const Register: React.FC = () => {
    const [userRegisterState, setUserRegisterState] = useState<API.RegisterResult>({ // 修改状态变量名称
        detail: ""
    });
    const { initialState, setInitialState } = useModel('@@initialState');
    const containerClassName = useEmotionCss(() => {
        return {
            display: 'flex',
            flexDirection: 'column',
            height: '100vh',
            overflow: 'auto',
            backgroundImage:
                "url('https://mdn.alipayobjects.com/yuyan_qk0oxh/afts/img/V-_oS6r-i7wAAAAAAAAAAAAAFl94AQBr')",
            backgroundSize: '100% 100%',
        };
    });

    const intl = useIntl();

    const fetchUserInfo = async () => {
        const userInfo = await initialState?.fetchUserInfo?.();
        if (userInfo) {
            flushSync(() => {
                setInitialState((s) => ({
                    ...s,
                    currentUser: userInfo,
                }));
            });
        }
    };

    const handleSubmit = async (values: API.RegisterParams) => { // 修改参数类型和函数名称
        try {
            // 注册，调用注册接口
            const msg = await register({ ...values }); // 修改为调用注册接口
            if (msg.detail === "请求成功") {
                const defaultRegisterSuccessMessage = intl.formatMessage({ // 修改提示消息
                    id: 'pages.register.success',
                    defaultMessage: '注册成功！',
                });
                message.success(defaultRegisterSuccessMessage);
                await fetchUserInfo();
                const urlParams = new URL(window.location.href).searchParams;
                history.push(urlParams.get('redirect') || '/');
                return;
            }
            console.log(msg);
            // 如果失败去设置用户错误信息
            setUserRegisterState(msg); // 修改状态变量名称
        } catch (error) {
            const defaultRegisterFailureMessage = intl.formatMessage({ // 修改提示消息
                id: 'pages.register.accountRegister.errorMessage',
                defaultMessage: '注册失败，请重试！',
            });
            console.log(error);
            message.error(defaultRegisterFailureMessage);
        }
    };
    const { detail } = userRegisterState; // 修改状态变量名称

    return (
        <div className={containerClassName}>
            <Helmet>
                <title>
                    {intl.formatMessage({
                        id: 'menu.register',
                        defaultMessage: '注册页', // 修改标题
                    })}
                    - {Settings.title}
                </title>
            </Helmet>
            <Lang />
            <div
                style={{
                    flex: '1',
                    padding: '32px 0',
                }}
            >
                <LoginForm // 修改为 RegisterForm
                    contentStyle={{
                        minWidth: 280,
                        maxWidth: '75vw',
                    }}
                    logo={<img alt="logo" src={logo} />}
                    title="Scum商城系统" // 修改标题
                    subTitle={intl.formatMessage({ id: 'pages.layouts.userLayout.title' })} // 修改副标题
                    initialValues={{
                        autoLogin: true,
                    }}
                    onFinish={async (values) => {
                        await handleSubmit(values as API.RegisterParams); // 修改参数类型
                    }}
                >

                    {detail === 'error' && (
                        <LoginMessage
                            content={intl.formatMessage({
                                id: 'pages.register.accountRegister.errorMessage', // 修改错误提示消息
                                defaultMessage: '账户注册失败！',
                            })}
                        />
                    )}

                    <>
                        <ProFormText
                            name="username"
                            fieldProps={{
                                size: 'large',
                                prefix: <UserOutlined />,
                            }}
                            placeholder={intl.formatMessage({
                                id: 'pages.register.username.placeholder', // 修改占位符文本
                                defaultMessage: '用户名: admin or user',
                            })}
                            rules={[
                                {
                                    required: true,
                                    message: (
                                        <FormattedMessage
                                            id="pages.register.username.required" // 修改错误消息
                                            defaultMessage="请输入用户名!"
                                        />
                                    ),
                                },
                            ]}
                        />
                        <ProFormText.Password
                            name="password"
                            fieldProps={{
                                size: 'large',
                                prefix: <LockOutlined />,
                            }}
                            placeholder={intl.formatMessage({
                                id: 'pages.register.password.placeholder', // 修改占位符文本
                                defaultMessage: '密码: ant.design',
                            })}
                            rules={[
                                {
                                    required: true,
                                    message: (
                                        <FormattedMessage
                                            id="pages.register.password.required" // 修改错误消息
                                            defaultMessage="请输入密码！"
                                        />
                                    ),
                                },
                            ]}
                        />
                    </>
                    <div
                        style={{
                            marginBlockEnd: 24,
                        }}
                    >
                        <ProFormCheckbox noStyle name="autoLogin">
                            自动登录
                        </ProFormCheckbox>
                        <a
                            href='/user/login' // 修改链接为登录页面
                            style={{
                                float: 'right',
                            }}
                        >
                            返回登录
                        </a>
                    </div>
                </LoginForm>
            </div>
            <Footer />
        </div>
    );
};

export default Register;
