---
id: UDG@20.15.2@MMLCommand@DSP IPFARM
type: MMLCommand
name: DSP IPFARM（查询IPFarm）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: IPFARM
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- DN管理
- IP Farm 管理
- IP Farm参数
status: active
---

# DSP IPFARM（查询IPFarm）

## 功能

**适用NF：PGW-U、UPF**

该命令用于显示对应IP farm的信息，包括IP farm的名称。如果参数为空，则显示所有IP farm的信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPFARMNAME | IP-Farm名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置IP farm名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/IPFARM]] · IPFarm（IPFARM）

## 使用实例

查询一条IP farm记录：

```
DSP IPFARM:;
```

```

RETCODE = 0 操作成功。

IPFarm信息
----------
IP-Farm名称 = test
IP Farm可用服务器数目 = 2
IP Farm服务器数目 = 2
(结果个数 = 1)
--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询IPFarm（DSP-IPFARM）_82837054.md`
