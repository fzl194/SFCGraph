---
id: UNC@20.15.2@MMLCommand@LST UECAPBYIMSI
type: MMLCommand
name: LST UECAPBYIMSI（查询UE无线能力策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: UECAPBYIMSI
command_category: 查询类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- UE无线能力策略
status: active
---

# LST UECAPBYIMSI（查询UE无线能力策略）

## 功能

**适用网元：MME**

该命令用于查询UE无线能力策略 。

## 注意事项

此命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 操作的配置对象

- [[configobject/UNC/20.15.2/UECAPBYIMSI]] · UE无线能力策略（UECAPBYIMSI）

## 使用实例

查询UE无线能力策略:

LST UECAPBYIMSI:;

```
%%LST UECAPBYIMSI:;%%
RETCODE = 0  操作成功

查询结果如下
------------------------
IMSI  =  460011418603055
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-UECAPBYIMSI.md`
