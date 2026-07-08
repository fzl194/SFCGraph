---
id: UNC@20.15.2@MMLCommand@RMV AUTOSCALINGSRBFD
type: MMLCommand
name: RMV AUTOSCALINGSRBFD（删除静态路由的动态BFD自动化配置模板）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: AUTOSCALINGSRBFD
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 自动部署
- 静态路由的动态BFD自动化配置
status: active
---

# RMV AUTOSCALINGSRBFD（删除静态路由的动态BFD自动化配置模板）

## 功能

该命令用于删除静态路由的动态BFD自动化配置模板。

## 注意事项

- 该命令执行后立即生效。
- 删除该BFD模板时，要保证该模板添加过，且没有被引用。
- 该命令在自动配置开关为关闭的状态下才能执行，请先使用SET AUTOCONFIG命令关闭自动配置开关。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICENAME | 服务名称 | 可选必选说明：必选参数<br>参数含义：该参数用来表示接口自动化配置服务模板名称。要求和ADD AUTOSCALINGSERVICE命令中配置的SERVICENAME参数保持一致。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格和中文。<br>默认值：无 |
| IPVERSION | 地址族 | 可选必选说明：可选参数<br>参数含义：该参数用来表示IP地址类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPv4：IPv4地址族。<br>- IPv6：IPv6地址族。<br>默认值：无 |

## 操作的配置对象

- [静态路由的动态BFD自动化配置模板（AUTOSCALINGSRBFD）](configobject/UNC/20.15.2/AUTOSCALINGSRBFD.md)

## 使用实例

删除一个静态路由的动态BFD自动化配置模板：

```
RMV AUTOSCALINGSRBFD:SERVICENAME="abc";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除静态路由的动态BFD自动化配置模板（RMV-AUTOSCALINGSRBFD）_49801674.md`
