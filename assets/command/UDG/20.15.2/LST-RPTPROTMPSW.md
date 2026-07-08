---
id: UDG@20.15.2@MMLCommand@LST RPTPROTMPSW
type: MMLCommand
name: LST RPTPROTMPSW（查询业务报表承载协议映射开关）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: RPTPROTMPSW
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 业务报表管理
- 报表功能管理
- 报表承载协议映射开关
status: active
---

# LST RPTPROTMPSW（查询业务报表承载协议映射开关）

## 功能

**适用NF：UPF**

该命令用来查询业务报表承载协议映射开关。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/RPTPROTMPSW]] · 业务报表承载协议映射开关（RPTPROTMPSW）

## 使用实例

查询业务报表承载协议映射开关：

```
LST RPTPROTMPSW:;
```

```

RETCODE = 0  操作成功.

业务报表承载协议映射开关
-------------------------------------------------
功能开关  =  使能
(结果个数 = 1)
--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-RPTPROTMPSW.md`
