---
id: UDG@20.15.2@MMLCommand@LST VTEPBINDGRP
type: MMLCommand
name: LST VTEPBINDGRP（查询VXLAN隧道端点绑定隧道组）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: VTEPBINDGRP
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
- VTEP绑定VXLAN隧道组
status: active
---

# LST VTEPBINDGRP（查询VXLAN隧道端点绑定隧道组）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询VXLAN隧道端点与隧道组的绑定关系。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VXLANGRPNAME | VXLAN组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VXLAN隧道组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/VTEPBINDGRP]] · VXLAN隧道端点绑定隧道组（VTEPBINDGRP）

## 使用实例

查询VXLAN隧道组为vxlangrp的绑定关系的相关信息：

```
LST VTEPBINDGRP: VXLANGRPNAME="vxlangrp";
```

```

RETCODE = 0  操作成功

VXLAN隧道端点绑定隧道组信息
----------------------------
VXLAN组名称  =  vxlangrp
   VTEP名称  =  vtep1
 主备用类型  =  主用
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询VXLAN隧道端点绑定隧道组（LST-VTEPBINDGRP）_80994832.md`
