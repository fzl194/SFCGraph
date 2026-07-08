---
id: UDG@20.15.2@MMLCommand@RMV CPNODEID
type: MMLCommand
name: RMV CPNODEID（删除SMF的NodeID）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: CPNODEID
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 对新用户生效
is_dangerous: true
category_path:
- 用户面服务管理
- 会话管理
- 会话地址管理
- SMF属性
status: active
---

# RMV CPNODEID（删除SMF的NodeID）

## 功能

**适用NF：PGW-U、UPF**

![](删除SMF的NodeID（RMV CPNODEID）_16780317.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，如果当前CPNODEID与相应的地址池组存在绑定关系，即通过PoolGrpMap命令与相应地址池组绑定，删除CPNODEID时对应关联的PoolGrpMap会被连带删除。

该命令用于删除指定SMF实例信息。

## 注意事项

- 该命令执行后只对新激活用户生效。
- 删除指定SMF实例时会同时删除关联的PoolGrpMap实例。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CPNAME | SMF名称 | 可选必选说明：必选参数<br>参数含义：SMF的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～255。由“_”、“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@CPNODEID]] · SMF的NodeID（CPNODEID）

## 使用实例

删除名为smfnode1的SMF实例：

```
RMV CPNODEID: CPNAME="smfnode1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-CPNODEID.md`
