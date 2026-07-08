---
id: UNC@20.15.2@MMLCommand@LST BATCHCUTFUNC
type: MMLCommand
name: LST BATCHCUTFUNC（查询分批割接功能）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: BATCHCUTFUNC
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- 分批割接功能
status: active
---

# LST BATCHCUTFUNC（查询分批割接功能）

## 功能

**适用网元：SGSN、MME**

在 **[MOCN](../../../../../../../../网络部署/特性部署/UNC特性指南/网络共享功能/WSFD-207003 基于LTE的网络共享（MOCN）_68260814.md)** 组网下的两网融合项目中，基于区域逐步融合，需要配置基于特定区域PLMN的使用策略。该命令用于查询分批割接功能。

## 注意事项

- 此命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/BATCHCUTFUNC]] · 分批割接功能（BATCHCUTFUNC）

## 使用实例

查询分批割接功能。

```
LST BATCHCUTFUNC:;
%%LST BATCHCUTFUNC:;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
            4G分批割接开关 =  YES
割接区到非割接区S1切换类型 =  NO
            3G分批割接开关 =  NO
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询分批割接功能(LST-BATCHCUTFUNC)_19313885.md`
