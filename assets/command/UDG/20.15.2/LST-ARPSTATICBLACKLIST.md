---
id: UDG@20.15.2@MMLCommand@LST ARPSTATICBLACKLIST
type: MMLCommand
name: LST ARPSTATICBLACKLIST（查询ARP静态黑名单）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: ARPSTATICBLACKLIST
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- ARP管理
- ARP防欺骗配置
status: active
---

# LST ARPSTATICBLACKLIST（查询ARP静态黑名单）

## 功能

该命令用于查询ARP静态黑名单。

当设备上创建了ARP静态黑名单，可用该命令查询已创建的ARP静态黑名单信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPADDR | IP地址 | 可选必选说明：可选参数<br>参数含义：该参数用于指定ARP静态黑名单的IP地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。IP地址0.0.0.0～255.255.255.255。<br>默认值：无 |
| MACADDR | MAC地址 | 可选必选说明：可选参数<br>参数含义：该参数用于指定ARP静态黑名单的MAC地址。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～48。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/ARPSTATICBLACKLIST]] · ARP静态黑名单（ARPSTATICBLACKLIST）

## 使用实例

不指定参数时，查询VNFC上所有ARP静态黑名单：

```
LST ARPSTATICBLACKLIST:;
```

```

RETCODE = 0  操作成功。

结果如下
--------
 IP地址  =  10.1.1.2
MAC地址  =  00E0-FC12-3456
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询ARP静态黑名单（LST-ARPSTATICBLACKLIST）_50121486.md`
