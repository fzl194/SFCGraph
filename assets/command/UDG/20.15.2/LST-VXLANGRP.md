---
id: UDG@20.15.2@MMLCommand@LST VXLANGRP
type: MMLCommand
name: LST VXLANGRP（查询VXLAN组）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: VXLANGRP
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
- VXLAN组信息
status: active
---

# LST VXLANGRP（查询VXLAN组）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询VXLAN隧道组。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GRPNAME | VXLAN隧道组名称 | 可选必选说明：可选参数<br>参数含义：VXLAN隧道组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/VXLANGRP]] · VXLAN组（VXLANGRP）

## 使用实例

查看名为vxlangrp的VXLAN隧道组的相关信息：

```
LST VXLANGRP: GRPNAME="vxlangrp";
```

```

RETCODE = 0  操作成功

VXLAN组信息
-----------
       VXLAN隧道组名称  =  vxlangrp
       VXLAN隧道源接口  =  nxucif1/1/0
          健康检查开关  =  使能
        时间阈值（秒）  =  6
      健康检查成功次数  =  3
      健康检查失败次数  =  3
Ping探测超时时长（秒）  =  2
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-VXLANGRP.md`
