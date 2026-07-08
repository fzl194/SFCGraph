---
id: UDG@20.15.2@MMLCommand@SET FABRICMTU
type: MMLCommand
name: SET FABRICMTU（设置PAE内联口的MTU值）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: FABRICMTU
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- PAE 调测命令
- 配置
status: active
---

# SET FABRICMTU（设置PAE内联口的MTU值）

## 功能

该命令用来设置PAE内联口的MTU值。

Fabric口也称为内联口，用于网元内节点间的通信。此命令为用户提供修改Fabric口MTU值的能力。

MTU的大小决定了发送端一次能够发送报文的最大字节数。

## 注意事项

- 该命令仅适用于非NP卡场景、NP卡非加速模式场景，以及NP卡ECMP组网模式下的fabric平面。 其他场景执行不生效。
- 该命令执行后立即生效。

- 该命令不存在系统初始记录。
- 如果报文长度超过了接收端所能够承受的最大值，或者是超过了发送路径上途经的某台节点所能够承受的最大值，这样就会造成报文分片甚至丢弃，加重网络传输的负担。正确配置MTU值，是保证节点之间正常、高效通信的前提。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组;

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MTUVALUE | MTU值（byte） | 可选必选说明：必选参数<br>参数含义：该参数用于指定Fabric口最大传输单元。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为512～9600。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@FABRICMTU]] · PAE内联口MTU值（FABRICMTU）

## 使用实例

设置PAE内联口的MTU值为1800字节：

```
%%SET FABRICMTU: MTUVALUE=1800;%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-FABRICMTU.md`
