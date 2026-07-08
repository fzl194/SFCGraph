---
id: UDG@20.15.2@MMLCommand@DSP VXLANGRPSTAT
type: MMLCommand
name: DSP VXLANGRPSTAT（显示VXLAN组链路状态）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: VXLANGRPSTAT
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
- 查询VXLAN Group状态
status: active
---

# DSP VXLANGRPSTAT（显示VXLAN组链路状态）

## 功能

**适用NF：PGW-U、UPF**

该命令用于显示对应VXLAN Group的信息，包括VXLAN Group的名称。如果参数为空，则显示所有VXLAN Group的信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VXLANGRPNAME | VXLAN隧道组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示VXLAN链路组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/VXLANGRPSTAT]] · VXLAN组链路状态（VXLANGRPSTAT）

## 使用实例

查询一条VXLAN隧道组名称为test的VXLAN Group记录：

```
DSP VXLANGRPSTAT: VXLANGRPNAME="test";
```

```

RETCODE = 0 操作成功。

VXLAN Group信息
----------------
VXLAN隧道组名称  =  test
VXLAN Group 可用服务器数目  =  1
VXLAN Group 服务器数目  =  1
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示VXLAN组链路状态（DSP-VXLANGRPSTAT）_42091189.md`
