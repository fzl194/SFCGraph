---
id: UNC@20.15.2@MMLCommand@LST IUREPLMN
type: MMLCommand
name: LST IUREPLMN（查询3G重定向PLMN）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IUREPLMN
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- 基于区域SGSN共享管理
- 3G重定向PLMN
status: active
---

# LST IUREPLMN（查询3G重定向PLMN）

## 功能

**适用网元：SGSN**

该命令用于查询3G重定向PLMN。

## 注意事项

- 此命令执行后立即生效。
- 此命令不对移动虚拟网络运营商生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [3G重定向PLMN（IUREPLMN）](configobject/UNC/20.15.2/IUREPLMN.md)

## 使用实例

查询3G重定向PLMN。

LST IUREPLMN:;

```
%%LST IUREPLMN:;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
  移动国家码 =  460
  移动国家码 =  05
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询3G重定向PLMN(LST-IUREPLMN)_84095370.md`
