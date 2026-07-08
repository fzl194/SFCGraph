---
id: UNC@20.15.2@MMLCommand@LST ROAMMGMTPARA
type: MMLCommand
name: LST ROAMMGMTPARA（查询漫游管理参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: ROAMMGMTPARA
command_category: 查询类
applicable_nf:
- AMF
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- 漫游参数管理
status: active
---

# LST ROAMMGMTPARA（查询漫游管理参数）

## 功能

**适用NF：AMF、SMF**

该命令用于查询漫游管理参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/ROAMMGMTPARA]] · 漫游管理参数（ROAMMGMTPARA）

## 使用实例

查询漫游管理参数。

```
%%LST ROAMMGMTPARA:;%%
RETCODE = 0 操作成功

结果如下
------------------------
识别关口局NF开关 = OFF
避免网元混用开关 = OFF
（结果个数=1）

---- END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询漫游管理参数（LST-ROAMMGMTPARA）_06385409.md`
