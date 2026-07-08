---
id: UNC@20.15.2@MMLCommand@LST UPRESELECTFUNC
type: MMLCommand
name: LST UPRESELECTFUNC（查询UP重选功能）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: UPRESELECTFUNC
command_category: 查询类
applicable_nf:
- SMF
- GGSN
- PGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UPF选择管理
- UPF重选
status: active
---

# LST UPRESELECTFUNC（查询UP重选功能）

## 功能

**适用NF：SMF、GGSN、PGW-C**

该命令用来查询UP重选相关的功能配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/UPRESELECTFUNC]] · UP重选功能（UPRESELECTFUNC）

## 使用实例

查看触发UP重选的场景：

```
%%LST UPRESELECTFUNC:;%%
RETCODE = 0  操作成功

结果如下
--------
UP重选场景  =  SMF分配地址失败
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-UPRESELECTFUNC.md`
