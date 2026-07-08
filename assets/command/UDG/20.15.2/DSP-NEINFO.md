---
id: UDG@20.15.2@MMLCommand@DSP NEINFO
type: MMLCommand
name: DSP NEINFO（显示 NeInfo）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: NEINFO
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- DN管理
- NE信息管理
- NE类型管理
status: active
---

# DSP NEINFO（显示 NeInfo）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

显示网元形态列表以及NF列表。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/NEINFO]] ·  NeInfo（NEINFO）

## 使用实例

列出当前网元形态列表：

```
DSP NEINFO;
```

```

RETCODE = 0 操作成功。

结果如下
--------
网元基本信息 =
NE type list = UPF,SGWU,PGWU 
NF list = FrameWork，UP, NAT 
(Number of results = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-NEINFO.md`
