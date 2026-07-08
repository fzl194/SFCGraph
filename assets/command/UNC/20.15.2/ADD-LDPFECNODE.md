---
id: UNC@20.15.2@MMLCommand@ADD LDPFECNODE
type: MMLCommand
name: ADD LDPFECNODE（添加FEC节点）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: LDPFECNODE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 1000
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- MPLS管理
- LDP管理
- LDP FEC节点
status: active
---

# ADD LDPFECNODE（添加FEC节点）

## 功能

该命令用于向FEC列表中添加FEC节点。FEC列表是多个FEC节点地址的集合，用于指导动态BFD会话的建立。以FEC列表方式触发建立BFD会话能够精确控制对哪些LDP Tunnel进行检测，从而一定程度上控制网络的开销。采用此方式，首先要建立一个FEC列表，并向列表中添加相应的FEC节点，然后配置BFD引用此列表即可。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1000。
- 配置该命令前，需要通过ADD LDPFECLIST添加FEC列表。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FECLISTNAME | FEC列表名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定FEC列表的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：通过LST LDPFECLIST查看当前已存在的FEC列表。 |
| IPADDRESS | IP地址 | 可选必选说明：必选参数<br>参数含义：该参数用于指定FEC的IP地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |

## 操作的配置对象

- [FEC节点（LDPFECNODE）](configobject/UNC/20.15.2/LDPFECNODE.md)

## 使用实例

添加FEC节点：

```
ADD LDPFECNODE:FECLISTNAME="name1",IPADDRESS="192.168.1.1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/添加FEC节点（ADD-LDPFECNODE）_50281126.md`
