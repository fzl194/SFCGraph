---
id: UDG@20.15.2@MMLCommand@LST SNSSAI
type: MMLCommand
name: LST SNSSAI（查询NF支持的网络切片选择标识）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SNSSAI
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 网络切片管理
- 网络切片选择标识
status: active
---

# LST SNSSAI（查询NF支持的网络切片选择标识）

## 功能

**适用NF：UPF**

该命令用于显示UPF上配置的所有网络切片选择标识。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/SNSSAI]] · NF支持的网络切片选择标识（SNSSAI）

## 使用实例

获取当前UPF配置的所有网络切片选择标识：

```
LST SNSSAI:;
```

```

RETCODE = 0操作成功。

S-NSSAI信息
---------------
切片/服务类型  =  255
   切片区分码  =  134576
   配置域名称  =  NULL
（结果个数 = 1）
--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-SNSSAI.md`
