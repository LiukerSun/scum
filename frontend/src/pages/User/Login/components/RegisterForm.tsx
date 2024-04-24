import React from 'react';
import ProForm, {
    ProFormText,
    ProFormCheckbox,
} from '@ant-design/pro-form';
import { message } from 'antd';

const RegisterForm = () => {
    const handleSubmit = async (values: any) => {
        // Here you would usually send the form values to the server
        console.log(values);
        message.success('注册成功');
    };

    return (
        <ProForm
            onFinish={handleSubmit}
        >
            <ProFormText
                name="username"
                label="用户名"
                placeholder="请输入用户名"
                rules={[
                    {
                        required: true,
                        message: '请输入用户名!',
                    },
                ]}
            />
            <ProFormText.Password
                name="password"
                label="密码"
                placeholder="请输入密码"
                rules={[
                    {
                        required: true,
                        message: '请输入密码!',
                    },
                ]}
            />
            <ProFormText.Password
                name="confirm"
                label="确认密码"
                placeholder="请再次输入密码"
                dependencies={['password']}
                rules={[
                    {
                        required: true,
                        message: '请确认密码!',
                    },
                    ({ getFieldValue }) => ({
                        validator(_, value) {
                            if (!value || getFieldValue('password') === value) {
                                return Promise.resolve();
                            }
                            return Promise.reject(new Error('两次输入的密码不匹配!'));
                        },
                    }),
                ]}
            />
            <ProFormCheckbox
                name="agreement"
                rules={[
                    {
                        validator: (_, value) =>
                            value ? Promise.resolve() : Promise.reject(new Error('必须同意协议才能注册')),
                    },
                ]}
            >
                我已阅读并同意<a href="#agreement">《用户协议》</a>
            </ProFormCheckbox>
            <ProForm.Item>
                <button type="submit">
                    注册
                </button>
            </ProForm.Item>
        </ProForm>
    );
};

export default RegisterForm;