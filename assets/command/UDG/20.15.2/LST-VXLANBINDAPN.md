---
id: UDG@20.15.2@MMLCommand@LST VXLANBINDAPN
type: MMLCommand
name: LST VXLANBINDAPN（查询VXLAN隧道组绑定APN）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: VXLANBINDAPN
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 路径管理
- VXLAN路径管理
- VXLAN隧道绑定APN
status: active
---

# LST VXLANBINDAPN（查询VXLAN隧道组绑定APN）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询VXLAN隧道组与apn的绑定关系。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数必须已经通过ADD APN命令配置。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/VXLANBINDAPN]] · VXLAN隧道组绑定APN（VXLANBINDAPN）

## 使用实例

查询所有与APN绑定的VXLAN隧道组：

```
LST VXLANBINDAPN:;
```

```

RETCODE = 0  操作成功

VXLAN隧道绑定APN信息
--------------------
        APN  =  apn1
VXLAN组名称  =  vxlangrp2
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-VXLANBINDAPN.md`
