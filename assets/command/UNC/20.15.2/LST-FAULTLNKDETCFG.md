---
id: UNC@20.15.2@MMLCommand@LST FAULTLNKDETCFG
type: MMLCommand
name: LST FAULTLNKDETCFG（查询故障链路探测配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: FAULTLNKDETCFG
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 扩展调测
- 平台调测
- 故障链路探测管理
status: active
---

# LST FAULTLNKDETCFG（查询故障链路探测配置）

## 功能

**适用网元：SGSN、MME**

该命令用于查询故障链路探测功能配置。

## 注意事项

无

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/FAULTLNKDETCFG]] · 故障链路探测配置（FAULTLNKDETCFG）

## 使用实例

查询故障链路探测配置：

LST FAULTLNKDETCFG:;

```
%%LST FAULTLNKDETCFG:;%%
RETCODE = 0  操作成功

操作结果如下
------------------
 控制开关  =  关
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询故障链路探测配置(LST-FAULTLNKDETCFG)_72225551.md`
