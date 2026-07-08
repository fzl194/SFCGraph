---
id: UDG@20.15.2@MMLCommand@LST NGBINDMCASTGRP
type: MMLCommand
name: LST NGBINDMCASTGRP（查询5G LAN实例绑定组播组配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: NGBINDMCASTGRP
command_category: 查询类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 5G LAN管理
- 5G LAN静态组播配置
- 5G LAN实例绑定组播组
status: active
---

# LST NGBINDMCASTGRP（查询5G LAN实例绑定组播组配置）

## 功能

**适用NF：UPF**

该命令用于查询静态组播组与5G LAN会话实例绑定记录。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VNINSTANCE | 5G LAN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定5G LAN会话实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为18～37。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/NGBINDMCASTGRP]] · 5G LAN实例绑定组播组配置（NGBINDMCASTGRP）

## 使用实例

查询静态组播组和5G LAN会话实例绑定关系：

```
%%LST NGBINDMCASTGRP:;
```

```
%%
RETCODE = 0  操作成功

5G LAN实例绑定组播组信息
------------------------
5G LAN实例名称  =  a0000001-460-003-01
    组播组名称  =  group1
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询5G-LAN实例绑定组播组配置（LST-NGBINDMCASTGRP）_15711178.md`
