---
id: UNC@20.15.2@MMLCommand@DSP COMGTPCPATHNUM
type: MMLCommand
name: DSP COMGTPCPATHNUM（显示UAM GTP-C路径数量）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: COMGTPCPATHNUM
command_category: 查询类
applicable_nf:
- AMF
- MME
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- GTP-C接口配置管理
- GTP-C路径维护
status: active
---

# DSP COMGTPCPATHNUM（显示UAM GTP-C路径数量）

## 功能

**适用NF：AMF、MME、SGSN**

该命令用于显示UAM GTP-C路径数量。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [UAM GTP-C路径数量（COMGTPCPATHNUM）](configobject/UNC/20.15.2/COMGTPCPATHNUM.md)

## 使用实例

DSP COMGTPCPATHNUM:;

```
%%DSP COMGTPCPATHNUM:;%%
RETCODE = 0  操作成功

结果如下
------------------------
     AMF路径数量  =  4
MME/SGSN路径数量  =  0
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示UAM-GTP-C路径数量（DSP-COMGTPCPATHNUM）_24956624.md`
