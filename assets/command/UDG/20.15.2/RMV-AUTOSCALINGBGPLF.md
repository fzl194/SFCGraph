---
id: UDG@20.15.2@MMLCommand@RMV AUTOSCALINGBGPLF
type: MMLCommand
name: RMV AUTOSCALINGBGPLF（删除BGP入不转板自动化配置模板）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: AUTOSCALINGBGPLF
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 自动部署
- BGP入不转板自动化配置
status: active
---

# RMV AUTOSCALINGBGPLF（删除BGP入不转板自动化配置模板）

## 功能

该命令用于删除BGP入不转板自动化配置模板。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 策略名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定BGP入不转板策略名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格和中文。<br>默认值：无 |
| SERVICENAME | 服务名称 | 可选必选说明：必选参数<br>参数含义：该参数用来表示接口自动化配置服务模板名称。该参数由ADD AUTOSCALINGSERVICE命令配置获得。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格和中文。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@AUTOSCALINGBGPLF]] · BGP入不转板自动化配置模板（AUTOSCALINGBGPLF）

## 使用实例

删除一个BGP入不转板自动化配置模板：

```
RMV AUTOSCALINGBGPLF:POLICYNAME="bgppolicy",SERVICENAME="s1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-AUTOSCALINGBGPLF.md`
