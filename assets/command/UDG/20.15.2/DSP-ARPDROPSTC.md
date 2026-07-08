---
id: UDG@20.15.2@MMLCommand@DSP ARPDROPSTC
type: MMLCommand
name: DSP ARPDROPSTC（查询ARP丢弃报文统计）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: ARPDROPSTC
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- ARP
status: active
---

# DSP ARPDROPSTC（查询ARP丢弃报文统计）

## 功能

该命令用于查询ARP丢弃报文统计。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/ARPDROPSTC]] · ARP丢弃报文统计（ARPDROPSTC）

## 使用实例

查看ARP丢弃报文统计：

```
DSP ARPDROPSTC:;
```

```

        RETCODE = 0  操作成功

        结果如下
        ------------------------
        源IP地址     目的IP地址    源MAC地址        目的MAC地址        接口名称         丢弃类型            报文丢弃计数    最后丢弃报文的时间

        10.10.10.10  10.10.14.1    00E0-FC12-3456   FFFF-FFFF-FFFF     Ethernet64/0/4   接口DOWN            12              2017-09-11 18:40:45
        10.10.10.10  10.10.13.1    00E0-FC12-3457   FFFF-FFFF-FFFF     Ethernet64/0/3   IP地址非法          12              2017-09-11 18:40:36
        10.10.13.1   10.10.13.1    00E0-FC12-3458   FFFF-FFFF-FFFF     Ethernet64/0/3   IP地址不在同网段    4               2017-09-11 18:40:34
        (结果个数 = 3)
        ---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-ARPDROPSTC.md`
