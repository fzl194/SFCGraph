---
id: UNC@20.15.2@MMLCommand@ADD AUTOSCALINGMPLS
type: MMLCommand
name: ADD AUTOSCALINGMPLS（增加MPLS自动化配置模板）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: AUTOSCALINGMPLS
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 4096
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 自动部署
- MPLS自动化配置
status: active
---

# ADD AUTOSCALINGMPLS（增加MPLS自动化配置模板）

## 功能

该命令用于添加MPLS自动化配置模板。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为4096。
- 使用此命令前必须先要使用SET MPLSSITE命令全局使能MPLS功能。
- 该命令在自动化配置开关为关闭的状态下才能执行，请先使用SET AUTOCONFIG命令关闭自动配置开关；若要使配置生效，需要再次使用SET AUTOCONFIG命令开启自动配置开关。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICENAME | 服务名称 | 可选必选说明：必选参数<br>参数含义：该参数用来表示接口自动化配置服务模板名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格和中文。<br>默认值：无<br>配置原则：该参数要求和ADD AUTOSCALINGSERVICE命令中配置的SERVICENAME参数保持一致。可通过LST AUTOSCALINGSERVICE命令查询获取。 |
| MTU | 最大传输单元 | 可选必选说明：可选参数<br>参数含义：该参数用于指定MPLS接口最大传输单元。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为46～9600。<br>默认值：无<br>配置原则：如果不输入该参数，则实际生效配置为接口的MTU。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/AUTOSCALINGMPLS]] · MPLS自动化配置模板（AUTOSCALINGMPLS）

## 使用实例

增加一个MPLS自动化配置模板：

```
ADD AUTOSCALINGMPLS:SERVICENAME="s1", MTU=1500;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-AUTOSCALINGMPLS.md`
