---
id: UNC@20.15.2@MMLCommand@LST NFGROUPID
type: MMLCommand
name: LST NFGROUPID（查询NF群组信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NFGROUPID
command_category: 查询类
applicable_nf:
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- NF GROUP信息管理
status: active
---

# LST NFGROUPID（查询NF群组信息）

## 功能

**适用NF：SMSF**

该命令用于查询NF实例支持的群组信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/NFGROUPID]] · NF群组信息（NFGROUPID）

## 使用实例

查询NF支持的群组信息。

```
%%LST NFGROUPID:;%%
RETCODE = 0  操作成功

结果如下
--------
NF实例名称  =  SMSF_Instance_0
  群组标识  =  GROUP01
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NFGROUPID.md`
