---
id: UNC@20.15.2@MMLCommand@RMV UEOVERLDCTRL
type: MMLCommand
name: RMV UEOVERLDCTRL（删除UE重载控制策略）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: UEOVERLDCTRL
command_category: 配置类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- UE重载控制管理
status: active
---

# RMV UEOVERLDCTRL（删除UE重载控制策略）

## 功能

**适用NF：AMF**

该命令用于为指定的用户（群）删除重载控制策略参数。

## 注意事项

该命令执行后下一次注册流程或签约变更流程生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于表示AMF上配置重载控制策略的用户范围。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_USER（所有用户）”：所有用户<br>- “HOME_USER（本网用户）”：本网用户<br>- “FOREIGN_USER（外网用户）”：外网用户<br>- “IMSI_PREFIX（IMSI前缀）”：指定IMSI前缀<br>默认值：无<br>配置原则：<br>对于指定的用户群，策略匹配的优先级从高到低依次为：“IMSI_PREFIX(IMSI前缀)”、“HOME_USER(本网用户)”或“FOREIGN_USER(外网用户)”、“ALL_USER(所有用户)”。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：该参数在"SUBRANGE"配置为"IMSI_PREFIX"时为条件必选参数。<br>参数含义：该参数用于指定应用重载控制策略的用户的IMSI前缀。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。 只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@UEOVERLDCTRL]] · UE重载控制策略（UEOVERLDCTRL）

## 使用实例

删除IMSI前缀为“123456”的用户的重载控制策略，执行如下命令：

```
RMV UEOVERLDCTRL:SUBRANGE=IMSI_PREFIX, IMSIPRE="123456";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-UEOVERLDCTRL.md`
