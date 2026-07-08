---
id: UDG@20.15.2@MMLCommand@DSP VTEPSTAT
type: MMLCommand
name: DSP VTEPSTAT（显示Vtep状态）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: VTEPSTAT
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
- 查询VTEP状态
status: active
---

# DSP VTEPSTAT（显示Vtep状态）

## 功能

**适用NF：PGW-U、UPF**

该命令用于显示与指定VXLAN Group绑定的VTEP的信息，包括VTEP的名称。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VXLANGRPNAME | VXLAN隧道组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示VXLAN链路组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@VTEPSTAT]] · Vtep状态（VTEPSTAT）

## 使用实例

查询与VXLAN Group“test”绑定的VTEP信息：

```
DSP VTEPSTAT: VXLANGRPNAME="test";
```

```

RETCODE = 0  操作成功。

VTEP状态
-----------
VXLAN隧道端点名称   =  test
地址信息  =  10.0.0.1
服务器状态 =  正常
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-VTEPSTAT.md`
