---
id: UNC@20.15.2@MMLCommand@ADD LDPFECLIST
type: MMLCommand
name: ADD LDPFECLIST（添加FEC列表）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: LDPFECLIST
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- MPLS管理
- LDP管理
- LDP FEC列表
status: active
---

# ADD LDPFECLIST（添加FEC列表）

## 功能

该命令用于添加FEC列表。FEC列表是多个FEC节点地址的集合，用于指导动态BFD会话的建立。以FEC列表方式触发建立BFD会话能够精确控制对哪些LDP Tunnel进行检测，从而一定程度上控制网络的开销。采用此方式，首先要建立一个FEC列表，并向列表中添加相应的FEC节点，然后配置BFD引用此列表即可。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 配置该命令前，需要通过SET MPLSSITE全局使能MPLS能力。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FECLISTNAME | FEC列表名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定FEC列表的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：只能配置一个FEC列表。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@LDPFECLIST]] · FEC列表（LDPFECLIST）

## 使用实例

添加FEC列表：

```
ADD LDPFECLIST:FECLISTNAME="name1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-LDPFECLIST.md`
