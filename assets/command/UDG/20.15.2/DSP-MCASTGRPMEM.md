---
id: UDG@20.15.2@MMLCommand@DSP MCASTGRPMEM
type: MMLCommand
name: DSP MCASTGRPMEM（查询组播组成员状态）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: MCASTGRPMEM
command_category: 查询类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 5G LAN管理
- 5G LAN静态组播配置
- 组播组成员配置
status: active
---

# DSP MCASTGRPMEM（查询组播组成员状态）

## 功能

**适用NF：UPF**

该命令用于查询静态组播组内成员激活状态。

## 注意事项

- 该命令执行后立即生效。
- 状态激活显示为Active，状态未激活显示为Inactive。
- IMSI类型的组播组成员，只有当该IMSI对应的用户激活在该静态组播组绑定的5G LAN组会话下，状态才是Active。
- VTEP类型的组播组成员，链路状态UP时，状态为Active。
- DFSR PAIR类型的组播组成员，结对中有一个用户激活，状态就显示为Active。
- ETHERNETPDN类型的组播组成员，状态只显示为Active。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCASTGRPNAME | 组播组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于配置组播组的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63，区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@MCASTGRPMEM]] · 组播组成员配置（MCASTGRPMEM）

## 使用实例

查询静态组播组成员状态：

```
DSP MCASTGRPMEM: MCASTGRPNAME="group";
```

```

RETCODE = 0  操作成功

组播组成员状态
--------------
组播组名称  成员类型  成员标识    状态

group       IMSI                               1234567748  Inactive
group       IMSI                               123456778   Inactive
group       VTEP                               vtep1       Inactive
group       Ethernet PDN                       1           Active
group       Dual Fed Selective Receiving Pair  1           Inactive
(结果个数 = 5)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-MCASTGRPMEM.md`
