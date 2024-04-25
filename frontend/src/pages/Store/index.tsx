import React from 'react'
import { PageContainer } from '@ant-design/pro-components';
import { Card, Col, Row, Menu } from 'antd';
import { AppstoreOutlined, MailOutlined, SettingOutlined } from '@ant-design/icons';

import type { MenuProps } from 'antd';

export default function Store() {

    const [selectedMenu, setSelectedMenu] = React.useState<string>('all_items')

    const iconMap: Record<string, React.ReactNode> = {
        MailOutlined: <MailOutlined />,
        AppstoreOutlined: <AppstoreOutlined />,
        SettingOutlined: <SettingOutlined />,
        // 添加其他图标的映射关系
    };
    function jsonToItems(jsonData: any[]): any[] {
        return jsonData.map(item => {
            const newItem = { ...item };
            if (item.icon && iconMap[item.icon]) {
                newItem.icon = iconMap[item.icon];
            }
            if (item.children) {
                newItem.children = jsonToItems(item.children);
            }
            return newItem;
        });
    }
    const menu_fetchData: any = {
        data: [
            {
                "label": "所有物品",
                "key": "all_items",
                "icon": "AppstoreOutlined"
            },
            {
                "label": "家具",
                "key": "家具",
                "icon": "SettingOutlined",
            },
            {
                "label": "近战武器",
                "key": "近战武器",
                "icon": "SettingOutlined",
            },
            {
                "label": "工具",
                "key": "工具",
                "icon": "SettingOutlined",
            },
            {
                "label": "食物调料",
                "key": "食物调料",
                "icon": "SettingOutlined",
            },
            {
                "label": "载具",
                "key": "载具",
                "icon": "SettingOutlined",
            },
            {
                "label": "套装",
                "type": "group",
                "children": [
                    {
                        "label": "套装1",
                        "key": "套装1"
                    },
                    {
                        "label": "套装2",
                        "key": "套装2"
                    }
                ]
            }
        ]
    }


    const items = jsonToItems(menu_fetchData.data)
    const onClick: MenuProps['onClick'] = (e) => {
        setSelectedMenu(e.key)
    };
    console.log("🚀 ~ selectedMenu:", selectedMenu)

    return (
        <PageContainer>
            <Row>

                <Col span={4} >
                    <Menu
                        onClick={onClick}
                        defaultSelectedKeys={['all_items']}
                        defaultOpenKeys={['sub1']}
                        mode="inline"
                        items={items}
                    />
                </Col>
                <Col span={19} style={{ paddingLeft: 16 }}>
                    <Row gutter={16}>
                        <Col span={8}>
                            <Card title="Card title" bordered={false}>
                                Card content
                            </Card>
                        </Col>
                        <Col span={8}>
                            <Card title="Card title" bordered={false}>
                                Card content
                            </Card>
                        </Col>
                        <Col span={8}>
                            <Card title="Card title" bordered={false}>
                                Card content
                            </Card>
                        </Col>
                    </Row>
                </Col>
            </Row>
        </PageContainer>
    )
}
