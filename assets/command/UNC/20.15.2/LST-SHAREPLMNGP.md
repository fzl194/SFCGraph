---
id: UNC@20.15.2@MMLCommand@LST SHAREPLMNGP
type: MMLCommand
name: LST SHAREPLMNGP（查询共享PLMN群组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SHAREPLMNGP
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
- 基于区域MME共享管理
- 共享PLMN群组管理
status: active
---

# LST SHAREPLMNGP（查询共享PLMN群组）

## 功能

**适用网元：MME**

在 **[MOCN](../../../../../../../../../网络部署/特性部署/UNC特性指南/网络共享功能/WSFD-207003 基于LTE的网络共享（MOCN）_68260814.md)** 组网下的两网融合项目中，基于区域逐步融合，需要配置基于特定区域PLMN的使用策略。该命令用于查询共享PLMN群组。

## 注意事项

- 此命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/SHAREPLMNGP]] · 共享PLMN群组（SHAREPLMNGP）

## 使用实例

查询共享PLMN群组。

LST SHAREPLMNGP:;

```
%%LST SHAREPLMNGP:;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
PLMN群组标识 =  1
PLMN群组名称 =  HUAWEI1
 (结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询共享PLMN群组(LST-SHAREPLMNGP)_83887094.md`
