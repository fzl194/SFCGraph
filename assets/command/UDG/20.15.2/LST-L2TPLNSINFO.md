---
id: UDG@20.15.2@MMLCommand@LST L2TPLNSINFO
type: MMLCommand
name: LST L2TPLNSINFO（查询L2TP组的LNS信息）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: L2TPLNSINFO
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- L2TP隧道管理
- L2tp组Lns信息
status: active
---

# LST L2TPLNSINFO（查询L2TP组的LNS信息）

## 功能

**适用NF：PGW-U、UPF**

用于查询L2TP组绑定的LNS信息。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPID | L2TP组号 | 可选必选说明：可选参数<br>参数含义：指定L2TP组号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～1500。<br>默认值：无<br>配置原则：该参数使用ADD L2TPGROUP命令配置生成。 |
| LNSNO | LNS序号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定添加LNS的序号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～30。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@L2TPLNSINFO]] · L2TP组的LNS信息（L2TPLNSINFO）

## 使用实例

查询L2TP组绑定的LNS信息：

```
LST L2TPLNSINFO:;
```

```

RETCODE = 0 操作成功。

RETCODE = 0  Operation succeeded

L2tp Group Lns Info
----------------------
                   L2TP Group ID  =  1
             LNS Sequence Number  =  1
                   Lns IP version = IPV4
                 LNS IPv4 Address = 10.1.1.1
                 LNS IPv6 Address = ::
                     LNS Password = *****
             Confirm LNS Password = *****
(Number of results = 1)

--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-L2TPLNSINFO.md`
