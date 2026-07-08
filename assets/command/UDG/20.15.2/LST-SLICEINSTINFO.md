---
id: UDG@20.15.2@MMLCommand@LST SLICEINSTINFO
type: MMLCommand
name: LST SLICEINSTINFO（显示切片实例信息）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SLICEINSTINFO
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 网络切片管理
- 网络切片实例信息
status: active
---

# LST SLICEINSTINFO（显示切片实例信息）

## 功能

**适用NF：UPF**

此命令用于显示切片实例信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@SLICEINSTINFO]] · 切片实例信息（SLICEINSTINFO）

## 使用实例

查询切片实例信息：

```
LST SLICEINSTINFO:;
```

```

RETCODE = 0  操作成功

网络切片实例信息
----------------
   NsiInfo  =  test
   NSSI ID  =  0
配置域名称  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-SLICEINSTINFO.md`
