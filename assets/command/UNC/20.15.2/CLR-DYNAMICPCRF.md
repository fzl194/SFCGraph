---
id: UNC@20.15.2@MMLCommand@CLR DYNAMICPCRF
type: MMLCommand
name: CLR DYNAMICPCRF（清除动态PCRF）
nf: UNC
version: 20.15.2
verb: CLR
object_keyword: DYNAMICPCRF
command_category: 动作类
applicable_nf:
- PGW-C
- GGSN
effect_mode: 立即生效
is_dangerous: true
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- PCRF Diameter连接
- 动态PCRF
status: active
---

# CLR DYNAMICPCRF（清除动态PCRF）

## 功能

**适用NF：PGW-C、GGSN**

![](清除动态PCRF（CLR DYNAMICPCRF）_09897123.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，删除对端信息可能导致已在线用户发送CCR消息失败。

此命令用于删除动态PCRF主机列表表项。

## 注意事项

- 该命令执行后立即生效。
- 动态PCRF主机列表最多支持2000个表项。
- 删除动态PCRF会导致已在线用户无法按照之前的Destination-Host和Destination-Realm封装发送CCR消息。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HOSTNAME | PCRF主机名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示动态PCRF主机的主机名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～127。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DYNAMICPCRF]] · 动态PCRF（DYNAMICPCRF）

## 使用实例

删除所有动态PCRF主机列表：

```
CLR DYNAMICPCRF:;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/CLR-DYNAMICPCRF.md`
