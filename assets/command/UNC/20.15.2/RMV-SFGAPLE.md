---
id: UNC@20.15.2@MMLCommand@RMV SFGAPLE
type: MMLCommand
name: RMV SFGAPLE（删除SFGAP本端实体）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SFGAPLE
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- N2接口管理
- SFGAP本端实体管理
status: active
---

# RMV SFGAPLE（删除SFGAP本端实体）

## 功能

![](删除SFGAP本端实体（RMV SFGAPLE）_75982872.assets/notice_3.0-zh-cn_2.png)

执行此命令，会导致SFG-RAN链路异常，影响感知gNodeB业务。

**适用NF：AMF**

在部署感知的场景下，通过RMV SFGAPLE删除SFGAP本端实体。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SFGAPLEIDX | SFGAP本端实体索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定SFGAP本端实体的索引，该索引作为SFGAP本端实体的唯一标识。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~1023。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [SFGAP本端实体（SFGAPLE）](configobject/UNC/20.15.2/SFGAPLE.md)

## 使用实例

删除本端实体标识为1的SFGAP本端实体，执行如下命令：

```
RMV SFGAPLE: SFGAPLEIDX=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除SFGAP本端实体（RMV-SFGAPLE）_75982872.md`
