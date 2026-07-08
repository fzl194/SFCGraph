---
id: UDG@20.15.2@MMLCommand@LST CUSTATECHK
type: MMLCommand
name: LST CUSTATECHK（查询SMF和UPF时间一致性检测）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: CUSTATECHK
command_category: 查询类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 配置校验控制
- CP和UP关键配置不一致策略
status: active
---

# LST CUSTATECHK（查询SMF和UPF时间一致性检测）

## 功能

**适用NF：UPF**

查询SMF和UPF时间一致性检测参数。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/CUSTATECHK]] · SMF和UPF时间一致性检测（CUSTATECHK）

## 使用实例

查询SMF和UPF时间一致性检测参数：

```
%%LST CUSTATECHK:;
```

```
%%
RETCODE = 0  Operation succeeded

Time Inconsistency Between SMF and UPF
--------------------------------------
UTC Time Consistency Check Switch  =  ENABLE
        Detection error threshold  =  1000
           Alarm Report Threshold  =  10
            Alarm Clear Threshold  =  5
(Number of results = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询SMF和UPF时间一致性检测（LST-CUSTATECHK）_79440357.md`
