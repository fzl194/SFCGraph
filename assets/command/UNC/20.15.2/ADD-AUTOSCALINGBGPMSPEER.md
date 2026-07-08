---
id: UNC@20.15.2@MMLCommand@ADD AUTOSCALINGBGPMSPEER
type: MMLCommand
name: ADD AUTOSCALINGBGPMSPEER（增加BGP自动化多源邻居配置模板）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: AUTOSCALINGBGPMSPEER
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 4096
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 自动部署
- BGP多源peer自动化配置
status: active
---

# ADD AUTOSCALINGBGPMSPEER（增加BGP自动化多源邻居配置模板）

## 功能

该命令用于添加BGP多源peer自动化配置模板，在扩容场景下使用BGP多源peer自动化配置模板可以自动化产生BGP多源peer的配置，可以减少人工手动配置，提升配置效率。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为4096。
- 依赖参数SERVICENAME值相同的ADD AUTOSCALINGSERVICE已经配置。
- 该命令在自动化配置开关为关闭的状态下才能执行，请先使用SET AUTOCONFIG命令关闭自动配置开关；生效配置，需要再次使用SET AUTOCONFIG命令开启自动配置开关。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICENAME | 服务名称 | 可选必选说明：必选参数<br>参数含义：该参数用来表示接口自动化配置服务模板名称。要求和ADD AUTOSCALINGSERVICE命令中配置的SERVICENAME参数保持一致。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格。<br>默认值：无 |
| IPVERSION | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用来指定peer的地址族信息。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPv4：IPv4地址族。<br>默认值：无 |
| PEER4 | 对等体地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPv4”时为必选参数。<br>参数含义：该参数用于指定用所连接对等体的接口地址。要求和ADD BGPPEER命令中的PEERADDR参数保持一致。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@AUTOSCALINGBGPMSPEER]] · BGP自动化多源邻居配置模板（AUTOSCALINGBGPMSPEER）

## 使用实例

添加一个BGP多源peer自动化配置模板：

```
ADD AUTOSCALINGBGPMSPEER:SERVICENAME="service1",IPVERSION=IPv4,PEER4="10.1.1.1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-AUTOSCALINGBGPMSPEER.md`
