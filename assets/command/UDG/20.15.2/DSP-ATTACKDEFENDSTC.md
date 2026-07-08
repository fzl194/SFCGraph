---
id: UDG@20.15.2@MMLCommand@DSP ATTACKDEFENDSTC
type: MMLCommand
name: DSP ATTACKDEFENDSTC（显示攻击防范统计信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: ATTACKDEFENDSTC
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP安全管理
- 攻击防范
status: active
---

# DSP ATTACKDEFENDSTC（显示攻击防范统计信息）

## 功能

该命令用于显示攻击防范统计计数。

不指定参数时，查询所有攻击类型的统计信息；当指定参数时，可以查询指定攻击类型的统计信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ATTACKTYPE | 攻击类型 | 可选必选说明：可选参数<br>参数含义：该参数用于标识攻击类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ABNORMAL：畸形报文。<br>- FRAGMENT：分片报文。<br>- TCP-SYN：TCP-SYN报文。<br>- UDP-FLOOD：UDP泛洪报文。<br>- ICMP-FLOOD：ICMP泛洪报文。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/ATTACKDEFENDSTC]] · 攻击防范统计信息（ATTACKDEFENDSTC）

## 使用实例

显示攻击防范统计计数信息：

```
DSP ATTACKDEFENDSTC:;
```

```

        RETCODE = 0  操作成功

        结果如下：
        ------------------------
        攻击类型          报文总数    丢弃的报文总数    通过的报文总数

        畸形报文          0           0                 0
        分片报文          0           0                 0
        ICMP泛洪报文      90168       0                 90168
        TCP-SYN报文       27722       0                 27722
        UDP泛洪报文       0           0                 0
        (结果个数 = 5)
        ---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示攻击防范统计信息（DSP-ATTACKDEFENDSTC）_50280910.md`
