---
id: UDG@20.15.2@MMLCommand@RMV AUTOSCALINGMPLS
type: MMLCommand
name: RMV AUTOSCALINGMPLS（删除MPLS自动化配置模板）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: AUTOSCALINGMPLS
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 自动部署
- MPLS自动化配置
status: active
---

# RMV AUTOSCALINGMPLS（删除MPLS自动化配置模板）

## 功能

该命令用于删除MPLS自动化配置模板。

## 注意事项

- 该命令执行后立即生效。
- 删除该模板时，要保证该模板添加过。
- 该命令在自动化配置开关为关闭的状态下才能执行，请先使用SET AUTOCONFIG命令关闭自动配置开关。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICENAME | 服务名称 | 可选必选说明：必选参数<br>参数含义：该参数用来表示接口自动化配置服务模板名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格和中文。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/AUTOSCALINGMPLS]] · MPLS自动化配置模板（AUTOSCALINGMPLS）

## 使用实例

删除一个MPLS自动化配置模板：

```
RMV AUTOSCALINGMPLS:SERVICENAME="s1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除MPLS自动化配置模板（RMV-AUTOSCALINGMPLS）_00600929.md`
