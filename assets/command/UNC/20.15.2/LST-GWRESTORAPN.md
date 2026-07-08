---
id: UNC@20.15.2@MMLCommand@LST GWRESTORAPN
type: MMLCommand
name: LST GWRESTORAPN（查询网关容灾APN）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GWRESTORAPN
command_category: 查询类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- 网关故障管理
status: active
---

# LST GWRESTORAPN（查询网关容灾APN）

## 功能

**适用网元：MME**

本命令用于查询应用S-GW/P-GW容灾功能的APNNI。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [网关容灾APN（GWRESTORAPN）](configobject/UNC/20.15.2/GWRESTORAPN.md)

## 使用实例

本命令用于查询应用S-GW/P-GW容灾功能的APNNI：

LST GWRESTORAPN:;

```
%%LST GWRESTORAPN:;%%
RETCODE = 0  操作成功。

操作结果如下
------------
APN网络标识  =  HUAWEI.COM
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询网关容灾APN(LST-GWRESTORAPN)_72345683.md`
