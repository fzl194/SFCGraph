---
id: UNC@20.15.2@MMLCommand@DSP ARPHISTORY
type: MMLCommand
name: DSP ARPHISTORY（查询ARP表项变更历史）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: ARPHISTORY
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

# DSP ARPHISTORY（查询ARP表项变更历史）

## 功能

该命令用于查看ARP表项变更历史。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/ARPHISTORY]] · ARP表项变更历史（ARPHISTORY）

## 使用实例

查看ARP表项变更历史：

```
DSP ARPHISTORY:;
```

```

        RETCODE = 0  操作成功

        结果如下
        -------------------------
        操作类型    变更类型    IPv4地址    接口名称        MAC地址         VLAN ID值    内层VLAN ID值    变更时间

        增加        报文        10.10.7.14  Ethernet64/0/5  00E0-FC12-3456  0            0                2017-06-06 11:01:56
        修改        报文        10.10.7.1   Ethernet64/0/5  00E0-FC12-3457  0            0                2017-06-06 11:03:05
        删除        报文        10.10.7.1   Ethernet64/0/5  00E0-FC12-3458  0            0                2017-06-06 11:03:50
        (结果个数 = 3)
        ---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询ARP表项变更历史（DSP-ARPHISTORY）_50120718.md`
