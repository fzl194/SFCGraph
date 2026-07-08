---
id: UDG@20.15.2@MMLCommand@DSP IPFARMSERVER
type: MMLCommand
name: DSP IPFARMSERVER（查询IPFarm服务器状态）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: IPFARMSERVER
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
- IP Farm服务器
status: active
---

# DSP IPFARMSERVER（查询IPFarm服务器状态）

## 功能

**适用NF：PGW-U、UPF**

该命令用于显示该IP farm服务器所在的IP farm中的所有IP farm服务器信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPFARMNAME | IP-Farm名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置IP farm名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/IPFARMSERVER]] · IPFarmServer（IPFARMSERVER）

## 使用实例

查询一个IP farm下的全部服务器：

```
DSP IPFARMSERVER:IPFARMNAME="test";
```

```

RETCODE = 0 操作成功。

IPFarmServer信息
----------------
IP-Farm名称 = f2
   地址信息 = fdff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
 服务器状态 = 正常
(结果个数 = 1)
--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-IPFARMSERVER.md`
