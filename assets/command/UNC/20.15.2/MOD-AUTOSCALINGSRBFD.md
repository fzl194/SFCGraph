---
id: UNC@20.15.2@MMLCommand@MOD AUTOSCALINGSRBFD
type: MMLCommand
name: MOD AUTOSCALINGSRBFD（修改静态路由的动态BFD自动化配置模板）
nf: UNC
version: 20.15.2
verb: MOD
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

# MOD AUTOSCALINGSRBFD（修改静态路由的动态BFD自动化配置模板）

## 功能

该命令用于修改静态路由的动态BFD自动化配置模板。

## 注意事项

- 该命令执行后立即生效。
- 修改该BFD模板时，要保证该模板添加过。
- 该命令在自动化配置开关为关闭的状态下才能执行，请先使用SET AUTOCONFIG命令关闭自动配置开关；生效配置，需要再次使用SET AUTOCONFIG命令开启自动配置开关。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICENAME | 服务名称 | 可选必选说明：必选参数<br>参数含义：该参数用来表示接口自动化配置服务模板名称。要求和ADD AUTOSCALINGSERVICE命令中配置的SERVICENAME参数保持一致。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格和中文。<br>默认值：无 |
| MINRXINTERVAL | 最小接收间隔（ms） | 可选必选说明：可选参数<br>参数含义：该参数用于指定期望从对端接收BFD报文的最小接收间隔。如果未指定，采用全局缺省值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为30～1000。<br>默认值：无 |
| MINTXINTERVAL | 最小发送间隔（ms） | 可选必选说明：可选参数<br>参数含义：该参数用于指定向对端发送BFD报文的最小传输间隔。如果未指定，采用全局缺省值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为30～1000。<br>默认值：无 |
| MULTIPLIER | 检测倍数 | 可选必选说明：可选参数<br>参数含义：该参数用于指定本地检测倍数。如果未指定，采用全局缺省值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为3～50。<br>默认值：无 |

## 操作的配置对象

- [静态路由的动态BFD自动化配置模板（AUTOSCALINGSRBFD）](configobject/UNC/20.15.2/AUTOSCALINGSRBFD.md)

## 使用实例

修改一个静态路由的动态BFD自动化配置模板：

```
MOD AUTOSCALINGSRBFD:SERVICENAME="abc",MINRXINTERVAL=300,MINTXINTERVAL=300,MULTIPLIER=5;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改静态路由的动态BFD自动化配置模板（MOD-AUTOSCALINGSRBFD）_00840773.md`
