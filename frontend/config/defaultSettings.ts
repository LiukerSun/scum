import { ProLayoutProps } from '@ant-design/pro-components';
/**
 * @name
 */
const Settings: ProLayoutProps & {
  pwa?: boolean;
  logo?: string;
} = {
  title: 'SCUM商城',
  navTheme: "light",
  colorPrimary: "#1890ff",
  layout: "top",
  contentWidth: "Fluid",
  fixedHeader: false,
  fixSiderbar: true,
  pwa: true,
  logo: "/logo.png",
  token: {},
  splitMenus: false
};

export default Settings;
