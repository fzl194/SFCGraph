---
id: UNC@20.15.2@MMLCommand@MOD CPNODE
type: MMLCommand
name: MOD CPNODE（修改CP节点信息）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: CPNODE
command_category: 配置类
applicable_nf:
- SMF
- PGW-C
- SGW-C
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- PFCP接口管理
- CP管理
- CP节点管理
status: active
---

# MOD CPNODE（修改CP节点信息）

## 功能

**适用NF：SMF、PGW-C、SGW-C、GGSN**

该命令用于修改一个CP节点即控制面节点的功能。 CP节点的IP地址不允许修改，如果需要修改，请先执行删除CP节点，再重新添加。

## 注意事项

- 该命令执行后立即生效。

- 在执行此命令前必须先执行过ADD CPNODE命令。修改CP节点可能会造成CP节点和UP节点的连接短暂性断开，因为UP节点不能及时的感知CP节点修改后的信息。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CPNODEINDEX | CP节点索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定CP节点索引。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0。<br>默认值：无<br>配置原则：无 |
| CPFUNCTION | CP节点功能 | 可选必选说明：可选参数<br>参数含义：该参数用于指定CP节点功能。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~65535。其中有效取值范围为0~255。<br>默认值：无<br>配置原则：<br>当前产品暂未实现协议定义的负载控制等相关功能，建议配置为0即可。<br>如果通过MOD CPNODE修改该参数取值，对产品功能无影响，但是会触发N4偶联的更新，可以在测试偶联链路更新场景下使用。 |

## 操作的配置对象

- [CP节点信息（CPNODE）](configobject/UNC/20.15.2/CPNODE.md)

## 使用实例

将索引为0的CP节点CPFUNCTION的值从0修改为1，从而触发N4偶联更新流程，执行如下命令：

```
MOD CPNODE: CPNODEINDEX=0, CPFUNCTION=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改CP节点信息（MOD-CPNODE）_09654361.md`
