---
id: UNC@20.15.2@MMLCommand@LST BWRATIO
type: MMLCommand
name: LST BWRATIO（查询带宽占用比例表）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: BWRATIO
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 数据转发管理
- 转发资源管理
- 带宽资源管理
- 带宽占用比例管理
status: active
---

# LST BWRATIO（查询带宽占用比例表）

## 功能

**适用网元：SGSN**

该命令用于查询会话类和流类业务所用的静态带宽能占用的可用带宽的最大百分比。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@BWRATIO]] · 带宽占用比例表（BWRATIO）

## 使用实例

查询QoS级别为会话类和流类业务所用的静态带宽能占用的可用带宽的最大百分比：

LST BWRATIO:;

```
%%LST BWRATIO:;%%
RETCODE = 0  操作成功。

输出结果如下
-------------------------
静态带宽最大百分比(%)  =  100
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-BWRATIO.md`
