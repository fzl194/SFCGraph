---
id: UNC@20.15.2@MMLCommand@LST MSCSELPLCY
type: MMLCommand
name: LST MSCSELPLCY（查询MSC选择策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: MSCSELPLCY
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- Sv接口管理
- MSC选择策略
status: active
---

# LST MSCSELPLCY（查询MSC选择策略）

## 功能

**适用网元：MME**

该命令用于查询MSC域名解析策略。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/MSCSELPLCY]] · MSC选择策略（MSCSELPLCY）

## 使用实例

查询Sv接口域名解析采用的是RAI还是LAI解析MSC，使用该命令：

LST MSCSELPLCY:;

```
%%LST MSCSELPLCY:;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
Sv接口域名解析策略 = LAI
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询MSC选择策略(LST-MSCSELPLCY)_72345577.md`
